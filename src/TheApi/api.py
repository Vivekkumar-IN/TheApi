import os
import re
import random
import string
import textwrap
from io import BytesIO
from typing import List, Union
from os.path import realpath

import aiohttp
import aiofiles
import requests
from PIL import Image, ImageOps, ImageDraw, ImageFont

from .func import FilePath


class TheApi:
    def __init__(self):
        self.base_urls = {
            "advice": "https://api.adviceslip.com/advice",
            "animechan": "https://animechan.io/api/v1/quotes/random",
            "bing_image": "https://www.bing.com/images/async",
            "carbon": "https://carbonara.solopov.dev/api/cook",
            "cat": "https://api.thecatapi.com/v1/images/search",
            "dog": "https://random.dog/woof.json",
            "domain": "https://api.domainsdb.info/v1/domains/search?domain={domain}&zone={zone}",
            "fox": "https://randomfox.ca/floof/",
            "font": "https://github.com/google/fonts/raw/main/ofl/poetsenone/PoetsenOne-Regular.ttf",
            "hindi_jokes": "https://hindi-jokes-api.onrender.com/jokes?api_key=93eeccc9d663115eba73839b3cd9",
            "hindi_quote": "https://hindi-quotes.vercel.app/random",
            "image": "https://graph.org/file/1f8d00177ac2429b101b9.jpg",
            "jokes": "https://v2.jokeapi.dev/joke/Any",
            "meme": "https://meme-api.com/gimme",
            "neko_url": "https://nekos.best/api/v2/{endpoint}?amount={amount}",
            "neko_hug": "https://nekos.best/api/v2/hug?amount={}",
            "pypi": "https://pypi.org/pypi",
            "qr_gen": "https://api.stakdek.de/api/qr/gen?data={query}",
            "quote": "https://api.quotable.io/random",
            "random_word": "https://random-word-api.herokuapp.com/word",
            "useless_fact": "https://uselessfacts.jsph.pl/api/v2/facts/random",
            "wikipedia_search": "https://en.wikipedia.org/w/api.php",
            "words": "https://random-word-api.herokuapp.com/word",
            "word_info": "https://api.dictionaryapi.dev/api/v2/entries/en/{word}",
            "upload": "https://envs.sh/",
        }

    async def _make_request(
        self,
        url: str,
        method: str = "GET",
        params: dict = None,
        data: dict = None,
        files: dict = None,
        headers: dict = None,
        verify: bool = True,
        return_content: bool = False,
    ) -> Union[dict, str, bytes]:
        """
        Makes an asynchronous HTTP request to the specified URL with optional parameters, headers, and data.

        Args:
            url (str): The URL to send the request to.
            method (str, optional): The HTTP method to use (e.g., "GET", "POST"). Defaults to "GET".
            params (dict, optional): Query parameters to include in the request. Defaults to None.
            data (dict, optional): Data to include in the request body (for POST requests). Defaults to None.
            files (dict, optional): Files to upload with the request, if applicable. Defaults to None.
            headers (dict, optional): Headers to include in the request. Defaults to None.
            verify (bool, optional): Whether to verify SSL certificates. Defaults to True.
            return_content (bool, optional): If True, returns the raw content of the response. Defaults to False.

        Returns:
            Union[dict, str, bytes]: The response content:
                - JSON response as a dictionary if the response is JSON-formatted.
                - Text response as a string if the response is plain text.
                - Raw bytes if `return_content` is True.

        Raises:
            ValueError: If the request fails due to a client error or invalid response.
        """
        async with aiohttp.ClientSession() as session:
            try:
                async with session.request(
                    method=method,
                    url=url,
                    params=params,
                    data=data,
                    headers=headers,
                    ssl=verify,
                ) as response:
                    response.raise_for_status()
                    if return_content:
                        return await response.read()
                    if "application/json" in response.headers.get("Content-Type", ""):
                        return await response.json()
                    return await response.text()
            except aiohttp.ClientResponseError as e:
                if e.status == 404 and e.message == "Not Found":
                    try:
                        async with aiohttp.ClientSession() as session:
                            async with session.get(url) as response:
                                return await response.json()
                    except Exception:
                        raise ValueError(f"Request failed: {str(e)}")
                raise ValueError(f"Request failed: {str(e)}")

            except Exception as e:
                raise ValueError(f"Unexpected error occurred: {str(e)}") from e

    def _rnd_str(self):
        """
        Generates a random string of 8 alphanumeric characters.

        Returns:
            str: A random 8-character alphanumeric string.
        """
        random_str = "".join(random.choices(string.ascii_letters + string.digits, k=8))
        return random_str

    async def animechan(self):
        """
        Fetches a random anime quote from the AnimeChan API.

        Returns:
            dict: Contains the quote content, anime name, and character details.
        """
        response = await self._make_request(self.base_urls["animechan"])
        return response["data"]

    async def get_advice(self):
        """
        Fetches a random piece of advice.

        Returns:
            str: A random advice message.
        """
        response = requests.get(self.base_urls["advice"]).json()
        return response["slip"]["advice"]

    async def get_jokes(self, amount=1):
        """
        Fetches a specified number of jokes.

        Args:
            amount (int, optional): The number of jokes to retrieve. Defaults to 1.

        Returns:
            str: A single joke if `amount` is 1. If `amount` > 1, returns numbered jokes as a formatted string.
        """
        url = self.base_urls["jokes"]
        params = {"type": "single", "amount": amount}
        response = await self._make_request(url, params=params)

        if amount == 1:
            return response["joke"]
        else:
            jokes = [joke["joke"] for joke in response["jokes"]]
            return "\n\n".join(f"{i + 1}. {joke}" for i, joke in enumerate(jokes))

    async def get_hindi_jokes(self):
        """
        Fetches a random Hindi joke.

        Returns:
            str: A random Hindi joke if available, or "No joke found" if not available.
        """
        response = await self._make_request(self.base_urls["hindi_jokes"])
        return response["jokeContent"] if response["status"] else "No joke found."

    async def gen_qr(self, query: str, file_path: str = None) -> str:
        """
        Generates a QR code and saves it to the specified file path.

        Args:
            query (str): The data to encode in the QR code.
            file_path (str, optional): The file path to save the QR code.
                                       Defaults to "downloads/{random_str}_qr.png".

        Returns:
            FilePath: The file path where the QR code was saved.
        """
        if file_path is None:
            file_path = os.path.join("downloads", f"{self._rnd_str()}_qr.png")

        os.makedirs(os.path.dirname(file_path), exist_ok=True)

        qr_content = await self._make_request(
            self.base_urls["qr_gen"].format(query=query), return_content=True
        )

        async with aiofiles.open(file_path, "wb") as f:
            await f.write(qr_content)

        return FilePath(realpath(file_path))

    async def get_uselessfact(self):
        """
        Fetches a random useless fact.

        Returns:
            str: A random useless fact.
        """
        response = await self._make_request(self.base_urls["useless_fact"])
        return response["text"]

    async def quote(self) -> str:
        """
        Fetches a random quote.

        Returns:
            str: The content of a random quote followed by the author's name.
        """
        data = await self._make_request(self.base_urls["quote"], verify=False)
        return f"{data['content']}\n\nauthor - {data['author']}"

    async def hindi_quote(self) -> str:
        """
        Fetches a random Hindi quote.

        Returns:
            str: The content of a random Hindi quote.
        """
        data = await self._make_request(self.base_urls["hindi_quote"])
        return data["quote"]

    async def random_word(self) -> str:
        """
        Fetches a random word.

        Returns:
            str: A random word if available; "None" if an error occurs.
        """
        params = {"number": 1}
        try:
            data = await self._make_request(
                self.base_urls["random_word"], params=params
            )
            return data[0]
        except RequestError:
            return "None"

    async def write(self, text):
        """
        Creates an image with text written on it, using a predefined template and font,
        and uploads the image after generation.

        Args:
            text (str): The text to be written on the image. Text exceeding 55 characters
                        per line will be wrapped, with up to 25 lines displayed.

        Returns:
            str: The URL of the uploaded image.

        Notes:
            A temporary image file is created, saved, and removed after uploading.
        """
        tryimg = "https://graph.org/file/1f8d00177ac2429b101b9.jpg"
        tryresp = requests.get(tryimg)
        img = Image.open(BytesIO(tryresp.content))
        draw = ImageDraw.Draw(img)

        font_url = "https://github.com/google/fonts/raw/main/ofl/poetsenone/PoetsenOne-Regular.ttf"
        font_response = requests.get(font_url)
        font = ImageFont.truetype(BytesIO(font_response.content), 24)

        x, y = 150, 140
        lines = []
        if len(text) <= 55:
            lines.append(text)
        else:
            all_lines = text.split("\n")
            for line in all_lines:
                if len(line) <= 55:
                    lines.append(line)
                else:
                    k = len(line) // 55
                    lines.extend(
                        line[((z - 1) * 55) : (z * 55)] for z in range(1, k + 2)
                    )

        umm = lines[:25]

        line_height = font.getbbox("hg")[3]
        linespacing = 41
        for line in umm:
            draw.text((x, y), line, fill=(1, 22, 55), font=font)
            y = y + linespacing

        downloads_folder = "downloads"
        os.makedirs(downloads_folder, exist_ok=True)

        file_path = os.path.join(downloads_folder, f"write_{self._rnd_str()}.jpg")

        img.save(file_path)

        return FilePath(realpath(file_path))

    async def carbon(self, query):
        """
        Generates a code snippet image using the Carbon API, saves it to the downloads folder,
        uploads it, and returns the URL of the uploaded image.

        Args:
            query (str): The code snippet to be rendered as an image.

        Returns:
            FilePath: The file path of the saved image.
        """
        async with aiohttp.ClientSession(
            headers={"Content-Type": "application/json"},
        ) as ses:
            params = {
                "code": query,
            }
            try:
                response = await ses.post(
                    "https://carbonara.solopov.dev/api/cook",
                    json=params,
                )
                response_data = await response.read()
            except aiohttp.client_exceptions.ClientConnectorError:
                raise ValueError("Can not reach the Host!")

            downloads_folder = "downloads"
            os.makedirs(downloads_folder, exist_ok=True)

            file_path = os.path.join(downloads_folder, f"carbon_{self._rnd_str()}.png")

            async with aiofiles.open(file_path, "wb") as f:
                await f.write(response_data)

            return FilePath(realpath(file_path))

    async def wikipedia(self, query):
        """
        Searches Wikipedia for a given query and retrieves the top result's summary, URL, and image.

        Args:
            query (str): The search term to look up on Wikipedia.

        Returns:
            dict: A dictionary containing information about the top search result, with keys:
                - title (str): The title of the Wikipedia article.
                - summary (str): A brief summary of the article's content.
                - url (str): The URL link to the full Wikipedia article.
                - image_url (str): The URL of the article's thumbnail image, or "No image available" if none exists.

            If no results are found, returns a dictionary with an "error" key.
        """
        search_url = self.base_urls["wikipedia_search"]

        params = {
            "action": "query",
            "list": "search",
            "srsearch": query,
            "format": "json",
        }

        search_response = await self._make_request(search_url, params=params)
        search_results = search_response.get("query", {}).get("search", [])

        if search_results:
            top_result = search_results[0]
            page_id = top_result["pageid"]
            summary_url = (
                f"{self.base_urls['wikipedia_search']}?action=query&prop=extracts|pageimages"
                f"&exintro&explaintext&piprop=thumbnail&pithumbsize=500&format=json&pageids={page_id}"
            )

            summary_response = await self._make_request(summary_url)
            pages = summary_response.get("query", {}).get("pages", {})
            page_info = pages.get(str(page_id), {})
            image_url = page_info.get("thumbnail", {}).get(
                "source", "No image available"
            )

            return {
                "title": top_result["title"],
                "summary": page_info.get("extract", "No summary available."),
                "url": f"https://en.wikipedia.org/?curid={page_id}",
                "image_url": image_url,
            }
        else:
            return {"error": "No search results found"}

    async def github_search(self, query, search_type="repositories", max_results=3):
        """
        Searches GitHub for various types of content.

        Args:
            query (str): The search query.
            search_type (str, optional): The type of search. Can be one of:
                - "repositories"
                - "users"
                - "organizations"
                - "issues"
                - "pull_requests"
                - "commits"
                - "topics"

                Defaults to "repositories".
            max_results (int, optional): The maximum number of results to return. Defaults to 3.

        Returns:
            list: A list of search results or an error message.
        """
        valid_search_types = [
            "repositories",
            "users",
            "organizations",
            "issues",
            "pull_requests",
            "commits",
            "topics",
        ]

        if search_type not in valid_search_types:
            return {
                "error": f"Invalid search type. Valid types are: {valid_search_types}"
            }

        url_mapping = {
            "pull_requests": "https://api.github.com/search/issues",
            "organizations": "https://api.github.com/search/users",
            "topics": "https://api.github.com/search/topics",
        }

        if search_type in url_mapping:
            url = url_mapping[search_type]
            if search_type == "pull_requests":
                query += " type:pr"
            elif search_type == "organizations":
                query += " type:org"
        else:
            url = f"https://api.github.com/search/{search_type}"

        headers = {"Accept": "application/vnd.github.v3+json"}
        params = {"q": query, "per_page": max_results}

        try:
            response = requests.get(url, headers=headers, params=params)
            response.raise_for_status()
            results = response.json()
            items = results.get("items", [])

            result_list = []

            for item in items:
                item_info = {}
                if search_type == "repositories":
                    item_info = {
                        "name": item["name"],
                        "full_name": item["full_name"],
                        "description": item["description"],
                        "url": item["html_url"],
                        "language": item.get("language"),
                        "stargazers_count": item.get("stargazers_count"),
                        "forks_count": item.get("forks_count"),
                    }
                elif search_type in ["users", "organizations"]:
                    item_info = {
                        "login": item["login"],
                        "id": item["id"],
                        "url": item["html_url"],
                        "avatar_url": item.get("avatar_url"),
                        "type": item.get("type"),
                        "site_admin": item.get("site_admin"),
                        "name": item.get("name"),
                        "company": item.get("company"),
                        "blog": item.get("blog"),
                        "location": item.get("location"),
                        "email": item.get("email"),
                        "bio": item.get("bio"),
                        "public_repos": item.get("public_repos"),
                        "public_gists": item.get("public_gists"),
                        "followers": item.get("followers"),
                        "following": item.get("following"),
                    }
                elif search_type in ["issues", "pull_requests"]:
                    item_info = {
                        "title": item["title"],
                        "user": item["user"]["login"],
                        "state": item["state"],
                        "url": item["html_url"],
                        "comments": item.get("comments"),
                        "created_at": item.get("created_at"),
                        "updated_at": item.get("updated_at"),
                        "closed_at": item.get("closed_at"),
                    }
                elif search_type == "commits":
                    item_info = {
                        "sha": item["sha"],
                        "commit_message": item["commit"]["message"],
                        "author": item["commit"]["author"]["name"],
                        "date": item["commit"]["author"]["date"],
                        "url": item["html_url"],
                    }
                elif search_type == "topics":
                    item_info = {
                        "name": item["name"],
                        "display_name": item.get("display_name"),
                        "short_description": item.get("short_description"),
                        "description": item.get("description"),
                        "created_by": item.get("created_by"),
                        "url": item.get("url") if "url" in item else None,
                    }

                result_list.append(item_info)

            return result_list

        except requests.exceptions.RequestException as e:
            return {"error": f"Request exception: {e}"}
        except requests.exceptions.HTTPError as e:
            return {
                "error": f"HTTP error: {e.response.status_code} - {e.response.text}"
            }
        except KeyError as e:
            return {"error": f"Key error: {e}"}
        except Exception as e:
            return {"error": f"Unexpected error: {e}"}

    async def words(self, num_words: int):
        """
        Fetches a specified number of random words.

        Args:
            num_words (int): The number of random words to retrieve.

        Returns:
            list: A list of random words if available; an empty list if no response is received.
        """
        url = f"{self.base_urls['words']}?number={num_words}"
        response = await self._make_request(url)
        return response if response else []

    async def cat(self):
        """
        Fetches a random cat image URL.

        Returns:
            str or None: The URL of a random cat image if available; None if no response is received.
        """
        response = await self._make_request(self.base_urls["cat"])
        return response[0]["url"] if response else None

    async def dog(self):
        """
        Fetches a random dog image URL.

        Returns:
            str or None: The URL of a random dog image if available; None if no response is received.
        """
        response = await self._make_request(self.base_urls["dog"])
        return response["url"] if response else None

    async def pypi(self, package_name):
        """
        Retrieves metadata information about a specified Python package from the PyPI API.

        Args:
            package_name (str): The name of the package to search for on PyPI.

        Returns:
            dict or None: A dictionary with relevant package information if found, containing:
                - name (str): Package name.
                - version (str): Latest package version.
                - summary (str): Short description of the package.
                - author (str): Package author.
                - author_email (str): Email of the package author.
                - license (str): License type.
                - home_page (str): URL of the package's homepage.
                - package_url (str): URL of the package on PyPI.
                - requires_python (str): Minimum Python version required.
                - keywords (str): Keywords associated with the package.
                - classifiers (list): List of PyPI classifiers.
                - project_urls (dict): Additional project URLs (e.g., source code, documentation).
            Returns None if the package is not found or there is an error.
        """
        url = f"{self.base_urls['pypi']}/{package_name}/json"
        response = await self._make_request(url)
        if response:
            info = response["info"]
            relevant_info = {
                "name": info["name"],
                "version": info["version"],
                "summary": info["summary"],
                "author": info["author"],
                "author_email": info["author_email"],
                "license": info["license"],
                "home_page": info["home_page"],
                "package_url": info["package_url"],
                "requires_python": info["requires_python"],
                "keywords": info["keywords"],
                "classifiers": info["classifiers"],
                "project_urls": info["project_urls"],
            }
            return relevant_info
        else:
            return None

    async def meme(self):
        """
        Fetches a random meme image URL.

        Returns:
            str or None: The URL of the meme image if available, otherwise None.
        """
        response = await self._make_request(self.base_urls["meme"])
        return response["preview"][-1] if response else None

    async def fox(self):
        """
        Fetches a random fox image URL.

        Returns:
            str or None: The URL of the fox image if available, otherwise None.
        """
        response = await self._make_request(self.base_urls["fox"])
        return response["link"] if response else None

    async def bing_image(self, query: str, limit: int = 3):
        """
        Searches Bing for images based on a query and retrieves image URLs.

        Args:
            query (str): The search query string for finding images.
            limit (int, optional): The maximum number of image URLs to return. Defaults to 3.

        Returns:
            list: A list of image URLs retrieved from the Bing search results.
        """
        data = {
            "q": query,
            "first": 0,
            "count": limit,
            "adlt": "off",
            "qft": "",
        }
        response = await self._make_request(self.base_urls["bing_image"], params=data)
        return re.findall(r"murl&quot;:&quot;(.*?)&quot;", response) if response else []

    async def stackoverflow_search(self, query, max_results=3, sort_type="relevance"):
        """
        Searches Stack Overflow for questions based on a query, returning results sorted by relevance or another specified criteria.

        Args:
            query (str): The search query string.
            max_results (int, optional): The maximum number of results to return. Defaults to 3.
            sort_type (str, optional): The sorting criteria for the results, such as "relevance" or "votes". Defaults to "relevance".

        Returns:
            list: A list of search results in JSON format, with each entry containing Stack Overflow question details.

        Raises:
            ValueError: If there is an issue with the request to the Stack Overflow API.
        """

        url = "https://api.stackexchange.com/2.3/search/advanced"
        params = {
            "order": "desc",
            "sort": sort_type,
            "q": query,
            "site": "stackoverflow",
            "page": 1,
        }

        all_results = []
        while len(all_results) < max_results:
            response = requests.get(url, params=params)

            if response.status_code != 200:
                raise ValueError("Failed to retrieve results from Stack Overflow API")

            results = response.json().get("items", [])
            if not results:
                break

            all_results.extend(results)
            if len(results) < 30:
                break

            params["page"] += 1

        return all_results[:max_results]

    async def blackpink(self, query, color="#ff94e0", border_color=None):
        """
        Creates a stylized "Blackpink"-themed image with custom text, color, and optional border.

        Args:
            query (str): The text to display on the image.
            color (str, optional): The primary color of the text and gradient background in hex format.
                Defaults to "#ff94e0" (a pink shade).
            border_color (str, optional): The color of the image border in hex format.
                If not provided, defaults to the value of `color`.

        Returns:
            FilePath: The file path of the generated image with delete attribute.
        """
        text = query
        font_path = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
        initial_font_size = 100

        img_width = 800
        img_height = 600

        dummy_img = Image.new("RGB", (1, 1))
        draw_dummy = ImageDraw.Draw(dummy_img)

        font_size = initial_font_size
        padding = 50
        max_width = img_width - 2 * padding
        max_height = img_height - 2 * padding

        font = ImageFont.truetype(font_path, font_size)
        lines = textwrap.wrap(text, width=40)

        while True:
            text_height = sum(draw_dummy.textsize(line, font=font)[1] for line in lines)
            if text_height <= max_height and all(
                draw_dummy.textsize(line, font=font)[0] <= max_width for line in lines
            ):
                break
            font_size -= 1
            font = ImageFont.truetype(font_path, font_size)
            lines = textwrap.wrap(text, width=40)

        gradient = Image.new("RGB", (img_width, img_height), color)
        for i in range(img_height):
            r = int(255 - (255 - int(color[1:3], 16)) * (i / img_height))
            g = int(148 - (148 - int(color[3:5], 16)) * (i / img_height))
            b = int(224 - (224 - int(color[5:7], 16)) * (i / img_height))
            ImageDraw.Draw(gradient).line([(0, i), (img_width, i)], fill=(r, g, b))

        img = Image.new("RGB", (img_width, img_height), (0, 0, 0))
        draw = ImageDraw.Draw(img)

        y_text = (img_height - text_height) // 2
        for line in lines:
            line_width, line_height = draw.textsize(line, font=font)
            draw.text(
                ((img_width - line_width) // 2, y_text),
                line,
                fill=color,
                font=font,
                align="center",
            )
            y_text += line_height

        border_color = border_color or color
        border_width = 28
        img_with_border = ImageOps.expand(img, border=border_width, fill=border_color)

        final_img = Image.new(
            "RGB", (img_with_border.width, img_with_border.height), (0, 0, 0)
        )
        final_img.paste(gradient, (0, 0))
        final_img.paste(img_with_border, (0, 0))

        downloads_folder = "downloads"
        os.makedirs(downloads_folder, exist_ok=True)

        file_path = os.path.join(downloads_folder, f"blackpink_{self._rnd_str()}.jpg")

        final_img.save(file_path, format="JPEG")

        return FilePath(realpath(file_path))

    async def upload_image(self, file_path: Union[str, bytes, BytesIO]) -> str:
        """
        Uploads an image to https://envs.sh.

        Args:
            file_path (Union[str, bytes, BytesIO]): The image file to upload.
                Can be a file path (str), binary data (bytes), or a BytesIO object.

        Returns:
            str: The URL or confirmation message of the uploaded image if the upload is successful.
                Returns "Unexpected response format" if the response format is not as expected.

        Raises:
            ValueError: If the file is not found, the input type is invalid,
                or the upload request fails.
        """
        if isinstance(file_path, str):
            try:
                async with aiofiles.open(file_path, "rb") as f:
                    image_bytes = await f.read()
            except FileNotFoundError:
                raise ValueError(
                    f"File not found: '{file_path}' - Ensure the file path is correct."
                )
        elif isinstance(file_path, bytes) or isinstance(file_path, BytesIO):
            image_bytes = (
                file_path if isinstance(file_path, bytes) else file_path.getvalue()
            )
        else:
            raise ValueError(
                "Invalid input type - Expected a file path (str), binary data (bytes), or BytesIO object."
            )

        url = self.base_urls["upload"]
        files = {"file": image_bytes}

        try:
            response = await self._make_request(url=url, method="POST", files=files)
            return (
                response.strip()
                if isinstance(response, str)
                else "Unexpected response format"
            )
        except ValueError as e:
            raise ValueError(f"Upload failed: {str(e)}")

    @staticmethod
    async def riddle() -> dict:
        """
        Fetches a random riddle from the Riddles API.

        Returns:
            dict: The riddle data in JSON format.
        """
        response = requests.get("https://riddles-api.vercel.app/random")
        if response.status_code == 200:
            return response.json()
        else:
            return {"error": "Could not fetch riddle"}

    async def hug(self, amount: int = 1) -> list:
        """Fetches a specified number hug gif from the Nekos.Best API.

        Args:
            amount (int): The number of neko images to fetch. Defaults to 1.

        Returns:
            list: A list of dictionaries containing information about each fetched neko image or GIF.
                  Each dictionary typically includes:
                  - anime_name (str): The name of the anime.
                  - url (str): The URL of the GIF.
        """
        response = await self._make_request(self.base_urls["neko_hug"].format(amount))
        return response["results"]

    async def neko(self, endpoint: str = "neko", amount: int = 3) -> dict:
        """Fetches a specified number of neko images or GIFs from the Nekos.Best API.

        Args:
            endpoint (str): The endpoint category to fetch content from. Default is "neko".
                Valid image endpoints:
                - "husbando", "kitsune", "neko", "waifu"
                Valid GIF endpoints:
                - "baka", "bite", "blush", "bored", "cry", "cuddle", "dance", "facepalm",
                  "feed", "handhold", "handshake", "happy", "highfive", "hug", "kick",
                  "kiss", "laugh", "lurk", "nod", "nom", "nope", "pat", "peck", "poke",
                  "pout", "punch", "shoot", "shrug", "slap", "sleep", "smile", "smug",
                  "stare", "think", "thumbsup", "tickle", "wave", "wink", "yawn", "yeet"
            amount (int): The number of items to fetch. Default is 3.

        Returns:
            dict: A dictionary containing the results of the request. The dictionary has a key `"results"`,
                  which holds a list of items.

        Raises:
            ValueError: If the endpoint is not a valid category.
        """
        valid_categories = [
            "husbando",
            "kitsune",
            "neko",
            "waifu",  # Images
            "baka",
            "bite",
            "blush",
            "bored",
            "cry",
            "cuddle",
            "dance",
            "facepalm",
            "feed",
            "handhold",
            "handshake",
            "happy",
            "highfive",
            "hug",
            "kick",
            "kiss",
            "laugh",
            "lurk",
            "nod",
            "nom",
            "nope",
            "pat",
            "peck",
            "poke",
            "pout",
            "punch",
            "shoot",
            "shrug",
            "slap",
            "sleep",
            "smile",
            "smug",
            "stare",
            "think",
            "thumbsup",
            "tickle",
            "wave",
            "wink",
            "yawn",
            "yeet",  # GIFs
        ]

        if endpoint not in valid_categories:
            raise ValueError(
                f"Invalid endpoint '{endpoint}'. Must be one of: {', '.join(valid_categories)}"
            )

        url = self.base_urls["neko_url"].format(endpoint=endpoint, amount=amount)

        response = await self._make_request(url)

        return response

    async def domain_search(self, domain: str, zone: str = "com") -> dict:
        """Fetches domain information from the DomainsDB API.

        Args:
            domain (str): The domain name to search for (e.g., "facebook").
            zone (str): The domain zone to search within (e.g., "com").Default is "com".

        Returns:
            dict: A dictionary containing the results of the domain search.
        """
        url = self.base_urls["domain"].format(domain=domain, zone=zone)

        response = await self._make_request(url)

        return response

    async def get_word_definitions(self, word: str) -> List[dict]:
        """
        Fetch definitions for a word from the Dictionary API.

        Args:
            word (str): The word to fetch definitions for.

        Returns:
            list: A list of dictionaries containing the word definitions.

        Raises:
            ValueError: If the `word` is not provided or the API request fails.
        """
        url = self.base_urls["word_info"].format(word=word)
        response = await self._make_request(url)
        return response


api = TheApi()
