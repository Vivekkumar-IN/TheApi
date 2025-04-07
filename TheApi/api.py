import os
import random
import re
import string
import textwrap
from base64 import b64decode
from io import BytesIO
from typing import List, Optional, Union

import aiofiles
from bs4 import BeautifulSoup
from PIL import Image, ImageDraw, ImageFont, ImageOps

from ._request import Request
from ._upload import UploadMedia


class Client(UploadMedia):
    """
    A class to interact with various APIs and perform operations like fetching data and generating files.

    Args:
        downloads_dir (``str``, *optional*): Directory to save downloaded files. Defaults to "downloads".
    """

    def __init__(self, downloads_dir: str = "downloads", quiet: bool = False):
        self.base_urls = {
            "advice": "https://api.adviceslip.com/advice",
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
        }
        self.request = Request()
        self.downloads_dir = downloads_dir
        self.quiet = quiet

        os.makedirs(self.downloads_dir, exist_ok=True)

    def _handle_error(self, error: Exception) -> dict | Exception:
        if self.quiet:
            return {"error": True, "message": str(error)}
        raise error

    async def _create_file(
        self, contents: bytes, ext: str, name: str | None = None
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

               print(results)

            .. code-block:: JSON

               {
                   "file_name": "vicky",
                   "file_type": "image/jpeg",
                   "file_url": "https://cofuvfbkdyfchroaxcvi.supabase.co/storage/v1/object/public/avatars/vicky.jpg"
               }
        """

        response = await self.request.get("https://thedobby.club/api/avatars/random/")

        return response.json()

    async def animechan(self):
        """
        Fetches a random anime quote from the AnimeChan API.

        Returns:
            ``dict``: Contains the quote content, anime name, and character details.

        Example:
            .. code-block:: python

               >>> await api.animechan()

            .. code-block:: JSON

               {
                   "content": "Those who hate themselves, cannot love or trust others.",
                   "anime": {
                       "id": 649,
                       "name": "Neon Genesis Evangelion",
                       "altName": "Neon Genesis Evangelion"
                   },
                   "character": {
                       "id": 2111,
                       "name": "Rei Ayanami"
                    }
              }
        """
        response = await self.request.get("https://animechan.io/api/v1/quotes/random")
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
            theme (``str``, *optional*): The theme for the code snippet. Available themes:
                - "3024-night"
                - "a11y-dark"
                - "blackboard"
                - "base16-dark"
                - "base16-light"
                - "cobalt"
                - "duotone-dark"
                - "dracula-pro"
                - "hopscotch"
                - "lucario"
                - "material"
                - "monokai"
                - "nightowl"
                - "nord"
                - "oceanic-next"
                - "one-light"
                - "one-dark"
                - "panda-syntax"
                - "parasio-dark"
                - "seti"
                - "shades-of-purple"
                - "solarized+dark"
                - "solarized+light"
                - "synthwave-84"
                - "twilight"
                - "verminal"
                - "vscode"
                - "yeti"
                - "zenburn"
                Default is ``"seti"``.
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
                print(response)
                if response['success']:
                    print(f"Code image saved as '{response['result']}'.")
                else:
                    print(f"Error: {response['error']}")

            .. code-block:: JSON
               :caption: output

                {
                    "success": true,
                    "result": "downloads/carbon_Z6b6oUv7.png"
                }

            .. code-block:: text

                Code image saved as 'downloads/carbon_Z6b6oUv7.png'.
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

    async def get_emoji(
        self, endpoint: str = "random", category: str = None, group: str = None
    ) -> dict:
        """
        Fetch emoji data from EmojiHub API.

        This function allows fetching:
             - Random emoji
             - Random emoji by category or group
             - All emojis
             - All emojis by category or group

        Args:
            endpoint (str, optional): API endpoint to use.
                Options:
                    - "random" : Get a random emoji (default)
                    - "all"    : Get all available emojis

            category (str, optional): Filter emojis by category.
                Available Categories:
                    - "smileys-and-people"
                    - "animals-and-nature"
                    - "food-and-drink"
                    - "travel-and-places"
                    - "activities"
                    - "objects"
                    - "symbols"
                    - "flags"

            group (str, optional): Filter emojis by group.
                Available Groups:
                    - For "smileys-and-people":
                        "body", "cat-face", "clothing", "creature-face", "emotion", "face-negative",
                        "face-neutral", "face-positive", "face-role", "face-sick", "family",
                        "monkey-face", "person", "person-activity", "person-gesture",
                        "person-role", "skin-tone"

                    - For "animals-and-nature":
                        "animal-amphibian", "animal-bird", "animal-bug", "animal-mammal",
                        "animal-marine", "animal-reptile", "plant-flower", "plant-other"

                    - For "food-and-drink":
                        "dishware", "drink", "food-asian", "food-fruit", "food-prepared",
                        "food-sweet", "food-vegetable"

                    - Other Categories:
                        Groups are usually same as category name like:
                        "travel-and-places", "activities", "objects", "symbols", "flags"

        Returns:
            dict: JSON response containing emoji data or error message.

            Example Success Response:

                .. code-block:: JSON

                    {
                        "success": true,
                        result: {
                            "name": "hugging face",
                            "category": "smileys and people",
                            "group": "face positive",
                            "htmlCode": ["&#129303;"],
                            "unicode": ["U+1F917"]
                        }
                    }

            Example Error Response:

                .. code-block:: JSON

                    {
                        "success": false, "error": "Failed to fetch emoji"
                    }

        Example:

        .. code-block:: python

            # Get a random emoji
            emoji = await api.get_emoji()

            # Get random emoji from a specific group
            emoji = await api.get_emoji(endpoint="random", group="face-positive")

            # Get all emojis from a specific category
            emoji = await api.get_emoji(endpoint="all", category="food-and-drink")

            # Get all emojis
            emoji = await api.get_emoji(endpoint="all")
        """

    base = "https://emojihub.yurace.pro/api"

    url = f"{base}/{endpoint}"

    if category:
        url += f"/category/{category}"
    if group:
        url += f"/group/{group}"

    response = await self.request.get(url)

    if response.status_code == 200:
        return {"success": False, "result": response.json()}

    return {"success": False, "error": "Failed to fetch emoji"}

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

    async def get_btc_value(self, currency: str | None = None) -> dict:
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

    async def get_truth(self, rating: str = None) -> dict:
        """
        Fetches a truth question from the `API <https://docs.truthordarebot.xyz/api-docs>`_ .

        Args:
            rating (``str``, *optional*): The rating of the question. Must be "pg", "pg13", or "r".

        Returns:
            ``dict``: The JSON response containing the truth question.
        """
        params = {"rating": rating} if rating else {}
        response = await self.request.get(
            "https://api.truthordarebot.xyz/v1/truth", params=params
        )
        return response.json()

    async def get_dare(self, rating: str = None) -> dict:
        """
        Fetches a dare question from the `API <https://docs.truthordarebot.xyz/api-docs>`_ .

        Args:
            rating (``str``, *optional*): The rating of the question. Must be "pg", "pg13", or "r".

        Returns:
            ``dict``: The JSON response containing the dare question.
        """
        params = {"rating": rating} if rating else {}
        response = await self.request.get(
            "https://api.truthordarebot.xyz/v1/dare", params=params
        )
        return response.json()

    async def get_wyr(self, rating: str = None) -> dict:
        """
        Fetches a Would You Rather question from the `API <https://docs.truthordarebot.xyz/api-docs>`_ .

        Args:
            rating (``str``, *optional*): The rating of the question. Must be "pg", "pg13", or "r".

        Returns:
            ``dict``: The JSON response containing the Would You Rather question.
        """
        params = {"rating": rating} if rating else {}
        response = await self.request.get(
            "https://api.truthordarebot.xyz/v1/wyr", params=params
        )
        return response.json()

    async def get_nhie(self, rating: str = None) -> dict:
        """
        Fetches a Never Have I Ever question from the `API <https://docs.truthordarebot.xyz/api-docs>`_ .

        Args:
            rating (``str``, *optional*): The rating of the question. Must be "pg", "pg13", or "r".

        Returns:
            ``dict``: The JSON response containing the Never Have I Ever question.
        """
        params = {"rating": rating} if rating else {}
        response = await self.request.get(
            "https://api.truthordarebot.xyz/v1/nhie", params=params
        )
        return response.json()

    async def get_paranoia(self, rating: str = None) -> dict:
        """
        Fetches a Paranoia question from the `API <https://docs.truthordarebot.xyz/api-docs>`_ .

        Args:
            rating (``str``, *optional*): The rating of the question. Must be "pg", "pg13", or "r".

        Returns:
            ``dict``: The JSON response containing the Paranoia question.
        """
        params = {"rating": rating} if rating else {}
        response = await self.request.get(
            "https://api.truthordarebot.xyz/v1/paranoia", params=params
        )
        return response.json()

    async def hashtag(self, query: str, country: str = None) -> list:
        """
        Fetches hashtags based on the given query. If a country code is provided,
        it fetches hashtags related to the query for that specific country. Otherwise,
        it fetches the best hashtags for the query.

        Args:
            query (``str``): The search term or category for which hashtags are to be fetched.
            country (``str``, *optional*): The country code (e.g., 'IN' for India). Defaults to None.

        Returns:
            list: A list of hashtags related to the query, either based on the country or globally.

        Examples:
            .. code-block:: python

               >>> await api.hashtag('python')
               ['#python', '#coding', '#programming', '#developer']

               >>> await api.hashtag('python', 'IN')
               ['#pythonindia', '#codingindia', '#programmingindia', '#developerindia']
        """
        if country:
            page = await self.request.get(
                f"https://www.tagsfinder.com/en-{country}/related/{query}/"
            )
            soup = BeautifulSoup(page.content, "html.parser")
            hashtags = soup.find(id="hashtagy").get_text()
            if hashtags:
                hashtags = hashtags.strip().split(" ")
        else:
            page = await self.requests.get(f"http://best-hashtags.com/hashtag/{query}/")
            soup = BeautifulSoup(page.content, "html.parser")
            hashtags = soup.find("p1").get_text()
            if hashtags:
                hashtags = hashtags.strip().split(" ")

        return hashtags

    async def quote(self) -> str:
        """
        Fetches a random quote.

        Returns:
            ``str``: The content of a random quote followed by the author's name.
        """
        response = await self.request.get(self.base_urls["quote"], verify=False)
        data = response.json()
        return f"{data['content']}\n\nauthor - {data['author']}"

    async def random_user(self) -> dict:
        """
        Fetch a random user details from the `Random API <https://randomuser.me/>`_ .

        Returns:
            ``dict``: Parsed JSON response with user details.
        """
        response = await self.request.get("https://randomuser.me/api/")
        return response.json()

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

        font.getbbox("hg")[3]
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

    async def get_words(self, limit=10, length=None, letter=None, alphabetize=False):
        """
        Fetch random words from the Random Word API.

        Args:
            limit (``int``): Number of words to generate (default is 10).
            length (``int``): Length limit of the word (default is None).
            letter (``str``): First letter of the words (optional).
            alphabetize (``bool``): Whether to alphabetize the result (default is False).

        Returns:
            ``list``: A list of random words or an error message.

        Example:

            .. code-block:: python

                r = await api.get_words()
                print(r)

                r = await api.get_words(limit=4)
                print(r)

                r = await api.get_words(limit=2, length=3)
                print(r)

            .. code-block:: JSON

                [
                    "Comic", "Thirsting", "Uncover", "Justice", "Unroasted",
                    "Emphatic", "Agonize", "Upside", "Unmasking", "Limpness"
                ]

            .. code:: JSON

                [ "Dayroom", "Native", "Grudging", "Bagel" ]

            .. code-block:: JSON

                ["jot", "opt"]
        """
        params = {
            "words": limit,
            "type": "capitalized",
            "alphabetize": str(alphabetize).lower(),
        }
        if limit:
            params["limit"] = length
        if letter:
            params["letter"] = letter

        response = await self.request.get(self.base_urls["words"], params=params)
        return response.json()

    async def cat(self):
        """
        Fetches a random cat image URL.

        Returns:
            ``str`` or ``None``: The URL of a random cat image if available; None if no response is received.


        Example:
            .. code-block:: python

               >>> await api.cat()

            .. code-block:: text

                https://cdn2.thecatapi.com/images/baf.jpg

        """
        response = await self.request.get(self.base_urls["cat"])
        response = response.json()
        return response[0]["url"] if response else None

    async def dog(self):
        """
        Fetches a random dog image URL.

        Returns:
            ``str`` or None: The URL of a random dog image if available; None if no response is received.

        Example:
            .. code-block:: python

               >>> await api.dog()

            .. code-block:: text

                https://random.dog/914e15e9-ddf2-4b7a-b380-0aa9ff7458e7.PNG

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

    async def meme(self) -> dict:
        """
        Fetches a random meme image URL.

        Returns:
            ``dict``: A dict containing the results.

        Example:
            .. code-block:: python

               result = await api.meme()
               print(result)

            .. code-block:: json

               {
                  "postLink": "https://redd.it/1i1fqhq",
                  "subreddit": "dankmemes",
                  "title": "Our beloved half reptile, half cyborg",
                  "url": "https://i.redd.it/pjg18sljr0de1.png",
                  "nsfw": false,
                  "spoiler": false,
                  "author": "Techno-Xenos",
                  "ups": 189,
                  "preview": [
                    "https://preview.redd.it/pjg18sljr0de1.png?width=108&crop=smart&auto=webp&s=eb4141c3ac83bb2e9847fc598a5f676a9bf5425b",
                    "https://preview.redd.it/pjg18sljr0de1.png?width=216&crop=smart&auto=webp&s=28ba33960f084eeeb8218c1aab36a51cd80cbc0d",
                    "https://preview.redd.it/pjg18sljr0de1.png?width=320&crop=smart&auto=webp&s=87f0748cbaa3082160c13c453352c805010cd7d6"
                  ]
               }
        """

        response = await self.request.get("https://meme-api.com/gimme")
        return response.json()

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

        Example:

            .. code-block:: python

                res = await api.bing_image("Pokemon")

                print(res)

            .. code-block:: JSON


                [
                    "https://cdn.custom-cursor.com/collections/129/cover-pokemon-preview.png",
                    "https://images.pexels.com/photos/9560277/pexels-photo-9560277.jpeg?cs=srgb&dl=pexels-erik-mclean-9560277.jpg&fm=jpg",
                    "https://images.pexels.com/photos/9661257/pexels-photo-9661257.jpeg?cs=srgb&dl=pexels-erik-mclean-9661257.jpg&fm=jpg"
                ]
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

    async def upload_image(self, file_path: str | bytes | BytesIO) -> dict:
        """Uploads an image to `Envs.sh <https://envs.sh>`_.

        Args:
            file_path (Union[str, bytes, BytesIO]): The image file to upload. Can be one of:
                - str: Local file path (e.g., "image.png").
                - bytes: Raw binary data of the file.
                - BytesIO: File-like object containing binary data.

        Returns:
            dict: A dictionary containing the upload result:
                - On success: {"success": true, "url": "<file_url>", "retention": "<days> days"}
                - On failure: {"success": false, "error": "<error_message>"}
                Retention period is calculated based on file size, ranging from 30 to 90 days.

        Examples:

            .. code-block:: python
               :caption: Upload an image from a file path

                x = await api.upload_image("image.png")
                print(x)
                if x["success"]:
                    print(f"Your uploaded file link is {x["url"]} and this will be deleted in {x["retention"]}")


            .. code-block:: json

                {
                    "success": true,
                    "url": "https://envs.sh/abc.png",
                    "retention": "85 days"
                }

            .. code-block:: text

                Your uploaded file link is https://envs.sh/abc.png and this will be deleted in 85 days.


            .. code-block:: python
               :caption: Upload an image from binary data

                with open("image.png", "rb") as f:
                    x = await api.upload_image(f.read())
                print(x)
                # Output: {"success": true, "url": "https://envs.sh/def.png", "retention": "78 days"}

            .. code-block:: python
               :caption: Upload an image from BytesIO

                from io import BytesIO
                x = await api.upload_image(BytesIO(b"image binary data"))
                print(x)
                # Output: {"success": true, "url": "https://envs.sh/ghi.png", "retention": "82 days"}

            .. code-block:: python
               :caption: Invalid input example

                x = await api.upload_image(12345)
                print(x)
                # Output: {"success": false, "error": "Invalid input type"}

            .. code-block:: python
               :caption: File not found error

                x = await api.upload_image("non_existent_file.png")
                print(x)
                # Output: {"success": false, "error": "File not found: 'non_existent_file.png'"}
        """
        if isinstance(file_path, str):
            try:
                async with aiofiles.open(file_path, "rb") as f:
                    image_bytes = await f.read()
            except FileNotFoundError:
                return {"success": False, "error": f"File not found: '{file_path}'"}
        elif isinstance(file_path, (bytes, BytesIO)):
            image_bytes = (
                file_path if isinstance(file_path, bytes) else file_path.getvalue()
            )
        else:
            return {"success": False, "error": "Invalid input type"}

        file_size = len(image_bytes)
        max_size, min_age, max_age = 512 * 1024 * 1024, 30, 90
        retention = min_age + (-max_age + min_age) * pow((file_size / max_size - 1), 3)
        retention = max(min_age, min(max_age, retention))

        url = "https://envs.sh"
        files = {"file": ("upload.png", image_bytes, "image/png")}

        try:
            response = await self.request.post(url=url, files=files)
            return {
                "success": True,
                "url": response.text.strip(),
                "retention": f"{round(retention)} days",
            }
        except Exception as e:
            return {"success": False, "error": str(e)}

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

        Example:

            .. code-block:: python

                response = await api.domain_search("github")

                domains = response.get("domains")

                print(domains)

                if domains:
                    print(f"Found a  total of {response["total"]} domains.

            .. code-block:: JSON


                {
                    "domains": [
                        {
                            "domain": "xngithub-ou3lv93ce3f.com",
                            "create_date": "2025-03-21T15:48:02.308178",
                            "update_date": "2025-03-21T15:48:02.308180",
                            "country": null,
                            "isDead": "False",
                            "A": null,
                            "NS": null,
                            "CNAME": null,
                            "MX": null,
                            "TXT": null
                        },
                        {
                            "domain": "github-security-login.com",
                            "create_date": "2025-03-14T16:06:36.281306",
                            "update_date": "2025-03-14T16:06:36.281308",
                            "country": null,
                            "isDead": "False",
                            "A": null,
                            "NS": null,
                            "CNAME": null,
                            "MX": null,
                            "TXT": null
                        },
                        {
                            "domain": "github-azure-app.com",
                            "create_date": "2025-03-13T06:43:49.541243",
                            "update_date": "2025-03-13T06:43:49.541244",
                            "country": null,
                            "isDead": "False",
                            "A": null,
                            "NS": null,
                            "CNAME": null,
                            "MX": null,
                            "TXT": null
                        }
                        ...
                    ],
                    "total": 96,
                    "time": "4",
                    "next_page": null
                 }
            .. code-block::

                Found a total of 96 domains.
        """
        url = self.base_urls["domain"].format(domain=domain, zone=zone)

        response = await self.request.get(url)

        return response.json()

    async def get_word_definitions(self, word: str) -> list[dict]:
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

    async def take_screenshot(
        self,
        url: str,
        screen: str = "desktop",
        format: str = "jpeg",
        full: bool = False,
    ) -> str:
        """
        Generate a screenshot of a webpage using the given parameters.

        Args:
            url (str): The URL of the webpage to capture.
            screen (str, optional): The screen resolution or preset to use.
                Can be a predefined name listed in the **Screens** section (e.g., "desktop", "24_desktop")
                or a custom resolution in the format "width×height". Defaults to "desktop".
            format (str, optional): The image format for the screenshot ("jpeg" or "png"). Defaults to "jpeg".
            full (bool, optional): Whether to capture the full page. Defaults to False.

        Returns:
            str: The filename of the saved screenshot.

        Raises:
            ValueError: If the URL or screen resolution is invalid.

        Screens:
            Predefined screen names and their resolutions:

            - **Commons**:

              - "meta_thumbnail": 1200×628
              - "desktop": 1440×1024
              - "mackbook_pro": 1152×700
              - "surface_book": 1500×1000
              - "imac": 1280×720
              - "androvalue": 480×1024
              - "ipad": 414×736
              - "iphone": 480×1024

            - **Desktop and Laptop**:

              - "24_desktop": 1920×1200
              - "23_desktop": 1920×1080
              - "22_desktop": 1680×1050
              - "20_desktop": 1600×900
              - "19_desktop": 1440×900
              - "15_notebook": 1366×768
              - "13_notebook": 1024×800
              - "10_notebook": 1024×600

            - **Tablets**:

              - "ipad_pro": 1024×1366
              - "ipad_mini_air": 768×1024
              - "samsung_galaxy_10": 800×1280
              - "nexus_7": 600×960
              - "nexus_9": 768×1024

            - **Mobile Devices**:

              - "google_pixel": 411×731
              - "iphone_x": 375×812
              - "iphone_6_plus": 414×736
              - "iphone_7_8_6": 375×667
              - "iphone_5": 320×568
              - "iphone_4_3": 320×480

        Example:

            .. code-block:: python

               filename = await api.take_screenshot(
                   url="https://github.com/vivekkumar-in",
                   screen="iphone",
                   format="png",
                   full=True
               )
               print(f"Screenshot saved as {filename}")

        .. note::

           - If you are using tweet URLs, then only the "Format" setting will work; the "Set" option will be ignored.
           - There is a 10-second timeout; if the screenshot job takes more than 10 seconds, it will fail.
           - Use JPG in most cases; PNG will cause errors in many instances.
           - If using full screen, only use JPG; PNG will cause errors.
           - If trying to screenshot a slow website, the time limit will cause an error.
           - If the website has ads, the chances of failure are high.
           - Use HD Quality only on small screen sizes.
        """

        url_regex = re.compile(
            r"^(https?:\/\/)?(([a-z\d]([a-z\d-]*[a-z\d])*)\.)+[a-z]{2,}(:\d+)?(\/[-a-z\d%_.~+]*)*(\?[;&a-z\d%_.~+=-]*)?(\#[-a-z\d_]*)?$",
            re.IGNORECASE,
        )
        if not re.match(url_regex, url):
            raise ValueError("Invalid URL provided.")
        if not url.startswith(("http://", "https://")):
            url = "https://" + url

        screens = {
            # common
            "meta_thumbnail": (1200, 628),
            "desktop": (1440, 1024),
            "mackbook_pro": (1152, 700),
            "surface_book": (1500, 1000),
            "imac": (1280, 720),
            "androvalue": (480, 1024),
            "ipad": (414, 736),
            "iphone": (480, 1024),
            # Desktop and Laptop Resolutions
            "24_desktop": (1920, 1200),
            "23_desktop": (1920, 1080),
            "22_desktop": (1680, 1050),
            "20_desktop": (1600, 900),
            "19_desktop": (1440, 900),
            "15_notebook": (1366, 768),
            "13_notebook": (1024, 800),
            "10_notebook": (1024, 600),
            # iPad/Tablets Resolutions
            "ipad_pro": (1024, 1366),
            "ipad_mini_air": (768, 1024),
            "samsung_galaxy_10": (800, 1280),
            "nexus_7": (600, 960),
            "nexus_9": (768, 1024),
            # Mobile Resolutions
            "google_pixel": (411, 731),
            "iphone_x": (375, 812),
            "iphone_6_plus": (414, 736),
            "iphone_7_8_6": (375, 667),
            "iphone_5": (320, 568),
            "iphone_4_3": (320, 480),
            # Default
            "desktop": (1440, 1024),
        }

        if "×" in screen:
            try:
                width, height = map(int, screen.split("×"))
            except ValueError:
                raise ValueError(
                    "Invalid custom resolution format. Use 'width×height'."
                )
        else:
            resolution = screens.get(screen)
            if not resolution:
                raise ValueError(f"Invalid screen value: {screen}")
            width, height = resolution

        payload = {
            "url": url,
            "width": width,
            "height": height,
            "format": format,
            "full": full,
        }

        response = await self.request.post(
            "https://webscreenshot.vercel.app/api", json=payload
        )
        base64_string = response.json()["image"].split(",")[1]
        base64_decoded = b64decode(base64_string)
        path = await self._create_file(base64_decoded, ext=format, name="webshot")
        return path
