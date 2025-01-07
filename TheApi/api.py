import os
import re
import random
import string
import textwrap
from io import BytesIO
from typing import List, Union, Optional

import aiofiles
from bs4 import BeautifulSoup
from PIL import Image, ImageOps, ImageDraw, ImageFont

from ._request import Request


class Client:
    """
    A class to interact with various APIs and perform operations like fetching data and generating files.

    Args:
        downloads_dir (``str``, *optional*): Directory to save downloaded files. Defaults to "downloads".
        quiet (``bool``, *optional*): Whether to suppress error messages. Defaults to False.
    """

    def __init__(self, downloads_dir: str = "downloads", quiet: bool = False):

        self.base_urls = {
            "advice": "https://api.adviceslip.com/advice",
            "animechan": "https://animechan.io/api/v1/quotes/random",
            "avatar": "https://thedobby.club/api/avatars/random/",
            "btc_value": "https://api.stakdek.de/api/btc/",
            "bing_image": "https://www.bing.com/images/async",
            "carbon": "https://carbonara.solopov.dev/api/cook",
            "cat": "https://api.thecatapi.com/v1/images/search",
            "dog": "https://random.dog/woof.json",
            "domain": "https://api.domainsdb.info/v1/domains/search?domain={domain}&zone={zone}",
            "faker": "https://fakerapi.it/api/v2/",
            "fox": "https://randomfox.ca/floof/",
            "font": "https://github.com/google/fonts/raw/main/ofl/poetsenone/PoetsenOne-Regular.ttf",
            "hindi_jokes": "https://hindi-jokes-api.onrender.com/jokes?api_key=93eeccc9d663115eba73839b3cd9",
            "hindi_quote": "https://hindi-quotes.vercel.app/random",
            "image": "https://graph.org/file/1f8d00177ac2429b101b9.jpg",
            "jokes": "https://v2.jokeapi.dev/joke/Any",
            "meme": "https://meme-api.com/gimme",
            "neko_url": "https://nekos.best/api/v2/{endpoint}?amount={amount}",
            "neko_hug": "https://nekos.best/api/v2/hug?amount={}",
            "pdf": "https://api.stakdek.de/api",
            "pypi": "https://pypi.org/pypi",
            "qr_gen": "https://api.qrserver.com/v1",
            "quote": "https://api.quotable.io/random",
            "riddle": "https://riddles-api.vercel.app/random",
            "useless_fact": "https://uselessfacts.jsph.pl/api/v2/facts/random",
            "wikipedia_search": "https://en.wikipedia.org/w/api.php",
            "words": "https://random-word-api.vercel.app/api",
            "word_info": "https://api.dictionaryapi.dev/api/v2/entries/en/{word}",
            "upload": "https://envs.sh/",
        }
        self.request = Request()
        self.downloads_dir = downloads_dir
        self.quiet = quiet

        os.makedirs(self.downloads_dir, exist_ok=True)

    def _handle_error(self, error: Exception) -> Union[dict, Exception]:
        if self.quiet:
            return {"error": True, "message": str(error)}
        raise error

    async def _create_file(
        self, contents: bytes, ext: str, name: Optional[str] = None
    ) -> str:
        file_name = f"{name or 'file'}_{self._rnd_str()}.{ext}"
        file_path = os.path.join(self.downloads_dir, file_name)

        async with aiofiles.open(file_path, "wb") as f:
            await f.write(contents)

        return file_path

    def _rnd_str(self) -> str:
        random_str = "".join(random.choices(string.ascii_letters + string.digits, k=8))
        return random_str

    async def avatar(self):
        """
        Fetches a random avatar from the thedobby.club API.

        Returns:
            ``dict``: A dictionary containing the file name, file type, and file URL.
        Example:
            .. code-block:: python

               results = await api.avatar()
        """

        response = await self.request.get(self.base_urls["avatar"])

        return response.json()

    async def animechan(self):
        """
        Fetches a random anime quote from the AnimeChan API.

        Returns:
            ``dict``: Contains the quote content, anime name, and character details.
        """
        response = await self.request.get(self.base_urls["animechan"])
        return response.json()["data"]

    async def carbon(
        self,
        code,
        background_color="rgba(171, 184, 195, 1)",
        drop_shadow=True,
        drop_shadow_blur_radius="68px",
        drop_shadow_offset_y="20px",
        export_size="2x",
        font_custom="",
        font_size="14px",
        font_family="Hack",
        first_line_number=1,
        language="auto",
        line_height="133%",
        line_numbers=False,
        padding_horizontal="56px",
        padding_vertical="56px",
        prettify=False,
        selected_lines="",
        theme="seti",
        watermark=False,
        width=536,
        width_adjustment=True,
        window_controls=True,
        window_theme="none",
    ):
        """
        Generate an image of a code snippet using the `Carbonara API <https://github.com/petersolopov/carbonara>`_.


        Args:
            code (``str``): **Required.** The code snippet to generate an image for.
            background_color (``str``, *optional*): Background color of the image. Can be in ``rgba`` or ``hex`` format. Default is ``"rgba(171, 184, 195, 1)"``.
            drop_shadow (``bool``, *optional*): Whether to enable the shadow effect. Default is ``True``.
            drop_shadow_blur_radius (``str``, *optional*): The blur radius of the shadow. Default is ``"68px"``.
            drop_shadow_offset_y (``str``, *optional*): The vertical offset of the shadow. Default is ``"20px"``.
            export_size (``str``, *optional*): Resolution of the exported image, such as ``"1x"``, ``"2x"``, or ``"3x"``. Default is ``"2x"``.
            font_custom (``str``, *optional*): Custom font in Base64 format. Leave empty for default fonts. Default is an empty string.
            font_size (``str``, *optional*): The size of the font in the code snippet. Default is ``"14px"``.
            font_family (``str``, *optional*): Font family for the code snippet. Examples: ``"Hack"``, ``"JetBrains Mono"``, ``"Fira Code"``. Default is ``"Hack"``.
            first_line_number (``int``, *optional*): The line number to start with in the snippet. Default is ``1``.
            language (``str``, *optional*): Programming language for syntax highlighting. Default is ``"auto"``. Example: Use ``"python"``, ``"javascript"``, or ``"application/x-sh"`` for bash.
            line_height (``str``, *optional*): Line height for the text in the snippet. Default is ``"133%"``.
            line_numbers (``bool``, *optional*): Whether to display line numbers in the snippet. Default is ``False``.
            padding_horizontal (``str``, *optional*): Horizontal padding around the code block. Default is ``"56px"``.
            padding_vertical (``str``, *optional*): Vertical padding around the code block. Default is ``"56px"``.
            prettify (``bool``, *optional*): Automatically format JavaScript code using Prettier. Default is ``False``.
            selected_lines (``str``, *optional*): Specific lines to highlight, as a comma-separated string. Example: ``"3,4,6"``. Default is an empty string.
            theme (``str``, *optional*): The theme for the code snippet. Examples: ``"seti"``, ``"dracula"``. Default is ``"seti"``.
            watermark (``bool``, *optional*): Whether to include the Carbon watermark. Default is ``False``.
            width (``int``, *optional*): Width of the image in pixels. Default is ``536``.
            width_adjustment (``bool``, *optional*): Automatically adjusts width based on content. Default is ``True``.
            window_controls (``bool``, *optional*): Show or hide window controls (close, minimize, maximize buttons). Default is ``True``.
            window_theme (``str``, *optional*): Style of the window controls. Options: ``"none"``, ``"sharp"``, ``"bw"``, ``"boxy"``. Default is ``"none"``.

        Returns:
            A dictionary containing either the file path to the generated image or an error message.
            If successful, the dictionary will contain **"success": True** and **"result"**: the file path where the generated image is saved.
            If failed, the dictionary will contain **"success": False** and **"error"**: a string describing the error that occurred.

        Example:
            .. code-block:: python

                code_snippet = "print('Hello, World!')"

                response = await api.carbon(
                    code_snippet,
                    theme="dracula",
                    language="python"
                )

                if response['success']:

                    print(f"Code image saved as '{response['result']}'.")

                else:

                    print(f"Error: {response['error']}")
        """

        payload = {
            "code": code,
            "backgroundColor": background_color,
            "dropShadow": drop_shadow,
            "dropShadowBlurRadius": drop_shadow_blur_radius,
            "dropShadowOffsetY": drop_shadow_offset_y,
            "exportSize": export_size,
            "fontCustom": font_custom,
            "fontSize": font_size,
            "fontFamily": font_family,
            "firstLineNumber": first_line_number,
            "language": language,
            "lineHeight": line_height,
            "lineNumbers": line_numbers,
            "paddingHorizontal": padding_horizontal,
            "paddingVertical": padding_vertical,
            "prettify": prettify,
            "selectedLines": selected_lines,
            "theme": theme,
            "watermark": watermark,
            "width": width,
            "widthAdjustment": width_adjustment,
            "windowControls": window_controls,
            "windowTheme": window_theme,
        }
        try:
            response = await self.request.post(self.base_urls["carbon"], json=payload)
            response.raise_for_status()
            file_path = await self._create_file(
                response.content, ext="png", name="carbon"
            )

            return {"success": True, "result": file_path}
        except Exception as e:
            return {"success": False, "error": str(e)}

    async def fakerapi(
        self,
        endpoint: str,
        quantity: int = 3,
        locale: str = "en_US",
        seed: int = None,
        **kwargs,
    ):
        """
        Fetch data from the FakerAPI

        Args:
            endpoint (``str``):
                The resource endpoint. Valid endpoints are:
                *companies*, *addresses*, *books*, *CreditCards*, *images*,
                *persons*, *places*, *products*, *texts*.
            quantity (``int``, *optional*):
                Number of rows to fetch (default: 3, max: 1000).
            locale (``str``, *optional*):
                Locale for the data (default: 'en_US').
                `See valid locales <https://fakerapi.it/#params_locale>`_
            seed (``int``, *optional*):
                This parameter accept an integer and allows to get always the same results. So, executing the same request with seed parameter set to the same value (ex. 12345) the results will never change (Defaults to ``None``).
            **kwargs (``dict``, *optional*):
                Additional parameters passed to the API request. These can include any other valid query parameters accepted by the `FakerAPI <https://fakerapi.it/>`_ .

        Returns:
            ``dict``:
                Response data from the API.
        """

        valid_endpoints = [
            "companies",
            "addresses",
            "books",
            "CreditCards",
            "images",
            "persons",
            "places",
            "products",
            "texts",
            "users",
        ]
        valid_locales = [
            "ar_EG",
            "ar_JO",
            "ar_SA",
            "at_AT",
            "bg_BG",
            "bn_BD",
            "cs_CZ",
            "da_DK",
            "de_AT",
            "de_CH",
            "de_DE",
            "el_CY",
            "el_GR",
            "en_AU",
            "en_CA",
            "en_GB",
            "en_HK",
            "en_IN",
            "en_NG",
            "en_NZ",
            "en_PH",
            "en_SG",
            "en_UG",
            "en_US",
            "en_ZA",
            "es_AR",
            "es_ES",
            "es_PE",
            "es_VE",
            "et_EE",
            "fa_IR",
            "fi_FI",
            "fr_BE",
            "fr_CA",
            "fr_CH",
            "fr_FR",
            "he_IL",
            "hr_HR",
            "hu_HU",
            "hy_AM",
            "id_ID",
            "is_IS",
            "it_CH",
            "it_IT",
            "ja_JP",
            "ka_GE",
            "kk_KZ",
            "ko_KR",
            "lt_LT",
            "lv_LV",
            "me_ME",
            "mn_MN",
            "ms_MY",
            "nb_NO",
            "ne_NP",
            "nl_BE",
            "nl_NL",
            "pl_PL",
            "pt_BR",
            "pt_PT",
            "ro_MD",
            "ro_RO",
            "ru_RU",
            "sk_SK",
            "sl_SI",
            "sr_Cyrl_RS",
            "sr_Latn_RS",
            "sr_RS",
            "sv_SE",
            "th_TH",
            "tr_TR",
            "uk_UA",
            "vi_VN",
            "zh_CN",
            "zh_TW",
        ]

        if locale not in valid_locales:
            return self._handle_error(
                ValueError(
                    f"Invalid locale '{locale}'. Must be one of {' '.join(valid_locales)}"
                )
            )
        if endpoint not in valid_endpoints:
            return self._handle_error(
                ValueError(
                    f"Invalid endpoint '{endpoint}'. Must be one of {' '.join(valid_endpoints)}"
                )
            )
        if quantity < 1 or quantity > 1000:
            return self._handle_error(ValueError("Quantity must be between 1 and 1000"))

        params = {
            "_quantity": quantity,
            "_locale": locale,
            **kwargs,
        }
        if seed:
            params["_seed"] = seed
        url = f"{self.base_urls['faker']}{endpoint}"

        result = await self.request.get(url, params=params)
        return result.json()

    async def get_fake_images(
        self,
        quantity: int = 1,
        locale: str = "en_US",
        type: str = "any",
        width: int = 640,
        height: int = 480,
        seed: int = None,
    ):
        """
        Fetch fake image data from the `FakerAPI <https://fakerapi.it/>`_ .

        Args:
            quantity (``int``, *optional*): Number of images to fetch. Defaults to 1.

            locale (``str``, *optional*): Locale for the images. Defaults to "en_US".
                `See Valid locale <https://fakerapi.it/#params_locale>`_

            type (``st``r, *optional*): Type of image (e.g., 'any', 'animals', 'business', etc.).
                Defaults to "any".

            width (``int``, *optional*): Width of the images. Defaults to 640.

            height (``int``, *optional*): Height of the images. Defaults to 480.

            seed (``int``, *optional*): This parameter accept an integer and allows to get always the same results. So, executing the same request with seed parameter set to the same value (ex. 12345) the results will never change (Defaults to ``None``).


        Returns:
            ``dict``: Response data from the API.
        """

        return await self.fakerapi(
            "images",
            quantity=quantity,
            locale=locale,
            seed=seed,
            _type=type,
            _width=width,
            _height=height,
        )

    async def get_fake_credit_cards(
        self, locale: str = "en_US", quantity: int = 7, seed: int = None
    ):
        """
        Fetch fake credit card data from the `FakerAPI <https://fakerapi.it/>`_ .

        Args:
            locale (``str``, *optional*): Locale for the credit card data (default: "en_US"), `See Valid locale <https://fakerapi.it/#params_locale>`_.
            amount (``int``, *optional*): Number of credit card entries to fetch (default: 7).
            seed (``int``, *optional*): This parameter accept an integer and allows to get always the same results. So, executing the same request with seed parameter set to the same value (ex. 12345) the results will never change (Defaults to ``None``).

        Returns:
            ``dict``: Response data from the API.
        """
        return await self.fakerapi(
            "CreditCards", quantity=quantity, locale=locale, seed=seed
        )

    async def get_fake_addresses(
        self,
        quantity: int = 7,
        locale: str = "en_US",
        country_code: str = None,
        seed: int = None,
    ):
        """
        Fetch fake address data from the `FakerAPI <https://fakerapi.it/>`_ .

        Args:
            quantity (``int``, *optional*): Number of address entries to fetch (default: 7).
            locale (``str``, *optional*): Locale for the address data (default: "en_US"), `See Valid locale <https://fakerapi.it/#params_locale>`_.
            country_code (``str``, *optional*): force the country of response's adresses. ISO 3166-1 Two-letter format or locale format like en_US (default: ``None``).
            seed (``int``, *optional*): This parameter accept an integer and allows to get always the same results. So, executing the same request with seed parameter set to the same value (ex. 12345) the results will never change (Defaults to ``None``).


        Returns:
            ``dict``: Response data from the API.
        """
        kwargs = {}
        if country_code:
            kwargs["_country_code"] = country_code
        return await self.fakerapi(
            "addresses", quantity=quantity, locale=locale, seed=seed**kwargs
        )

    async def get_fake_persons(
        self,
        quantity: int = 7,
        locale: str = "en_US",
        gender: str = None,
        birthday_start: str = None,
        birthday_end: str = None,
        seed: int = None,
    ):
        """
        Fetch fake persons details from the `FakerAPI <https://fakerapi.it/>`_ .

        Args:
            quantity (``int``, *optional*): Number of address entries to fetch (default: 7).
            locale (``str``, *optional*): Locale for the address data (default: "en_US"), `See Valid locale <https://fakerapi.it/#params_locale>`_.
            gender (``str``, *optional*): Gender of the person can be ``male`` or ``female``.
            birthday_start (``str``, *optional*): Birthday starting date of person in format Y-m-d (default: FakerApi Keeps *90 years*)
            birthday_end (``str``, *optional*): Birthday ending date of person  in format Y-m-d (default: FakerApi keeps *now*)
            seed (``int``, *optional*): This parameter accept an integer and allows to get always the same results. So, executing the same request with seed parameter set to the same value (ex. 12345) the results will never change (Defaults to ``None``).

        Returns:
            ``dict``: Response data from the API.
        """
        kwargs = {}
        if birthday_start:
            kwargs["_birthday_start"] = birthday_start
        if birthday_end:
            kwargs["_birthday_end"] = birthday_end
        if gender:
            kwargs["_gender"] = gender
        return await self.fakerapi(
            "persons", quantity=quantity, locale=locale, seed=seed, **kwargs
        )

    async def get_advice(self):
        """
        Fetches a random piece of advice.

        Returns:
            ``str``: A random advice message.
        """
        response = await self.request.get(self.base_urls["advice"])
        return response.json()["slip"]["advice"]

    async def get_btc_value(self, currency: Optional[str] = None) -> dict:
        """
        Fetches the current value of Bitcoin (BTC) for the specified currency or all currencies.

        Args:
            currency (``str``, *optional*): The currency code (e.g., 'eur', 'usd', 'gbp').
                                      If None, fetches BTC value for all currencies.

        Returns:
            ``dict``: The response containing BTC value(s) for the specified currency or all currencies.

        Raises:
            ValueError: If the provided currency is invalid or the request fails.
        """
        valid_currencies = {"eur", "usd", "gbp"}
        url = (
            f"{self.base_urls['btc_value']}/get_btc_value"
            if not currency
            else f"{self.base_urls['btc_value']}/get_btc_{currency.lower()}"
        )

        if currency and currency.lower() not in valid_currencies:
            return self._handle_error(
                ValueError(
                    f"Invalid currency provided: {currency}. Valid options are: {valid_currencies}"
                )
            )

        response = await self.request.get(url)

        return response.json()

    async def get_jokes(self, amount=1):
        """
        Fetches a specified number of jokes.

        Args:
            amount (``int``, *optional*): The number of jokes to retrieve. Defaults to 1.

        Returns:
            ``str``: A single joke if `amount` is 1.
            ``list``: If `amount` > 1, returns numbered jokes.
        """
        url = self.base_urls["jokes"]
        params = {"type": "single", "amount": amount}
        response = await self.request.get(url, params=params)
        result = response.json()
        if amount == 1:
            return result["joke"]
        else:
            jokes = [joke["joke"] for joke in result["jokes"]]
            return jokes

    async def get_hindi_jokes(self):
        """
        Fetches a random Hindi joke.

        Returns:
            ``str``: A random Hindi joke if available, or "No joke found" if not available.
        """
        response = await self.request.get(self.base_urls["hindi_jokes"])
        response = response.json()
        return response["jokeContent"] if response["status"] else "No joke found."

    async def generate_pdf(
        self,
        source: str,
        from_url: bool = True,
    ) -> str:
        """
        Generates a PDF from a URL or an HTML string and saves it to a file.

        Args:
            source (``str``): The URL of the website (if `from_url=True`) or the HTML string (if `from_url=False`).
            from_url (``bool``, *optional"): Whether to generate the PDF from a URL (True) or an HTML string (False).

        Returns:
            ``str``: The file path where the PDF was saved.

        Raises:
            ValueError: If `from_url` is True and `source` is not a valid URL.
        """
        if from_url:
            # Validate the URL format using regex
            url_regex = re.compile(
                r"^(https?://)?"  # http or https
                r"(([A-Za-z0-9-]+\.)+[A-Za-z]{2,6})"  # Domain
                r"(:[0-9]{1,5})?"  # Optional port
                r"(/[A-Za-z0-9._%+-]*)*$",  # Path
                re.IGNORECASE,
            )
            if not re.match(url_regex, source):
                return self._handle_error(ValueError(f"Invalid URL provided: {source}"))
        url = self.base_urls["pdf"]
        url = url + "/from_url" if from_url else url + "/from_html"
        params = {"url": source} if from_url else {"html": source}

        response = await self.request.get(url, params=params)
        pdf_content = response.read()
        file_path = await self._create_file(pdf_content, ext="pdf", name="pdf")

        return file_path

    async def gen_qr(
        self,
        data: str,
        size: str = "150x150",
        foreground_color: str = "000000",
        background_color: str = "FFFFFF",
    ) -> str:
        """
        Generate a QR code using api.qrserver.com and save it as a PNG file.

        Args:
            data (``str``): The content for the QR code.
            size (``str``, *optional*): The size of the QR code in the format 'WIDTHxHEIGHT' (default: '150x150').
            foreground_color (``str``, *optional*): The color of the QR code (default: '000000' - black).
            background_color (``str``, *optional*): The background color of the QR code (default: 'FFFFFF' - white).

        Returns:
            str: The file path where the QR code was saved.
        """

        url = f"{self.base_urls['qr_gen']}/create-qr-code/"
        params = {
            "size": size,
            "data": data,
            "color": foreground_color,
            "bgcolor": background_color,
        }
        response = await self.request.get(url=url, params=params)
        file_path = await self._create_file(response.content, ext="png", name="QrCode")

        return file_path

    async def get_uselessfact(self):
        """
        Fetches a random useless fact.

        Returns:
            ``str``: A random useless fact.
        """
        response = await self.request.get(self.base_urls["useless_fact"])
        response = response.json()
        return response["text"]

    async def google_search(
        self,
        query: str,
        limit: int = 10,
        lang: str = "en",
        timeout: int = 5,
        adlt: str = "active",
        region: str = None,
    ) -> dict:
        """
         Perform an asynchronous search on Google and return a list of results.

         This method sends an HTTP request to Google with the specified query and retrieves the search results.
         The results are then returned in a dictionary format containing the URLs, titles, and descriptions.

         Args:
             query (str): The search query (e.g., "Python programming").
             limit (int, optional): The maximum number of results to return. Defaults to 10.
             lang (str, optional): The language for the search results. Defaults to "en".
             timeout (int, optional): The time to wait for a response in seconds. Defaults to 5.
             adlt (str, optional): The safe search setting. Can be "active" or "off". Defaults to "active".
             region (str, optional): The region to filter search results. Defaults to None.


        Returns:
             dict: A dictionary containing the success status and either the result or an error message.
                 If successful, the dictionary will contain **"success": True** and **"result"**: the file path where the generated image is saved.
                 If failed, the dictionary will contain **"success": False** and **"error"**: a string describing the error that occurred.

        """
        _useragent_list = [
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0",
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36",
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36",
            "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36",
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36 Edg/111.0.1661.62",
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/111.0",
        ]
        start, fetched_results, fetched_links = 0, 0, set()
        all_results = []

        while fetched_results < limit:
            params = {
                "q": query,
                "num": limit + 2,
                "hl": lang,
                "start": start,
                "safe": adlt,
                "gl": region,
            }
            headers = {"User-Agent": random.choice(_useragent_list)}

            try:
                resp = await self.request.get(
                    "https://www.google.com/search",
                    params=params,
                    headers=headers,
                    timeout=timeout,
                )
                resp.raise_for_status()
            except Exception as e:
                return {"success": False, "error": str(e)}
            soup = BeautifulSoup(resp.text, "html.parser")

            for result in soup.find_all("div", class_="g"):
                link_tag, title_tag = result.find("a", href=True), result.find("h3")
                description_box = result.find("div", {"style": "-webkit-line-clamp:2"})
                if not (link_tag and title_tag and description_box):
                    continue

                link = link_tag["href"]
                if link in fetched_links:
                    continue
                fetched_links.add(link)

                fetched_results += 1
                all_results.append(
                    {"url": link, "title": title_tag.text, "desc": description_box.text}
                )

                if fetched_results >= limit:
                    return {"success": True, "result": all_results}

            if not soup.find_all("div", class_="g"):
                break

            start += 10

        return {"success": True, "result": all_results}

    async def quote(self) -> str:
        """
        Fetches a random quote.

        Returns:
            ``str``: The content of a random quote followed by the author's name.
        """
        response = await self.request.get(self.base_urls["quote"], verify=False)
        data = response.json()
        return f"{data['content']}\n\nauthor - {data['author']}"

    async def hindi_quote(self) -> str:
        """
        Fetches a random Hindi quote.

        Returns:
            ``str``: The content of a random Hindi quote.
        """
        response = await self.request.get(self.base_urls["hindi_quote"])
        response = response.json()
        return response["quote"]

    async def write(self, text):
        """
        Creates an image with text written on it, using a predefined template and font,
        and uploads the image after generation.

        Args:
            text (``str``): The text to be written on the image. Text exceeding 55 characters
                        per line will be wrapped, with up to 25 lines displayed.

        Returns:
            ``str``: The URL of the uploaded image.

        """
        tryimg = "https://graph.org/file/1f8d00177ac2429b101b9.jpg"
        tryresp = await self.request.get(tryimg)
        img = Image.open(BytesIO(tryresp.content))
        draw = ImageDraw.Draw(img)

        font_url = "https://github.com/google/fonts/raw/main/ofl/poetsenone/PoetsenOne-Regular.ttf"
        font_response = await self.request.get(font_url)
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

        file_path = os.path.join(self.downloads_dir, f"write_{self._rnd_str()}.jpg")

        img.save(file_path)

        return file_path

    async def wikipedia(self, query):
        """
        Searches Wikipedia for a given query and retrieves the top result's summary, URL, and image.

        Args:
            query (``str``): The search term to look up on Wikipedia.

        Returns:
            ``dict``: A dictionary containing information about the top search result, with keys:
                **"title"** (**str**): The title of the Wikipedia article.
                **"summary"** (**str**): A brief summary of the article's content.
                **"url"** (**str**): The URL link to the full Wikipedia article.
                **"image_url"** (**str**): The URL of the article's thumbnail image, or **"No image available"** if none exists.

            If no results are found, returns a dictionary with an **"error"** key.
        """

        search_url = self.base_urls["wikipedia_search"]

        params = {
            "action": "query",
            "list": "search",
            "srsearch": query,
            "format": "json",
        }

        search_response = await self.request.get(search_url, params=params)
        search_response = search_response.json()
        search_results = search_response.get("query", {}).get("search", [])

        if search_results:
            top_result = search_results[0]
            page_id = top_result["pageid"]
            summary_url = (
                f"{self.base_urls['wikipedia_search']}?action=query&prop=extracts|pageimages"
                f"&exintro&explaintext&piprop=thumbnail&pithumbsize=500&format=json&pageids={page_id}"
            )

            summary_response = await self.request.get(summary_url)
            summary_response = summary_response.json()
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
            return self._handle_error(ValueError("No search results found"))

    async def github_search(self, query, search_type="repositories", max_results=3):
        """
        Searches GitHub for various types of content.

        Args:
            query (``str``): The search query.
            search_type (``str``, *optional*): The type of search. Can be one of:
                - "repositories"
                - "users"
                - "organizations"
                - "issues"
                - "pull_requests"
                - "commits"
                - "topics"

                Defaults to "repositories".
            max_results (``int``, *optional*): The maximum number of results to return. Defaults to 3.

        Returns:
            ``list``: A list of search results or an error message.
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
            response = await self.request.get(url, headers=headers, params=params)
            response = response.json()
            items = response.get("items", [])

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

        except Exception as e:
            return self._handle_error(ValueError(f"Unexpected error: {e}"))

    async def get_words(
        self, words=10, letter=None, word_type="capitalized", alphabetize=False
    ):
        """
        Fetch random words from the Random Word API.

        Args:
            words (``int``): Number of words to generate (default is 10).
            letter (``str``): First letter of the words (optional).
            word_type (``str``): Type of words (lowercase, uppercase, capitalized; default is capitalized).
            alphabetize (``bool``): Whether to alphabetize the result (default is False).

        Returns:
            ``list``: A list of random words or an error message.
        """
        params = {
            "words": words,
            "type": word_type,
            "alphabetize": str(alphabetize).lower(),
        }
        if letter:
            params["letter"] = letter

        response = await self.request.get(self.base_urls["words"], params=params)
        return response.json()

    async def cat(self):
        """
        Fetches a random cat image URL.

        Returns:
            ``str`` or ``None``: The URL of a random cat image if available; None if no response is received.
        """
        response = await self.request.get(self.base_urls["cat"])
        response = response.json()
        return response[0]["url"] if response else None

    async def dog(self):
        """
        Fetches a random dog image URL.

        Returns:
            ``str`` or None: The URL of a random dog image if available; None if no response is received.
        """
        response = await self.request.get(self.base_urls["dog"])
        response = response.json()
        return response["url"] if response else None

    async def pypi(self, package_name):
        """
        Retrieves metadata information about a specified Python package from the PyPI API.

        Args:
            package_name (``str``): The name of the package to search for on PyPI.

        Returns:
            ``dict`` or ``None``: A dictionary with relevant package information if found.
            Returns None if the package is not found or there is an error.
        """
        url = f"{self.base_urls['pypi']}/{package_name}/json"
        response = await self.request.get(url)
        response = response.json()
        if response:
            return response
        else:
            return None

    async def meme(self):
        """
        Fetches a random meme image URL.

        Returns:
            ``str`` or ``None``: The URL of the meme image if available, otherwise None.
        """
        response = await self.request.get(self.base_urls["meme"])
        response = response.json()
        return response["preview"][-1] if response else None

    async def fox(self):
        """
        Fetches a random fox image URL.

        Returns:
            ``str`` : The URL of the fox image if available.
        """
        response = await self.request.get(self.base_urls["fox"])
        response = response.json()
        return response["link"]

    async def bing_image(self, query: str, limit: int = 3, adlt: str = "moderate"):
        """
        Searches Bing for images based on a query and retrieves image URLs.

        Args:
            query (``str``): The search query string for finding images.
            limit (``int``, *optional*): The maximum number of image URLs to return. Defaults to 3.
            adlt (``str``, *optional*): The level of adult content filtering to apply.
                The available options are:
                "off", which disables filtering for adult content.
                "moderate" (default), which filters explicit images but may include related content.
                "strict", which enforces strict filtering, excluding all adult content.

        Returns:
            ``list``: A list of image URLs retrieved from the Bing search results.
        """
        data = {
            "q": query,
            "first": 0,
            "count": limit,
            "adlt": adlt,
            "qft": "",
        }
        response = await self.request.get(self.base_urls["bing_image"], params=data)
        return (
            re.findall(r"murl&quot;:&quot;(.*?)&quot;", response.text)
            if response
            else []
        )

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
            response = await self.request.get(url, params=params)
            response = response.json()
            results = response.get("items", [])
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
            query (``str``):
                The text to display on the image.
            color (``str``, *optional*):
                The primary color of the text and gradient background in hex format.
                Defaults to "#ff94e0" (a pink shade).
            border_color (``str``, *optional*):
                The color of the image border in hex format.
                If not provided, defaults to the value of ``color``.

        Returns:
            ``str``:
                The file path of the generated image.
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
            text_height = sum(
                draw_dummy.textbbox((0, 0), line, font=font)[3]
                - draw_dummy.textbbox((0, 0), line, font=font)[1]
                for line in lines
            )
            if text_height <= max_height and all(
                draw_dummy.textbbox((0, 0), line, font=font)[2] <= max_width
                for line in lines
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
            bbox = draw.textbbox((0, 0), line, font=font)
            line_width = bbox[2] - bbox[0]
            line_height = bbox[3] - bbox[1]
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

        file_path = os.path.join(self.downloads_dir, f"blackpink_{self._rnd_str()}.jpg")

        final_img.save(file_path, format="JPEG")

        return file_path

    async def upload_image(self, file_path: Union[str, bytes, BytesIO]) -> str:
        """
        Uploads an image to https://envs.sh.

        Args:
            file_path (``str``, ``bytes``, ``BytesIO``): The image file to upload.
                Can be a file path (**str**), binary data (**bytes**), or a **BytesIO** object.

        Returns:
            ``str``: The URL or confirmation message of the uploaded image if the upload is successful.
                Returns **"Unexpected response format"** if the response format is not as expected.
        """

        if isinstance(file_path, str):
            try:
                async with aiofiles.open(file_path, "rb") as f:
                    image_bytes = await f.read()
            except FileNotFoundError:
                return self._handle_error(
                    ValueError(
                        f"File not found: '{file_path}' - Ensure the file path is correct."
                    )
                )
        elif isinstance(file_path, bytes) or isinstance(file_path, BytesIO):
            image_bytes = (
                file_path if isinstance(file_path, bytes) else file_path.getvalue()
            )
        else:
            return self._handle_error(
                ValueError(
                    "Invalid input type - Expected a file path (str), binary data (bytes), or BytesIO object."
                )
            )

        url = self.base_urls["upload"]
        files = {"file": image_bytes}

        try:
            response = await self.request.post(url=url, files=files)
            return (
                response.text.strip()
                if isinstance(response, str)
                else "Unexpected response format"
            )
        except ValueError as e:
            return self._handle_error(ValueError(f"Upload failed: {str(e)}"))

    async def riddle(self) -> dict:
        """
        Fetches a random riddle from the Riddles API.

        Returns:
            ``dict``: The riddle data in JSON format.
        """
        response = await self.request.get(self.base_urls["riddle"])
        return response.json()

    async def hug(self, amount: int = 1) -> list:
        """Fetches a specified number hug gif from the Nekos.Best API.

        Args:
            amount (``int``): The number of neko images to fetch. Defaults to 1.

        Returns:
            ``list``: A list of dictionaries containing information about each fetched neko image or GIF.
                      Each dictionary will typically include:
                      **"anime_name"** (str): The name of the anime.
                      **"url"** (str): The URL of the GIF.

        """
        response = await self.request.get(self.base_urls["neko_hug"].format(amount))

        return response.json()["results"]

    async def neko(self, endpoint: str = "neko", amount: int = 3) -> dict:
        """Fetches a specified number of neko images or GIFs from the Nekos.Best API.

        Args:
            endpoint (``str``): The endpoint category to fetch content from. Default is "neko".
                Valid image endpoints:
                **"husbando"**, **"kitsune"**, **"neko"**, **"waifu"**
                Valid GIF endpoints:
                **"baka"**, **"bite"**, **"blush"**, **"bored"**, **"cry"**, **"cuddle"**,
                **"dance"**, **"facepalm"**, **"feed"**, **"handhold"**, **"handshake"**,
                **"happy"**, **"highfive"**, **"hug"**, **"kick"**, **"kiss"**, **"laugh"**,
                **"lurk"**, **"nod"**, **"nom"**, **"nope"**, **"pat"**, **"peck"**, **"poke"**,
                **"pout"**, **"punch"**, **"shoot"**, **"shrug"**, **"slap"**, **"sleep"**,
                **"smile"**, **"smug"**, **"stare"**, **"think"**, **"thumbsup"**, **"tickle"**,
                **"wave"**, **"wink"**, **"yawn"**, **"yeet"**
            amount (``int``): The number of items to fetch. Default is 3.

        Returns:
            ``dict``: A dictionary containing the results of the request. The dictionary has a key
            **"results"**, which holds a list of items.
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
            return self._handle_error(
                ValueError(
                    f"Invalid endpoint '{endpoint}'. Must be one of: {', '.join(valid_categories)}"
                )
            )

        url = self.base_urls["neko_url"].format(endpoint=endpoint, amount=amount)

        response = await self.request.get(url)

        return response.json()

    async def domain_search(self, domain: str, zone: str = "com") -> dict:
        """Fetches domain information from the DomainsDB API.

        Args:
            domain (``str``): The domain name to search for (e.g., "facebook").
            zone (``str``): The domain zone to search within (e.g., "com").Default is "com".

        Returns:
            ``dict``: A dictionary containing the results of the domain search.
        """
        url = self.base_urls["domain"].format(domain=domain, zone=zone)

        response = await self.request.get(url)

        return response.json()

    async def get_word_definitions(self, word: str) -> List[dict]:
        """
        Fetch definitions for a word from the Dictionary API.

        Args:
            word (``str``): The word to fetch definitions for.

        Returns:
            ``list``: A list of dictionaries containing the word definitions.

        """
        url = self.base_urls["word_info"].format(word=word)
        response = await self.request.get(url)
        return response.json()
