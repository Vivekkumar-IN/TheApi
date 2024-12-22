Welcome to the **TheApix!** This library allows you to easily interact with the API using asynchronous options.

#### Installation

```sh
pip install TheApix
```

##### FilePath Class
The `FilePath` class is a wrapper around a file path string, adding an additional `delete()` method to handle file deletion.

```python
class FilePath(str):
    """
    A wrapper around a file path string that provides an additional delete method.

    Attributes:
        path (str): The file path to the media file.

    Methods:
        delete(): Attempts to delete the file at the specified path.
                  If deletion fails, it handles the exception gracefully.
    """

    def delete(self):
        """Deletes the file at the specified path, handling exceptions if deletion fails."""
        try:
            os.remove(self)
        except Exception:
            pass
```

##### Usage Example

Whenever a media path is returned, it will be wrapped in a `FilePath` object. You can then call `delete()` on that object to delete the file if it exists.

```python
from TheApi import api

# Example of using the API to get a file path
file_path = await api.blackpink(query='Pokemon')  # Returns the file path where the blackpink media is saved

print(file_path)  # Print the file path

file_path.delete()  # Delete the file if it exists
```

In the example above, `file_path` will be an instance of the `FilePath` class, which allows you to easily delete the file associated with the media once you are done with it.

---

# 📘 API Documentation

## Status

| Function           | Status |
|--------------------|--------|
| [1. Animechan](#1-animechan) | ❌
| [2. Avatar](#2-avatar) | ✅
| [3. Bing Image](#3-bing-image) | ❌
| [4. Blackpink](#4-blackpink) | ✅
| [5. Carbon](#5-carbon) | ❌
| [6. Cat](#6-cat) | ✅
| [7. Delete](#7-delete) | ❌
| [8. Dog](#8-dog) | ✅
| [9. Domain Search](#9-domain-search) | ❌
| [10. Fakerapi](#10-fakerapi) | ❌
| [11. Fox](#11-fox) | ✅
| [12. Gen Qr](#12-gen-qr) | ❌
| [13. Generate Pdf](#13-generate-pdf) | ❌
| [14. Get](#14-get) | ❌
| [15. Get Advice](#15-get-advice) | ❌
| [16. Get Btc Value](#16-get-btc-value) | ✅
| [17. Get Fake Addresses](#17-get-fake-addresses) | ✅
| [18. Get Fake Credit Cards](#18-get-fake-credit-cards) | ✅
| [19. Get Fake Images](#19-get-fake-images) | ✅
| [20. Get Hindi Jokes](#20-get-hindi-jokes) | ✅
| [21. Get Jokes](#21-get-jokes) | ✅
| [22. Get Uselessfact](#22-get-uselessfact) | ✅
| [23. Get Word Definitions](#23-get-word-definitions) | ✅
| [24. Get Words](#24-get-words) | ✅
| [25. Github Search](#25-github-search) | ✅
| [26. Hindi Quote](#26-hindi-quote) | ✅
| [27. Hug](#27-hug) | ❌
| [28. Meme](#28-meme) | ✅
| [29. Neko](#29-neko) | ✅
| [30. Post](#30-post) | ❌
| [31. Put](#31-put) | ❌
| [32. Pypi](#32-pypi) | ✅
| [33. Quote](#33-quote) | ❌
| [34. Riddle](#34-riddle) | ✅
| [35. Stackoverflow Search](#35-stackoverflow-search) | ✅
| [36. Upload Image](#36-upload-image) | ✅
| [37. Wikipedia](#37-wikipedia) | ✅
| [38. Write](#38-write) | ✅


## 🎓 How to Use Each Function

### 1. Animechan

**Description**:
Fetches a random anime quote from the AnimeChan API.

**Returns:**
  - **dict**: Contains the quote content, anime name, and character details.

```python
from Pokemon import api

result = await api.animechan()
print(result)
```

#### Expected Output

```text
'coroutine' object is not subscriptable
```

### 2. Avatar

**Description**:
Fetches a random avatars from the thedobby.club API.

**Returns:**
  - **dict**: Contains the file name, file type, and file URL.

```python
from Pokemon import api

result = await api.avatar()
print(result)
```

#### Expected Output

```json
{
    "file_name": "sam",
    "file_type": "image/jpeg",
    "file_url": "https://cofuvfbkdyfchroaxcvi.supabase.co/storage/v1/object/public/avatars/sam.jpg"
}
```

### 3. Bing Image

**Description**:
Searches Bing for images based on a query and retrieves image URLs.

**Args:**
  - **query (str)**: The search query string for finding images.
  - **limit (int, optional)**: The maximum number of image URLs to return. Defaults to 3.

**Returns:**
  - **list**: A list of image URLs retrieved from the Bing search results.

```python
from TheApi import api

result = await api.bing_image(query='Pokemon', limit=3)
print(result)
```

#### Expected Output

```text
cannot use a string pattern on a bytes-like object
```

### 4. Blackpink

**Description**:
Creates a stylized "Blackpink"-themed image with custom text, color, and optional border.
**Args:**
  - **query (str)**: The text to display on the image.
  - **color (str, optional)**: The primary color of the text and gradient background in hex format.
    Defaults to "#ff94e0" (a pink shade).
  - **border_color (str, optional)**: The color of the image border in hex format.
    If not provided, defaults to the value of `color`.
**Returns:**
  - **FilePath**: The file path of the generated image with delete attribute.

```python
from TheApi import api

result = await api.blackpink(query='Pokemon', color='#ff94e0', border_color=None)
print(result)
```

#### Expected Output

```text
/home/runner/work/TheApi/TheApi/downloads/blackpink_FPAiR4Gl.jpg
```

### 5. Carbon

**Description**:
Generates a code snippet image using the Carbon API, saves it to the downloads folder, uploads it, and returns the URL of the uploaded image.

**Args:**
  - **query (str)**: The code snippet to be rendered as an image.

**Returns:**
  - **FilePath**: The file path of the saved image.

```python
from TheApi import api

result = await api.carbon(query='Pokemon')
print(result)
```

#### Expected Output

```text
name 'params' is not defined
```

### 6. Cat

**Description**:
Fetches a random cat image URL.

**Returns:**
  - **str or None**: The URL of a random cat image if available; None if no response is received.

```python
from Pokemon import api

result = await api.cat()
print(result)
```

#### Expected Output

```text
https://cdn2.thecatapi.com/images/417.jpg
```

### 7. Delete

**Description**:
No description available.

```python
from TheApi import api

result = await api.delete(url='Pokemon', headers=None, params=None, data=None, json=None, timeout=None, allow_redirects=True, ssl=None)
print(result)
```

#### Expected Output

```text
Request URL is missing an 'http://' or 'https://' protocol.
```

### 8. Dog

**Description**:
Fetches a random dog image URL.

**Returns:**
  - **str or None**: The URL of a random dog image if available; None if no response is received.

```python
from Pokemon import api

result = await api.dog()
print(result)
```

#### Expected Output

```text
https://random.dog/59fd867b-becf-46e9-b050-604540bd2dcc.jpg
```

### 9. Domain Search

**Description**:
Fetches domain information from the DomainsDB API.

**Args:**
  - **domain (str)**: The domain name to search for (e.g., "facebook").
  - **zone (str)**: The domain zone to search within (e.g., "com").Default is "com".

**Returns:**
  - **dict**: A dictionary containing the results of the domain search.

```python
from TheApi import api

result = await api.domain_search(domain='Pokemon', zone='com')
print(result)
```

#### Expected Output

```text
Expecting value: line 1 column 1 (char 0)
```

### 10. Fakerapi

**Description**:
Fetch data from the FakerAPI using aiohttp.

**Args:**
  - **endpoint (str)**: The resource endpoint. Valid endpoints are:
    - companies
    - addresses
    - books
    - CreditCards
    - images
    - persons
    - places
    - products
    - texts
    - users

**Description**:
quantity (int, optional): Number of rows to fetch (default: 3, max: 1000). locale (str, optional): Locale for the data (default: 'en_US').  [ See Valid locale ](https://fakerapi.it/#params_locale)

**Raises:**
  - **ValueError**: If the locale is invalid, the endpoint is invalid, or the quantity
    is outside the allowed range.

**Returns:**
  - **dict**: Response data from the API.


### 11. Fox

**Description**:
Fetches a random fox image URL.

**Returns:**
  - **str or None**: The URL of the fox image if available, otherwise None.

```python
from Pokemon import api

result = await api.fox()
print(result)
```

#### Expected Output

```text
https://randomfox.ca/?i=11
```

### 12. Gen Qr

**Description**:
Generate a QR code using api.qrserver.com and save it as a PNG file.

**Args:**
  - **data (str)**: The content for the QR code.
  - **size (str)**: The size of the QR code in the format 'WIDTHxHEIGHT' (default: '150x150').
  - **foreground_color (str)**: The color of the QR code (default: '000000' - black).
  - **background_color (str)**: The background color of the QR code (default: 'FFFFFF' - white).

**Returns:**
  - **FilePath**: The file path where the QR code was saved.

```python
from TheApi import api

result = await api.gen_qr(data='Pokemon', size='150x150', foreground_color='000000', background_color='FFFFFF')
print(result)
```

#### Expected Output

```text
Invalid path: /home/runner/work/TheApi/TheApi/downloads/QrCode_YZ5JTtou.png. Path must be a string.
```

### 13. Generate Pdf

**Description**:
Generates a PDF from a URL or an HTML string and saves it to a file.

**Args:**
  - **source (str)**: The URL of the website (if `from_url=True`) or the HTML string (if `from_url=False`).
  - **from_url (bool, optional)**: Whether to generate the PDF from a URL (True) or an HTML string (False).

**Returns:**
  - **FilePath**: The file path where the PDF was saved.

**Raises:**
  - **ValueError**: If `from_url` is True and `source` is not a valid URL.


### 14. Get

**Description**:
No description available.

```python
from TheApi import api

result = await api.get(url='Pokemon', headers=None, params=None, timeout=None, allow_redirects=True, ssl=None)
print(result)
```

#### Expected Output

```text
Request URL is missing an 'http://' or 'https://' protocol.
```

### 15. Get Advice

**Description**:
Fetches a random piece of advice.

**Returns:**
  - **str**: A random advice message.

```python
from Pokemon import api

result = await api.get_advice()
print(result)
```

#### Expected Output

```text
'coroutine' object is not subscriptable
```

### 16. Get Btc Value

**Description**:
Fetches the current value of Bitcoin (BTC) for the specified currency or all currencies.

**Args:**
  - **currency (str, optional)**: The currency code (e.g., 'eur', 'usd', 'gbp').
    If None, fetches BTC value for all currencies.

**Returns:**
  - **dict**: The response containing BTC value(s) for the specified currency or all currencies.

**Raises:**
  - **ValueError**: If the provided currency is invalid or the request fails.

```python
from TheApi import api

result = await api.get_btc_value(currency=None)
print(result)
```

#### Expected Output

```json
{
    "EUR": {
        "code": "EUR",
        "description": "Euro",
        "rate": "92,596.98",
        "rate_float": 92596.9803,
        "symbol": "&euro;"
    },
    "GBP": {
        "code": "GBP",
        "description": "British Pound Sterling",
        "rate": "76,890.147",
        "rate_float": 76890.1469,
        "symbol": "&pound;"
    },
    "USD": {
        "code": "USD",
        "description": "United States Dollar",
        "rate": "96,141.526",
        "rate_float": 96141.5261,
        "symbol": "&#36;"
    }
}
```

### 17. Get Fake Addresses

**Description**:
Fetch fake address data from the FakerAPI.

**Args:**
  - **quantity (int, optional)**: Number of address entries to fetch (default: 1).
  - **locale (str, optional)**: Locale for the address data (default: "en_US"), [ See Valid locale ](https://fakerapi.it/#params_locale).

**Returns:**
  - **dict**: Response data from the API.

```python
from TheApi import api

result = await api.get_fake_addresses(quantity=1, locale='en_US')
print(result)
```

#### Expected Output

```json
{
    "status": "OK",
    "code": 200,
    "locale": "en_US",
    "seed": null,
    "total": 1,
    "data": [
        {
            "id": 1,
            "street": "4981 Yundt Via Apt. 481",
            "streetName": "Raynor Plaza",
            "buildingNumber": "728",
            "city": "Quitzonborough",
            "zipcode": "32045",
            "country": "Martinique",
            "country_code": "MQ",
            "latitude": -23.922615,
            "longitude": 149.969368
        }
    ]
}
```

### 18. Get Fake Credit Cards

**Description**:
Fetch fake credit card data from the FakerAPI.

**Args:**
  - **locale (str, optional)**: Locale for the credit card data (default: "en_US"), [ See Valid locale ](https://fakerapi.it/#params_locale).
  - **amount (int, optional)**: Number of credit card entries to fetch (default: 1).

**Returns:**
  - **dict**: Response data from the API.

```python
from TheApi import api

result = await api.get_fake_credit_cards(locale='en_US', quantity=1)
print(result)
```

#### Expected Output

```json
{
    "status": "OK",
    "code": 200,
    "locale": "en_US",
    "seed": null,
    "total": 1,
    "data": [
        {
            "type": "MasterCard",
            "number": "2344358911592395",
            "expiration": "02/26",
            "owner": "Alycia Vandervort"
        }
    ]
}
```

### 19. Get Fake Images

**Description**:
Fetch fake image data from the FakerAPI.

**Args:**
  - **quantity (int, optional)**: Number of images to fetch (default: 1).
  - **locale (str, optional)**: Locale for the images (default: "en_US"), [ See Valid locale ](https://fakerapi.it/#params_locale).
  - **type (str, optional)**: Type of image (e.g., 'any', 'animals', 'business', etc.; default: "any").
  - **width (int, optional)**: Width of the images (default: 640).
  - **height (int, optional)**: Height of the images (default: 480).

**Returns:**
  - **dict**: Response data from the API.

```python
from TheApi import api

result = await api.get_fake_images(quantity=1, locale='en_US', type='any', width=640, height=480)
print(result)
```

#### Expected Output

```json
{
    "status": "OK",
    "code": 200,
    "locale": "en_US",
    "seed": null,
    "total": 1,
    "data": [
        {
            "title": "Voluptate eos et quis.",
            "description": "Qui corrupti possimus amet quae fuga. Non dignissimos in odit corrupti soluta aspernatur. Doloremque praesentium laborum et ipsum fugiat in.",
            "url": "https://picsum.photos/640/480"
        }
    ]
}
```

### 20. Get Hindi Jokes

**Description**:
Fetches a random Hindi joke.

**Returns:**
  - **str**: A random Hindi joke if available, or "No joke found" if not available.

```python
from Pokemon import api

result = await api.get_hindi_jokes()
print(result)
```

#### Expected Output

```text
वो अपनी पतली कमर पर साड़ी बांध रही थी ऐसे सिविल इंजीनियर नदी पर पुल बांध रहा हो जैसे 😆🤣😋😉 
```

### 21. Get Jokes

**Description**:
Fetches a specified number of jokes.

**Args:**
  - **amount (int, optional)**: The number of jokes to retrieve. Defaults to 1.

**Returns:**
  - **str**: A single joke if `amount` is 1.
  - **list**: If `amount` > 1, returns numbered jokes.

```python
from TheApi import api

result = await api.get_jokes(amount=1)
print(result)
```

#### Expected Output

```text
I was going to tell a dead baby joke. But I decided to abort.
```

### 22. Get Uselessfact

**Description**:
Fetches a random useless fact.

**Returns:**
  - **str**: A random useless fact.

```python
from Pokemon import api

result = await api.get_uselessfact()
print(result)
```

#### Expected Output

```text
Nearly 80% of all animals on earth have six legs.
```

### 23. Get Word Definitions

**Description**:
Fetch definitions for a word from the Dictionary API.

**Args:**
  - **word (str)**: The word to fetch definitions for.

**Returns:**
  - **list**: A list of dictionaries containing the word definitions.

**Raises:**
  - **ValueError**: If the `word` is not provided or the API request fails.

```python
from TheApi import api

result = await api.get_word_definitions(word='Pokemon')
print(result)
```

#### Expected Output

```json
{
    "title": "No Definitions Found",
    "message": "Sorry pal, we couldn't find definitions for the word you were looking for.",
    "resolution": "You can try the search again at later time or head to the web instead."
}
```

### 24. Get Words

**Description**:
Fetch random words from the Random Word API.

**Args:**
  - **words (int)**: Number of words to generate (default is 10).
  - **letter (str)**: First letter of the words (optional).
  - **word_type (str)**: Type of words (lowercase, uppercase, capitalized; default is capitalized).
  - **alphabetize (bool)**: Whether to alphabetize the result (default is False).

**Returns:**
  - **list**: A list of random words or an error message.

```python
from TheApi import api

result = await api.get_words(words=10, letter=None, word_type='capitalized', alphabetize=False)
print(result)
```

#### Expected Output

```text
Senate
Stout
Scholar
Quizzical
Proposal
Fax
Answering
Unsorted
Headway
Outdoors
```

### 25. Github Search

**Description**:
Searches GitHub for various types of content.

**Args:**
  - **query (str)**: The search query.
  - **search_type (str, optional)**: The type of search. Can be one of:
    - "repositories"
    - "users"
    - "organizations"
    - "issues"
    - "pull_requests"
    - "commits"
    - "topics"

**Description**:
Defaults to "repositories". max_results (int, optional): The maximum number of results to return. Defaults to 3.

**Returns:**
  - **list**: A list of search results or an error message.

```python
from TheApi import api

result = await api.github_search(query='Pokemon', search_type='repositories', max_results=3)
print(result)
```

#### Expected Output

```json
[
    {
        "name": "PokemonGo-Map",
        "full_name": "AHAAAAAAA/PokemonGo-Map",
        "description": "\ud83c\udf0f Live visualization of all the pokemon in your area... and more! (shutdown)",
        "url": "https://github.com/AHAAAAAAA/PokemonGo-Map",
        "language": null,
        "stargazers_count": 7527,
        "forks_count": 2815
    },
    {
        "name": "pokemon-showdown",
        "full_name": "smogon/pokemon-showdown",
        "description": "Pok\u00e9mon battle simulator.",
        "url": "https://github.com/smogon/pokemon-showdown",
        "language": "TypeScript",
        "stargazers_count": 4836,
        "forks_count": 2827
    },
    {
        "name": "PokemonGo-Bot",
        "full_name": "PokemonGoF/PokemonGo-Bot",
        "description": "The Pokemon Go Bot, baking with community.",
        "url": "https://github.com/PokemonGoF/PokemonGo-Bot",
        "language": "Python",
        "stargazers_count": 3879,
        "forks_count": 1542
    }
]
```

### 26. Hindi Quote

**Description**:
Fetches a random Hindi quote.

**Returns:**
  - **str**: The content of a random Hindi quote.

```python
from Pokemon import api

result = await api.hindi_quote()
print(result)
```

#### Expected Output

```text
जब कोई विचार अनन्य रुप से मस्तिष्क पर अधिकार कर लेता है तब वह वास्तविक, भौतिक या मानसिक अवस्था में परिवर्तित हो जाता है!
```

### 27. Hug

**Description**:
Fetches a specified number hug gif from the Nekos.Best API.

**Args:**
  - **amount (int)**: The number of neko images to fetch. Defaults to 1.

**Returns:**
  - **list**: A list of dictionaries containing information about each fetched neko image or GIF.
    Each dictionary typically includes:
    - anime_name (str): The name of the anime.
    - url (str): The URL of the GIF.

```python
from TheApi import api

result = await api.hug(amount=1)
print(result)
```

#### Expected Output

```text
'coroutine' object is not subscriptable
```

### 28. Meme

**Description**:
Fetches a random meme image URL.

**Returns:**
  - **str or None**: The URL of the meme image if available, otherwise None.

```python
from Pokemon import api

result = await api.meme()
print(result)
```

#### Expected Output

```text
https://preview.redd.it/nxhw4jf3h28e1.png?width=640&crop=smart&auto=webp&s=8bd7a667b89090cc726b93acd4d9e6fe577d8d0b
```

### 29. Neko

**Description**:
Fetches a specified number of neko images or GIFs from the Nekos.Best API.

**Args:**
  - **endpoint (str)**: The endpoint category to fetch content from. Default is "neko".
    Valid image endpoints:
    - "husbando", "kitsune", "neko", "waifu"
    Valid GIF endpoints:
    - "baka", "bite", "blush", "bored", "cry", "cuddle", "dance", "facepalm",
    "feed", "handhold", "handshake", "happy", "highfive", "hug", "kick",
    "kiss", "laugh", "lurk", "nod", "nom", "nope", "pat", "peck", "poke",
    "pout", "punch", "shoot", "shrug", "slap", "sleep", "smile", "smug",
    "stare", "think", "thumbsup", "tickle", "wave", "wink", "yawn", "yeet"
    amount (int): The number of items to fetch. Default is 3.

**Returns:**
  - **dict**: A dictionary containing the results of the request. The dictionary has a key `"results"`,
    which holds a list of items.

**Raises:**
  - **ValueError**: If the endpoint is not a valid category.

```python
from TheApi import api

result = await api.neko(endpoint='neko', amount=3)
print(result)
```

#### Expected Output

```json
{
    "results": [
        {
            "artist_href": "https://www.pixiv.net/en/users/9133563",
            "artist_name": "\u4f0a\u5948",
            "source_url": "https://www.pixiv.net/en/artworks/94887748",
            "url": "https://nekos.best/api/v2/neko/98ef29c7-b0be-4f72-9436-88e4dac0a3fc.png"
        },
        {
            "artist_href": "https://www.pixiv.net/en/users/220294",
            "artist_name": "\u3082\u3082\u3057\u304d",
            "source_url": "https://www.pixiv.net/en/artworks/98035200",
            "url": "https://nekos.best/api/v2/neko/1aa8a4b0-a34a-4e88-a1ae-3f36c39fcc47.png"
        },
        {
            "artist_href": "https://twitter.com/done_kanda",
            "artist_name": "\u9928\u7530\u30c0\u30f3",
            "source_url": "https://twitter.com/done_kanda/status/1323188100667904002",
            "url": "https://nekos.best/api/v2/neko/f0f1af20-53fe-4eba-b07e-18a343a6b03a.png"
        }
    ]
}
```

### 30. Post

**Description**:
No description available.

```python
from TheApi import api

result = await api.post(url='Pokemon', headers=None, params=None, data=None, json=None, files=None, timeout=None, allow_redirects=True, ssl=None)
print(result)
```

#### Expected Output

```text
Request URL is missing an 'http://' or 'https://' protocol.
```

### 31. Put

**Description**:
No description available.

```python
from TheApi import api

result = await api.put(url='Pokemon', headers=None, params=None, data=None, json=None, timeout=None, allow_redirects=True, ssl=None)
print(result)
```

#### Expected Output

```text
Request URL is missing an 'http://' or 'https://' protocol.
```

### 32. Pypi

**Description**:
Retrieves metadata information about a specified Python package from the PyPI API.

**Args:**
  - **package_name (str)**: The name of the package to search for on PyPI.

**Returns:**
  - **dict or None**: A dictionary with relevant package information if found.
    Returns None if the package is not found or there is an error.

```python
from TheApi import api

result = await api.pypi(package_name='Pokemon')
print(result)
```

#### Expected Output

```json
{
    "info": {
        "author": "Vanessa Sochat",
        "author_email": "vsoch@noreply.github.users.com",
        "bugtrack_url": null,
        "classifiers": [],
        "description": "# pokemon\n\nWatch the pokemon ascii being born!\n\n![img/generation.gif](https://github.com/vsoch/pokemon/raw/master/img/generation.gif)\n\nThis is a module for generating ascii art for any of the 890 pokemon, across 8 generations, in the Pokedex. The package includes functions for generating \"gravatars\" (pokemon associated with an identifier like an email address), and functions for searching and exploring the database. The library includes a [version of the database](pokemon/database/db.json) generated with [pokemon/make_db.py](pokemon/make_db.py) that can be updated by re-running the script. The choice of ascii art is to produce pokemon images or avatars that are suited for command line tools.\n\n```bash\n$ pokemon\nusage: pokemon [-h] [--avatar AVATAR] [--pokemon POKEMON] [--message MESSAGE]\n               [--catch] [--list]\n\ngenerate pokemon ascii art and avatars\n\noptional arguments:\n  -h, --help         show this help message and exit\n  --avatar AVATAR    generate a pokemon avatar for some unique id.\n  --pokemon POKEMON  generate ascii for a particular pokemon (by name)\n  --message MESSAGE  add a custom message to your ascii!\n  --catch            catch a random pokemon!\n  --list             list pokemon available\n```\n\n## Installation\n\nYou can install directly from pip:\n\n```bash\n$ pip install pokemon\n```\n\nor for the development version, clone the repo and install manually:\n\n```bash\ngit clone https://github.com/vsoch/pokemon\ncd pokemon\npip install .\n```\n\n## Produce an avatar\n\nAn \"avatar\" is an image that is consistently associated with some unique ID. In our case, this is an ascii avatar. For example,\n\n![img/avatar.png](img/avatar.png)\n\nTo do this, I take the hash of a string, and then use modulus to get the remainder of that hash divided by the number of pokemon in the database. This means that, given that the database doesn't change, and given that the pokemon have unique IDs in the range of 1 to 721, you should always get the same image for some unique id (like an email).\n\n**Note** the database was updated between version 0.34 and version 0.35, so you will\nget different avatars depending on the version you are using. There are Docker tags\nand pip installs available for each, and version 0.35 is suggested to use with Python 3.\n\n```bash\n$ pokemon --avatar vsoch\n\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n@@@@@@@@@?:::::::::::::::+.+.@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n@@@@@@@*?%:::::::::*::****#SSSSS%.**S+@@@@@@@@@@@@@@@@@@@@@@\n@@@@@@@*???:::::::*********#...+****++++S:@@@@@@@@@@@@@@@@@@\n@@@@@@@::SSS............S+.*....*****?%S+#@@@@@@@@@@@@@@@@@@\n@@@@@@@@@@@@@@.?SS.S.....S?%%%%%%%%..**+....?@@@@@@@@@@@@@@@\n@@@@@@@@@@@@@@@@..%???????#%%%%%%%....**++.....?@@@@@@@@@@@@\n@@@@@@@@@@@@@@..+++%????????????%%%%%%*.......%++%@@@@@@@@@@\n@@@@@@@@@@@@S.+++++S%+++SS%..????%%%?..............@@@@@@@@@\n@@@@@@@@@@@%++++S+S++++.......?@%%%%%......SSSSSS:@@@@@@@@@@\n@@@@@@@@@?.++.+++++%**.#.....?.%%%%%,@@@@@@@@@@@#.%@@@@@@@@@\n@@@@@@@?.*.....+.**.*.....%.....+++%@@#+++S.%?+++.%@@@@@@@@@\n@@@@@#***......%:.**++%........++++#.#+++++.++++.S@@@@@@@@@@\n@@@@,+%.......?+++++......#....#.**+++#@@%++++.SS@@@@@@@@@@@\n@@@:+?+...?..S.......S%%%...S+++::.+++@%++++.?.#@@@@@@@@@@@@\n@@@@@@@,?...S%%*@@.?%++SS.S++.+S...?#.+++S++..@@@@@@@@@@@@@@\n@@@@@@@@@@@@@@*...?.@SS+.SS....?....#++%:+..S@@@@@@@@@@@@@@@\n@@@@@@@@@@?+S.%?#+@@@@@S...#???%%%S@+:::...@@@@@@@@@@@@@@@@@\n@@@@@@@++S....#@@@@@@@@@@@@@@@S.%...:::+#...@@@@@@@@@@@@@@@@\n@@@@#++.....S@@@@@@@@@@@@@.S..++..%?:...+?...@@@@@@@@@@@@@@@\n@@@.......?@@@@@@@@@@@@+.....+++......#.++....*@@@@@@@@@@@@@\n@@.*+...@@@@@@@@@@@@S.....?.S+..S....++...S....@@@@@@@@@@@@@\n@+*++@@@@@@@@@@@@,?........@:%.*SS?+++++..+.....%@@@@@@@@@@@\n@:+%@@@@@@@@@@@:?........?@@@#:::.+++++#...+.....#@@@@@@@@@@\n@S@@@@@@@@@@@@+.........#@@@@@@+..++++....+......S.,@@@@@@@@\n@@@@@@@@@@@@@S%##.....S@@@@@@@@@*.??.......#@%...??.#@@@@@@@\n@@@@@@@@@@@@@S%@....?S@@@@@@@@@@@@@%.?...?.@@@.S+.....@@@@@@\n@@@@@@@@@@@@@@@@S.....?@@@@@@@@@@@@@@@.%S.?@@@@+++S....@@@@@\n@@@@@@@@@@@@@@@@+......@@@@@@@@@@@@@@@@@@@@@@@@.+++S....@@@@\n@@@@@@@@@@@@@@@.%......@@@@@@@@@@@@@@@@@@@@@@@@@++++......@@\n@@@@@@@@@@@@@@.%......S@@@@@@@@@@@@@@@@@@@@@@@@@++++......@@\n@@@@@@@@@@@@@S.#.....++@@@@@@@@@@@@@@@@@@@@@@@@@..+..+....S@\n@@@@@@@@@@@.::++S.@@?+?@@@@@@@@@@@@@@@@@@@@@@@@@+...#S+?..SS\n@@@@@@@@@@@@,@,@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@.+..*++,@\n@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@.::+@@\n\nvsoch\n```\n\nYou can also use the functions on command line:\n\n```python\nfrom pokemon.skills import get_avatar\n\n# Just get the string!\navatar = get_avatar(\"vsoch\", print_screen=False)\nprint(avatar)\n\n# Remove the name at the bottom, print to screen (default)\navatar = get_avatar(\"vsoch\", include_name=False)\n```\n\n## List Pokemon\nWant a complete listing of your Pokemon choices in the database?\n\n```bash\npokemon --list\n\nSlugma\nMachop\nDruddigon\nMagby\nClawitzer\nGrowlithe\nEmpoleon\nDusknoir\nRhydon\nKrookodile\nHoppip\nSwellow\nOddish\nScrafty\nBoldore\nPancham\nBeheeyem\nHonedge\n...\nJumpluff\nRotom\nFrillish\nLapras\nClamperl\nWingull\nVespiquen\nKeldeo\nMareep\nPhantump\nMedicham\nShuckle\nLickitung\nChingling\n```\n\nYou could use this to parse through a function. Here we show a simple loop to print the name of the Pokemon, but you would be more creative!\n\n```bash\nfor gotcha in $(pokemon --list)\n    do\n    echo $gotcha\ndone\n```\n\n## Randomly select a Pokemon\n\nYou might want to just randomly get a pokemon! Do this with the `--catch` command line argument!\n\n```bash\n      pokemon --catch\n\n      @%,@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n      .????.@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n      .???????S@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n      :?????????#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n      *?????????????*@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n      @???????#?????###@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@,*.??#\n      @?????,##,S???#####@@@@@@@@@@@@@@@@@@@@@@@@@@S##????????????\n      @?????*,,,,,,########@@@@@@@@@@@@@@@@@:###????????????????#@\n      @##????,,,,,,,,,#####@@@@@@@@@@@@@.######?????#?:#????????@@\n      @####?#,,,,,,,,,,,##@@@@@@@@@@@@@@#######*,,,,,*##+?????+@@@\n      @######,,,,,,,,,,,S@@@@@@@@@@@@@@#.,,,,,,,,,,,,,,:?####@@@@@\n      @######,,,,,,,,,,%@@,S.S.,@@@@@@@,,,,,,,,,,,,,,,######@@@@@@\n      @@#####,,,,,,,,.,,,,,,,,,,,,,,,*#,,,,,,,,,,,,,.#####:@@@@@@@\n      @@@@@@@@@@.#,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,######@@@@@@@@@\n      @@@@@@@@@,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,+######@@@@@@@@@@\n      @@@@@@@@%,,,,,++:,,,,,,,,,,,,,,,,,,,,,@@:.######:@@@@@@@@@@@\n      @@@@@@@:,,,:##@@@#,,,,,,,,,,,,?@S#,,,,,,@@@@@@@@@@@@@@@@@@@@\n      @@@@@@@?,,,#######,,,,,,,,,,,#.@:##,,,:?@@@@@@@@@@@@@@@@@@@@\n      @@@@@@@.,,S,??%?*,,,,,,,,,,,,####?%+,::%@@@@@@@@@@@@@@@@@@@@\n      @@@@@@@@?..*+,,,,,,*,,,,,,,,,,,+#S,::::*@@@@@@@@@@@@@@@@@@@@\n      @@@@@@@@@%..*,,,,,,,,,,,,,,,,,,,:.*...%@@@@@@@@@@@@@@@@@@@@@\n      @@@@@@@@@@.**::*::::::,,:::::::+.....@@@@@@@@@@@@@@@@@@@@@@@\n      @@@@@@@@.@@@@?:**:::*::::::::::*...@@@@@@@@@@@@@@@@@@@@@@@@@\n      @@@@@?,,,,,,,,,:,##S::::**:::S#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n      @@@@@@@.,,,,,,:S#?##?########:#****#,@@@@@@@@@@@@@@@@@@@@@@@\n      @@@@@@@@@@,%:*%,??#,,,,:*S##**:..****:,.*@@@@@@@@@@@@@@@@@@@\n      @@@@@@@@@@@@@+,,,,,,,,,,,,,,,,,,*...*:,.,@@@@@@@@@@@@@@@@@@@\n      @@@@@@@@@@@@@+,,,,,,,,,,,,,,,,,,?@@@@@*#?@@@@@@@@@@@@@@@@@@@\n      @@@@@@@@@@@@@*,,,,,,,,,,,,,,,,,,.@#########?@@@@@@@@@@@@@@@@\n      @@@@@@@@@@@@@.*:,,,,,,,,,,,,,,:.##%,?#####????:@@@@@@@@@@@@@\n      @@@@@@@@@@@@@@?.....*******....S@@@@@@:##?????@@@@@@@@@@@@@@\n      @@@@@@@@@@@@@@S.+..********...#%@@@@@@@@@##,@@@@@@@@@@@@@@@@\n      @@@@@@@@@@@#*,,,,*.#@@@@@@@..*:,,*S@@@@@@@@@@@@@@@@@@@@@@@@@\n      @@@@@@@@@@+@,%,,,#@@@@@@@@@@,S,,,%,,:@@@@@@@@@@@@@@@@@@@@@@@\n\n      Pichu\n```\nYou can equivalently use the `--message` argument to add a custom message to your catch!\n\n```bash\n      pokemon --catch --message \"You got me!\"\n\n      @@@@@@@@@*.@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n      @@@@@@@@...+@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n      @@@@@@@@++++@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n      :..+,@@+.+++%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n      @..++++S++++++.?...@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n      @@@:S.S+SSS.S%++.+++@@@@@@@@@@+.%.@@@@@@@@@@@@@@@@@@@@@@@@@@\n      @@@@:SSSSSSSSSS,@@@@@@@,:,:.SS+.....+.@@@@@@@@@@@@@@@@@@@@@@\n      @@@@,:%SS++SS.,.%,:,S,,,,+..%.........S.@@@@@@@@@@@@@@@@@@@@\n      @@@@@,:*...:,,+,.,,,,,,,*%%%++++..+++SSS+@@@@@@@@@@@@@@@@@@@\n      @@@@@@,,.....%:,,,:.:.,:.%%.SSSS++SS+%+S%,+@@@@@@@@@@@@@@@@@\n      @@@@@@@*.....S...***+,,,%..%++,?SSS.%.%%%:,.,@@@@@@@@@@@@@@@\n      @@@@@@@@,+**........,,,,....++S@,+%..#..%,,S..@@@@@@@@@@@@@@\n      @@@@@@@@@@@@@@@@*..:,,,,,%..%++S%%.%%.S%%,,*+.+@@@@@@@@@@@@@\n      @@@@@@@@@@@@@@@@S,,,,,,,,,%%%..SS..%?%%%,,,S+...@@@@@@@@@@@@\n      @@@@@@@@@@@@@@@@S.:::::::::%.%%S...%%%%:::*.....**@@@@@@@@@@\n      @@@@@@@@@@@@@@@@.%%..:::::::S%%.?%%%%%:::....**,S,,:@@@@@@@@\n      @@@@@@@@@@@@@@:::*%%%%?..*:::,.%%%%.,:*.%@@.*:,,,:,,S@....@@\n      @@@@@@@@@@@@@:,:,::*.?%%%%%%?+*%%?.?%%%%%+@@,,,,,,,.++%++@@@\n      @@@@@@@@@@@@@@*,,,,,**...*%%%%%%%%%%?++++++.@,,,,,SS+SS++@@@\n      @@@@@@@@@@@@@,,.,S,,,,:....***%%?%++++++++++.@.,,+SSSSS.S+@@\n      @@@@@@@@@@@@,,SSSS..:.%,:*..?%%??%%++++++.+S+@@@.S..%S.%.S++\n      @@@@@@@@@@@,,S.....S::*.@@@%%%%@?%%#+++++%%%?S@@@@@.%.,@@...\n      @@@@@@@@@@@:,,?.%%%::::@@@...%.@?.%.++++.+%%%%.@@@@..++@@@@@\n      @@@@@@@@@@S,.%%.:,,,,,S@@@@@.?@@+SS,S..........@@@@@,@@@@@@@\n      @@@@@@@@@@@+S...++.,,:@@@@@@@@@@@@@@@%....SSS+SS@@@@@@@@@@@@\n\n      You got me!\n```\n\nYou can also catch pokemon in your python applications. If you are going to be generating many, it is recommended to load the database once and provide it to the function, otherwise it will be loaded each time.\n\n```bash\nfrom pokemon.master import catch_em_all, get_pokemon\n\npokemons = catch_em_all()\ncatch = get_pokemon(pokemons=pokemons)\n```\n\nThe catch is a dictionary, with keys as the pokemon ID, and the value being another dictionary with various meta data (height, weight, japanese, link, ascii, etc).\n\n\n## Updating the database\n\nThe database was generated by running the script make_db.py, and you can update it by running it yourself, if at some point in the future new pokemon are added to the index.\n\n```bash\ngit clone https://github.com/vsoch/pokemon\ncd pokemon\ncd scripts\npip install -r requirements.txt\npython make_db.py\n```\n\nThen move your old database (and you can do this to keep it in case you don't want changes to persist):\n\n```bash\nmv pokemon/database dbbackup\nmv ./database pokemon/database\n```\n\nThe file pokemons.json will be saved under [pokemon/databases](pokemon/databases). Next, install as usual.\n\n```\npython setup.py install\n```\n\n## Docker\nYou can also use the [Docker image](https://hub.docker.com/r/vanessa/pokemon/),\nwhich provides the various functions and [Scientific Filesystem](https://sci-f.github.io) apps.\nThe 0.35 tag was developed with Python 2, and the 0.35 tag is Python 3 and later\n(with an updated database).\n\nWhat can I do?\n\n```bash\ndocker run vanessa/pokemon apps\n      list\n     catch\n    avatar\n```\n\nGive me my avatar!\n\n```bash\ndocker run vanessa/pokemon run avatar vsoch\n```\n\nCatch a random Pokemon\n\n```bash\ndocker run vanessa/pokemon run catch\n```\n\nWhat Pokemon can I catch?\n\n```bash\ndocker run vanessa/pokemon run list\n```\n\nCatch me Venusaur!\n\n```bash\ndocker run vanessa/pokemon run catch Venusaur\n```\n\nYou can also build the image locally:\n\n```bash\ndocker build -t vanessa/pokemon .\n```\n\n## Singularity\n\nWe can do the same with Singularity containers!\n\n\n```bash\nsudo singularity build pokemons Singularity\n```\n\nWhat can I do?\n\n```bash\n./pokemons apps\n    avatar\n     catch\n      list\n```\n\nGive me my avatar!\n\n```bash\n./pokemons run avatar vsoch\n```\n\nCatch a random Pokemon\n\n```bash\n./pokemons run catch\n```\n\nWhat Pokemons can I catch?\n\n```bash\n./pokemons list\n...\nPhantump\nTrevenant\nPumpkaboo\nGourgeist\nBergmite\nAvalugg\nNoibat\nNoivern\nXerneas\nYveltal\nZygarde\nDiancie\nHoopa\nVolcanion\n```\n\nCatch a specific Pokemon\n\n```bash\n./pokemons run catch Pikachu\n[catch] executing /bin/bash /scif/apps/catch/scif/runscript Pikachu\n@@@@@@@@@@@@@.@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n@@@@@@@@@@@,??@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n@@@@@@@@@@.###@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n@@@@@@@@@,##:,@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@*?@@\n@@@@@@@@@#::::@@@@@@@@@@@@@@@@@@@@@@@@@,*.???%@@@@@@@@*,,,@@\n@@@@@@@@::,,::@@@@@@@@@@@@@@@@@@%:,,:#####??,@@@@@@*,,,,,,:@\n@@@@@@@@%:,,:.@@@@@@@@@@@@@@.:::::::.#####@@@@@@@.::,,,,,::@\n@@@@@@@@%::::.,,,,:,:%@@:,:::::::::S###@@@@@@@@%,:::::,::,:%\n@@@@@@@@.S,,,,,,,,::::::::::::::::?@@@@@@@@@@?::::::::::::::\n@@@@@@@:,,,,,,,:,#.#?::::::+.,@@@@@@@@@@@@@.::::::::::::::::\n@@@@@,#:S,,:,::::*#.,:::::::*@@@@@@@@@@@@,::::::::::::::::+@\n@@@@@:%S::::::*,,:::...+.::::S@@@@@@@@@@:::::::::::::::%@@@@\n@@@@*.::::,SSSS%::::+++++:::::%@@@@@@@@:::::::::::::%@@@@@@@\n@@@@@.+:,,::S%+S::::.+++:::::::,@@@@@@@@@:::*::::S@@@@@@@@@@\n@@@@@@.S:::::.*.::::::::::::::::@@@@@@@@@,****%@@@@@@@@@@@@@\n@@@@@@@@.:::::::::::::::*:,**::::,@@@@@@@@,***@@@@@@@@@@@@@@\n@@@@,%,::::::::::::::::*.****::,:S%@@@@@@......@@@@@@@@@@@@@\n,**::::,,,,,,:::::::::::+:**:::::,::@@?.....S@@@@@@@@@@@@@@@\n%:*:,:::,,,,,,,,,,,::::::%::::::,,,::,@S..+@@@@@@@@@@@@@@@@@\n@@@@@,S%+::*,:,,::,:,,,,::::::::::::::?@@%SS?@@@@@@@@@@@@@@@\n@@@@@@@@@@@@.:,,,,:,,,,,,,:::::::::::::+SSSSS.@@@@@@@@@@@@@@\n@@@@@@@@@@@@@:,,,:::::,::::,:::::::::::*?.@@@@@@@@@@@@@@@@@@\n@@@@@@@@@@@@@+,:,:,::::::::::,,::,::::**.SS@@@@@@@@@@@@@@@@@\n@@@@@@@@@@@@@S,,:,,,,::::::::::::::::****@@@@@@@@@@@@@@@@@@@\n@@@@@@@@@@@@@@:::::::::****::::::*******S@@@@@@@@@@@@@@@@@@@\n@@@@@@@@@@@@@@@**********.%..***********@@@@@@@@@@@@@@@@@@@@\n@@@@@@@@@@@@@@@@@,?+S%@@@@@@@@@@@@......@@@@@@@@@@@@@@@@@@@@\n@@@@@@@@@@@@@@@@@@@+..*@@@@@@@@@@@@@:+**@@@@@@@@@@@@@@@@@@@@\n```\n\n\n## Issues and updates\n\nWould you like different or updated functionality?\nPlease ping me by adding an [issue](https://github.com/vsoch/pokemon/issues)!\nI did this for fun, might sneak it into a few command line applications,\nand it's pretty simple so far! I hope you have fun with it! :D\n\n\n",
        "description_content_type": "text/markdown",
        "docs_url": null,
        "download_url": "",
        "downloads": {
            "last_day": -1,
            "last_month": -1,
            "last_week": -1
        },
        "dynamic": null,
        "home_page": "https://github.com/vsoch/pokemon",
        "keywords": "pokemon,avatar,ascii,gravatar",
        "license": "LICENSE",
        "license_expression": null,
        "license_files": null,
        "maintainer": "",
        "maintainer_email": "",
        "name": "pokemon",
        "package_url": "https://pypi.org/project/pokemon/",
        "platform": null,
        "project_url": "https://pypi.org/project/pokemon/",
        "project_urls": {
            "Homepage": "https://github.com/vsoch/pokemon"
        },
        "provides_extra": null,
        "release_url": "https://pypi.org/project/pokemon/0.36/",
        "requires_dist": null,
        "requires_python": "",
        "summary": "ascii database of pokemon... in Python!",
        "version": "0.36",
        "yanked": false,
        "yanked_reason": null
    },
    "last_serial": 16452812,
    "releases": {
        "0.1": [
            {
                "comment_text": "",
                "digests": {
                    "blake2b_256": "40e7f3e80e891bb08d03ad6d0f69f6f5c0210da359de7f2064a14dedfe3833fe",
                    "md5": "cf5f8ec9193ec0b8d6fde9e0ee5db71a",
                    "sha256": "1e0abc5f79195f0677882d8117961fcdc533af7ea553ae84aa111f47a13fa2a0"
                },
                "downloads": -1,
                "filename": "pokemon-0.1.tar.gz",
                "has_sig": false,
                "md5_digest": "cf5f8ec9193ec0b8d6fde9e0ee5db71a",
                "packagetype": "sdist",
                "python_version": "source",
                "requires_python": null,
                "size": 21104373,
                "upload_time": "2016-07-25T01:05:41",
                "upload_time_iso_8601": "2016-07-25T01:05:41.197529Z",
                "url": "https://files.pythonhosted.org/packages/40/e7/f3e80e891bb08d03ad6d0f69f6f5c0210da359de7f2064a14dedfe3833fe/pokemon-0.1.tar.gz",
                "yanked": false,
                "yanked_reason": null
            }
        ],
        "0.2": [
            {
                "comment_text": "",
                "digests": {
                    "blake2b_256": "5ce0f9568f9ba22dbf618835bfc6c85a4dfb44d459fec6bad76521955ff38396",
                    "md5": "54c101cf8cbf9a0321fad874355d56c3",
                    "sha256": "1ed4ed4875ea1d2b76d4c4e556f4af22229bba10b8dabd954d68127cca4757a2"
                },
                "downloads": -1,
                "filename": "pokemon-0.2.tar.gz",
                "has_sig": false,
                "md5_digest": "54c101cf8cbf9a0321fad874355d56c3",
                "packagetype": "sdist",
                "python_version": "source",
                "requires_python": null,
                "size": 21104335,
                "upload_time": "2016-07-25T01:25:56",
                "upload_time_iso_8601": "2016-07-25T01:25:56.461624Z",
                "url": "https://files.pythonhosted.org/packages/5c/e0/f9568f9ba22dbf618835bfc6c85a4dfb44d459fec6bad76521955ff38396/pokemon-0.2.tar.gz",
                "yanked": false,
                "yanked_reason": null
            }
        ],
        "0.21": [
            {
                "comment_text": "",
                "digests": {
                    "blake2b_256": "8b0fc5652aa63c81bd400e72432115dc5156a63cf7d10113736037dad6279eb5",
                    "md5": "f22988c070544cd4968b2488359b2868",
                    "sha256": "a5835841f95dfadfce2a0e15abce91ce8405adbc96a27b63fd8c13286b63e5b7"
                },
                "downloads": -1,
                "filename": "pokemon-0.21.tar.gz",
                "has_sig": false,
                "md5_digest": "f22988c070544cd4968b2488359b2868",
                "packagetype": "sdist",
                "python_version": "source",
                "requires_python": null,
                "size": 21090122,
                "upload_time": "2017-09-14T02:49:41",
                "upload_time_iso_8601": "2017-09-14T02:49:41.200741Z",
                "url": "https://files.pythonhosted.org/packages/8b/0f/c5652aa63c81bd400e72432115dc5156a63cf7d10113736037dad6279eb5/pokemon-0.21.tar.gz",
                "yanked": false,
                "yanked_reason": null
            }
        ],
        "0.22": [
            {
                "comment_text": "",
                "digests": {
                    "blake2b_256": "dbcd58d86a5b61a566d3585695dfd5e1b64045a7b98b6fedce95365d8421d761",
                    "md5": "ffdd76135d19666fb76d70976df3767b",
                    "sha256": "d78e29baa5f04b5b8962405ca5264bddd494e1c6377c0016b295244bad3423a6"
                },
                "downloads": -1,
                "filename": "pokemon-0.22.tar.gz",
                "has_sig": false,
                "md5_digest": "ffdd76135d19666fb76d70976df3767b",
                "packagetype": "sdist",
                "python_version": "source",
                "requires_python": null,
                "size": 21090118,
                "upload_time": "2017-09-14T03:04:49",
                "upload_time_iso_8601": "2017-09-14T03:04:49.097545Z",
                "url": "https://files.pythonhosted.org/packages/db/cd/58d86a5b61a566d3585695dfd5e1b64045a7b98b6fedce95365d8421d761/pokemon-0.22.tar.gz",
                "yanked": false,
                "yanked_reason": null
            }
        ],
        "0.3": [
            {
                "comment_text": "",
                "digests": {
                    "blake2b_256": "7b4d2a0c205bfe71e8b9fcef09d210e61167008dbc3abc8148ccead7068f7049",
                    "md5": "beace9c117853737a0f52cdaa3cb225c",
                    "sha256": "07de0afebb8c16e172a27b470b51b1d3e966a6626a075055e029b89b64fbd2a3"
                },
                "downloads": -1,
                "filename": "pokemon-0.3.tar.gz",
                "has_sig": false,
                "md5_digest": "beace9c117853737a0f52cdaa3cb225c",
                "packagetype": "sdist",
                "python_version": "source",
                "requires_python": null,
                "size": 21104329,
                "upload_time": "2016-07-29T00:46:30",
                "upload_time_iso_8601": "2016-07-29T00:46:30.092413Z",
                "url": "https://files.pythonhosted.org/packages/7b/4d/2a0c205bfe71e8b9fcef09d210e61167008dbc3abc8148ccead7068f7049/pokemon-0.3.tar.gz",
                "yanked": false,
                "yanked_reason": null
            }
        ],
        "0.31": [
            {
                "comment_text": "",
                "digests": {
                    "blake2b_256": "9667c173bdd8b6ec4acff34a6b890aaa20a52bafcf12b489b32392345df13387",
                    "md5": "a07daf9e00c6da7181864ff92310d14a",
                    "sha256": "9a731f7e5b0ff7552027deaf7e0ed5be2df9f1c69fb223d0a718de0a5a0dcd6b"
                },
                "downloads": -1,
                "filename": "pokemon-0.31.tar.gz",
                "has_sig": false,
                "md5_digest": "a07daf9e00c6da7181864ff92310d14a",
                "packagetype": "sdist",
                "python_version": "source",
                "requires_python": null,
                "size": 21104416,
                "upload_time": "2016-07-29T00:48:17",
                "upload_time_iso_8601": "2016-07-29T00:48:17.362823Z",
                "url": "https://files.pythonhosted.org/packages/96/67/c173bdd8b6ec4acff34a6b890aaa20a52bafcf12b489b32392345df13387/pokemon-0.31.tar.gz",
                "yanked": false,
                "yanked_reason": null
            }
        ],
        "0.32": [
            {
                "comment_text": "",
                "digests": {
                    "blake2b_256": "bc12c30daf9ba6de2a1c4cd35d4330845631a133f3f6c09f03fb43f85e4a05bb",
                    "md5": "6f450055d57eefabbfc2643cc5abbc9e",
                    "sha256": "86f234984bf0d05560497ffadd2f712ceb6b36ce41c42c2fd7b22582a81903bd"
                },
                "downloads": -1,
                "filename": "pokemon-0.32.tar.gz",
                "has_sig": false,
                "md5_digest": "6f450055d57eefabbfc2643cc5abbc9e",
                "packagetype": "sdist",
                "python_version": "source",
                "requires_python": null,
                "size": 21104411,
                "upload_time": "2016-07-29T00:51:11",
                "upload_time_iso_8601": "2016-07-29T00:51:11.804888Z",
                "url": "https://files.pythonhosted.org/packages/bc/12/c30daf9ba6de2a1c4cd35d4330845631a133f3f6c09f03fb43f85e4a05bb/pokemon-0.32.tar.gz",
                "yanked": false,
                "yanked_reason": null
            }
        ],
        "0.33": [
            {
                "comment_text": "",
                "digests": {
                    "blake2b_256": "d63029c9689bd10bfb32bccdc28ed2da13ac195e23b36dd233fa020301e32e08",
                    "md5": "6a60877f97246456ad0afa3fff7afab1",
                    "sha256": "987ed554785fda7505b8728d2248e90ddbe012ad6cd9847dc73a1a860f949031"
                },
                "downloads": -1,
                "filename": "pokemon-0.33.tar.gz",
                "has_sig": false,
                "md5_digest": "6a60877f97246456ad0afa3fff7afab1",
                "packagetype": "sdist",
                "python_version": "source",
                "requires_python": null,
                "size": 21095109,
                "upload_time": "2018-01-21T18:36:23",
                "upload_time_iso_8601": "2018-01-21T18:36:23.720233Z",
                "url": "https://files.pythonhosted.org/packages/d6/30/29c9689bd10bfb32bccdc28ed2da13ac195e23b36dd233fa020301e32e08/pokemon-0.33.tar.gz",
                "yanked": false,
                "yanked_reason": null
            }
        ],
        "0.34": [
            {
                "comment_text": "",
                "digests": {
                    "blake2b_256": "c991b740e520872890c59d24cb60f6183068bc32750d49d8bd8ad52d6d4ac780",
                    "md5": "6cc9871e9df993c838c507354eb2a6eb",
                    "sha256": "2b99a09329a81480b03f4f2070fe606b31f48310bfc2488ef61461cf47bd11ec"
                },
                "downloads": -1,
                "filename": "pokemon-0.34.tar.gz",
                "has_sig": false,
                "md5_digest": "6cc9871e9df993c838c507354eb2a6eb",
                "packagetype": "sdist",
                "python_version": "source",
                "requires_python": null,
                "size": 21095329,
                "upload_time": "2018-01-21T19:37:33",
                "upload_time_iso_8601": "2018-01-21T19:37:33.414766Z",
                "url": "https://files.pythonhosted.org/packages/c9/91/b740e520872890c59d24cb60f6183068bc32750d49d8bd8ad52d6d4ac780/pokemon-0.34.tar.gz",
                "yanked": false,
                "yanked_reason": null
            }
        ],
        "0.35": [
            {
                "comment_text": "",
                "digests": {
                    "blake2b_256": "a353f961cebf8d15d06922b1bf48e4bb2b2b2f69626fdd602871cb604891fd3a",
                    "md5": "69fefdec524365221032246bb12c5d79",
                    "sha256": "cdbf9bcadee36376ffe1329087d614d220dc9565b1a955e40b90c87c35071889"
                },
                "downloads": -1,
                "filename": "pokemon-0.35.tar.gz",
                "has_sig": false,
                "md5_digest": "69fefdec524365221032246bb12c5d79",
                "packagetype": "sdist",
                "python_version": "source",
                "requires_python": null,
                "size": 26331571,
                "upload_time": "2020-04-11T18:14:22",
                "upload_time_iso_8601": "2020-04-11T18:14:22.378212Z",
                "url": "https://files.pythonhosted.org/packages/a3/53/f961cebf8d15d06922b1bf48e4bb2b2b2f69626fdd602871cb604891fd3a/pokemon-0.35.tar.gz",
                "yanked": false,
                "yanked_reason": null
            }
        ],
        "0.36": [
            {
                "comment_text": "",
                "digests": {
                    "blake2b_256": "b542337c5a15dcf934649f1d4d659d3cf916ba9a2b5ad128d0e70aefa3338d7a",
                    "md5": "be8c2c48394481a5b8ce67f4353f090d",
                    "sha256": "20f95b9037b197bda02269547fe90c19689df96a2383e68097a44c279a6dc1ce"
                },
                "downloads": -1,
                "filename": "pokemon-0.36.tar.gz",
                "has_sig": false,
                "md5_digest": "be8c2c48394481a5b8ce67f4353f090d",
                "packagetype": "sdist",
                "python_version": "source",
                "requires_python": null,
                "size": 29567079,
                "upload_time": "2023-01-17T04:06:36",
                "upload_time_iso_8601": "2023-01-17T04:06:36.034235Z",
                "url": "https://files.pythonhosted.org/packages/b5/42/337c5a15dcf934649f1d4d659d3cf916ba9a2b5ad128d0e70aefa3338d7a/pokemon-0.36.tar.gz",
                "yanked": false,
                "yanked_reason": null
            }
        ]
    },
    "urls": [
        {
            "comment_text": "",
            "digests": {
                "blake2b_256": "b542337c5a15dcf934649f1d4d659d3cf916ba9a2b5ad128d0e70aefa3338d7a",
                "md5": "be8c2c48394481a5b8ce67f4353f090d",
                "sha256": "20f95b9037b197bda02269547fe90c19689df96a2383e68097a44c279a6dc1ce"
            },
            "downloads": -1,
            "filename": "pokemon-0.36.tar.gz",
            "has_sig": false,
            "md5_digest": "be8c2c48394481a5b8ce67f4353f090d",
            "packagetype": "sdist",
            "python_version": "source",
            "requires_python": null,
            "size": 29567079,
            "upload_time": "2023-01-17T04:06:36",
            "upload_time_iso_8601": "2023-01-17T04:06:36.034235Z",
            "url": "https://files.pythonhosted.org/packages/b5/42/337c5a15dcf934649f1d4d659d3cf916ba9a2b5ad128d0e70aefa3338d7a/pokemon-0.36.tar.gz",
            "yanked": false,
            "yanked_reason": null
        }
    ],
    "vulnerabilities": []
}
```

### 33. Quote

**Description**:
Fetches a random quote.

**Returns:**
  - **str**: The content of a random quote followed by the author's name.

```python
from Pokemon import api

result = await api.quote()
print(result)
```

#### Expected Output

```text
name 'data' is not defined
```

### 34. Riddle

**Description**:
Fetches a random riddle from the Riddles API.

**Returns:**
  - **dict**: The riddle data in JSON format.

```python
from Pokemon import api

result = await api.riddle()
print(result)
```

#### Expected Output

```text
<TheApi._request.Response object at 0x7f27648c6570>
```

### 35. Stackoverflow Search

**Description**:
Searches Stack Overflow for questions based on a query, returning results sorted by relevance or another specified criteria.

**Args:**
  - **query (str)**: The search query string.
  - **max_results (int, optional)**: The maximum number of results to return. Defaults to 3.
  - **sort_type (str, optional)**: The sorting criteria for the results, such as "relevance" or "votes". Defaults to "relevance".

**Returns:**
  - **list**: A list of search results in JSON format, with each entry containing Stack Overflow question details.

**Raises:**
  - **ValueError**: If there is an issue with the request to the Stack Overflow API.

```python
from TheApi import api

result = await api.stackoverflow_search(query='Pokemon', max_results=3, sort_type='relevance')
print(result)
```

#### Expected Output

```json
[
    {
        "tags": [
            "ios",
            "flutter",
            "dart"
        ],
        "owner": {
            "account_id": 19921816,
            "reputation": 3,
            "user_id": 14597469,
            "user_type": "registered",
            "profile_image": "https://lh6.googleusercontent.com/-aT6u2l_JT94/AAAAAAAAAAI/AAAAAAAAAAA/AMZuuclcxb94zp_q0Q2R8DQN7b6X3kgo6w/s96-c/photo.jpg?sz=256",
            "display_name": "Senem Sedef",
            "link": "https://stackoverflow.com/users/14597469/senem-sedef"
        },
        "is_answered": false,
        "view_count": 125,
        "answer_count": 0,
        "score": 0,
        "last_activity_date": 1701515081,
        "creation_date": 1622231772,
        "last_edit_date": 1701515081,
        "question_id": 67744802,
        "content_license": "CC BY-SA 4.0",
        "link": "https://stackoverflow.com/questions/67744802/the-getter-pokemon-was-called-on-null-receiver-null-tried-calling-pokemon",
        "title": "The getter &#39;pokemon&#39; was called on null. Receiver: null Tried calling: pokemon"
    },
    {
        "tags": [
            "java"
        ],
        "owner": {
            "account_id": 919945,
            "reputation": 43,
            "user_id": 951797,
            "user_type": "registered",
            "profile_image": "https://www.gravatar.com/avatar/26b06d5d95992fa3780383abe5f49a3d?s=256&d=identicon&r=PG",
            "display_name": "Brian",
            "link": "https://stackoverflow.com/users/951797/brian"
        },
        "is_answered": true,
        "view_count": 32703,
        "accepted_answer_id": 7942409,
        "answer_count": 3,
        "score": 3,
        "last_activity_date": 1577442848,
        "creation_date": 1319931614,
        "question_id": 7942384,
        "content_license": "CC BY-SA 3.0",
        "link": "https://stackoverflow.com/questions/7942384/simple-java-pokemon-fight-simulator",
        "title": "Simple Java Pokemon Fight Simulator"
    },
    {
        "tags": [
            "reactjs",
            "random",
            "axios"
        ],
        "owner": {
            "account_id": 17931576,
            "reputation": 1,
            "user_id": 13028884,
            "user_type": "registered",
            "profile_image": "https://www.gravatar.com/avatar/7ebcdd2f784bca5dc54a1a0e17354f86?s=256&d=identicon&r=PG&f=y&so-version=2",
            "display_name": "GieGie",
            "link": "https://stackoverflow.com/users/13028884/giegie"
        },
        "is_answered": false,
        "view_count": 2035,
        "answer_count": 2,
        "score": 0,
        "last_activity_date": 1652730812,
        "creation_date": 1642222168,
        "last_edit_date": 1642223800,
        "question_id": 70718940,
        "content_license": "CC BY-SA 4.0",
        "link": "https://stackoverflow.com/questions/70718940/pokemon-api-request-generate-5-pok%c3%a9mon-at-a-time",
        "title": "Pokemon API request generate 5 Pok&#233;mon at a time"
    }
]
```

### 36. Upload Image

**Description**:
Uploads an image to https://envs.sh.

**Args:**
  - **file_path (Union[str, bytes, BytesIO])**: The image file to upload.
    Can be a file path (str), binary data (bytes), or a BytesIO object.

**Returns:**
  - **str**: The URL or confirmation message of the uploaded image if the upload is successful.
    Returns "Unexpected response format" if the response format is not as expected.

**Raises:**
  - **ValueError**: If the file is not found, the input type is invalid,
    or the upload request fails.


### 37. Wikipedia

**Description**:
Searches Wikipedia for a given query and retrieves the top result's summary, URL, and image.

**Args:**
  - **query (str)**: The search term to look up on Wikipedia.

**Returns:**
  - **dict**: A dictionary containing information about the top search result, with keys:
    - title (str): The title of the Wikipedia article.
    - summary (str): A brief summary of the article's content.
    - url (str): The URL link to the full Wikipedia article.
    - image_url (str): The URL of the article's thumbnail image, or "No image available" if none exists.

**Description**:
If no results are found, returns a dictionary with an "error" key.

```python
from TheApi import api

result = await api.wikipedia(query='Pokemon')
print(result)
```

#### Expected Output

```json
{
    "title": "Pok\u00e9mon",
    "summary": "Pok\u00e9mon is a Japanese media franchise consisting of video games, animated series and films, a trading card game, and other related media. The franchise takes place in a shared universe in which humans co-exist with creatures known as Pok\u00e9mon, a large variety of species endowed with special powers. The franchise's target audience is children aged 5 to 12, but it is known to attract people of all ages.\nThe franchise originated as a pair of role-playing games developed by Game Freak, from an original concept by its founder, Satoshi Tajiri. Released on the Game Boy on February 27, 1996, the games became sleeper hits and were followed by manga series, a trading card game, and anime series and films. From 1998 to 2000, Pok\u00e9mon was exported to the rest of the world, creating an unprecedented global phenomenon dubbed \"Pok\u00e9mania\". By 2002, the craze had ended, after which Pok\u00e9mon became a fixture in popular culture, with new products being released to this day. In the summer of 2016, the franchise spawned a second craze with the release of Pok\u00e9mon Go, an augmented reality game developed by Niantic. Pok\u00e9mon has since been estimated to be the world's highest-grossing media franchise and one of the best-selling video game franchises.\nPok\u00e9mon has an uncommon ownership structure. Unlike most IPs, which are owned by one company, Pok\u00e9mon is jointly owned by three: Nintendo, Game Freak, and Creatures. Game Freak develops the core series role-playing games, which are published by Nintendo exclusively for their consoles, while Creatures manages the trading card game and related merchandise, occasionally developing spin-off titles. The three companies established The Pok\u00e9mon Company (TPC) in 1998 to manage the Pok\u00e9mon property within Asia. The Pok\u00e9mon anime series and films are co-owned by Shogakukan. Since 2009, The Pok\u00e9mon Company International (TPCi), a subsidiary of TPC, has managed the franchise in all regions outside of Asia.",
    "url": "https://en.wikipedia.org/?curid=23745",
    "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/9/98/International_Pok%C3%A9mon_logo.svg/500px-International_Pok%C3%A9mon_logo.svg.png"
}
```

### 38. Write

**Description**:
Creates an image with text written on it, using a predefined template and font, and uploads the image after generation.

**Args:**
  - **text (str)**: The text to be written on the image. Text exceeding 55 characters
    per line will be wrapped, with up to 25 lines displayed.

**Returns:**
  - **str**: The URL of the uploaded image.

**Description**:
Notes: A temporary image file is created, saved, and removed after uploading.

```python
from TheApi import api

result = await api.write(text='Pokemon')
print(result)
```

#### Expected Output

```text
/home/runner/work/TheApi/TheApi/downloads/write_WqIZXfHK.jpg
```


This Project is Licensed under [MIT License](https://github.com/Vivekkumar-IN/TheApi/blob/main/LICENSE)