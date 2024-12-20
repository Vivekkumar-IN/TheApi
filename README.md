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
| [1. Animechan](#1-animechan) | ✅
| [2. Avatar](#2-avatar) | ✅
| [3. Bing Image](#3-bing-image) | ✅
| [4. Blackpink](#4-blackpink) | ✅
| [5. Carbon](#5-carbon) | ✅
| [6. Cat](#6-cat) | ✅
| [7. Dog](#7-dog) | ✅
| [8. Domain Search](#8-domain-search) | ❌
| [9. Fakerapi](#9-fakerapi) | ❌
| [10. Fox](#10-fox) | ✅
| [11. Gen Qr](#11-gen-qr) | ✅
| [12. Generate Pdf](#12-generate-pdf) | ✅
| [13. Get Advice](#13-get-advice) | ✅
| [14. Get Btc Value](#14-get-btc-value) | ✅
| [15. Get Fake Addresses](#15-get-fake-addresses) | ✅
| [16. Get Fake Credit Cards](#16-get-fake-credit-cards) | ✅
| [17. Get Fake Images](#17-get-fake-images) | ✅
| [18. Get Hindi Jokes](#18-get-hindi-jokes) | ✅
| [19. Get Jokes](#19-get-jokes) | ✅
| [20. Get Uselessfact](#20-get-uselessfact) | ✅
| [21. Get Word Definitions](#21-get-word-definitions) | ✅
| [22. Get Words](#22-get-words) | ❌
| [23. Github Search](#23-github-search) | ✅
| [24. Hindi Quote](#24-hindi-quote) | ✅
| [25. Hug](#25-hug) | ✅
| [26. Meme](#26-meme) | ✅
| [27. Neko](#27-neko) | ✅
| [28. Pypi](#28-pypi) | ✅
| [29. Quote](#29-quote) | ✅
| [30. Riddle](#30-riddle) | ✅
| [31. Stackoverflow Search](#31-stackoverflow-search) | ✅
| [32. Upload Image](#32-upload-image) | ✅
| [33. Wikipedia](#33-wikipedia) | ✅
| [34. Write](#34-write) | ✅


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

```json
{
    "content": "For me, despair is not a goal, or a set of principles, or a lifestyle, or even an instinct... It's what defines me as Junko Enoshima! It's just my characterization! That's why I'm able to pursue despair with such purity!",
    "anime": {
        "id": 364,
        "name": "Danganronpa: The Animation",
        "altName": "Danganronpa: Kibou no Gakuen to Zetsubou no Koukousei The Animation"
    },
    "character": {
        "id": 447,
        "name": "Junko Enoshima"
    }
}
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
    "file_name": "student",
    "file_type": "image/jpeg",
    "file_url": "https://cofuvfbkdyfchroaxcvi.supabase.co/storage/v1/object/public/avatars/student.jpg"
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
http://www.technosamrat.com/wp-content/uploads/2012/05/Pokemon-Wallpapers-Picture.jpg
http://www.animextremist.com/imagenes/pokemon/pokemon103.jpg
https://www.pokemon.com/static-assets/app/static3/img/og-default-image.jpeg
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
/home/runner/work/TheApi/TheApi/downloads/blackpink_Zm7NcCTp.jpg
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
/home/runner/work/TheApi/TheApi/downloads/carbon_YpyN7JGa.png
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
https://26.media.tumblr.com/tumblr_krwvziszMn1qa9hjso1_1280.jpg
```

### 7. Dog

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
https://random.dog/f7d8ae8c-f7ed-4fd1-89a0-781e57913a38.mp4
```

### 8. Domain Search

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
Request failed: 500, message='INTERNAL SERVER ERROR', url='https://api.domainsdb.info/v1/domains/search?domain=Pokemon&zone=com'
```

### 9. Fakerapi

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
quantity (int, optional): Number of rows to fetch (default: 3, max: 1000). locale (str, optional): Locale for the data (default: 'en_US').  See Valid locale [ From Here ](https://github.com/Vivekkumar-IN/TheApi/blob/main/src%2FTheApi%2Fapi.py#L185-L261)

**Raises:**
  - **ValueError**: If the locale is invalid, the endpoint is invalid, or the quantity
    is outside the allowed range.

**Returns:**
  - **dict**: Response data from the API.


### 10. Fox

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
https://randomfox.ca/?i=1
```

### 11. Gen Qr

**Description**:
Generate a QR code using api.qrserver.com and save it as a PNG file.

**Args:**
  - **data (str)**: The content for the QR code.
  - **size (str)**: The size of the QR code in the format 'WIDTHxHEIGHT' (default: '150x150').
  - **foreground_color (str)**: The color of the QR code (default: '000000' - black).
  - **background_color (str)**: The background color of the QR code (default: 'FFFFFF' - white).
  - **file_path (str, optional)**: The file path to save the QR code.
    Defaults to "downloads/{random_str}_qr.png".

**Returns:**
  - **FilePath**: The file path where the QR code was saved.

```python
from TheApi import api

result = await api.gen_qr(data='Pokemon', size='150x150', foreground_color='000000', background_color='FFFFFF', file_path=None)
print(result)
```

#### Expected Output

```text
/home/runner/work/TheApi/TheApi/downloads/XaFZNtzl_qr.png
```

### 12. Generate Pdf

**Description**:
Generates a PDF from a URL or an HTML string and saves it to a file.

**Args:**
  - **source (str)**: The URL of the website (if `from_url=True`) or the HTML string (if `from_url=False`).
  - **file_path (str, optional)**: The file path to save the generated PDF.
    Defaults to "downloads/<random_str>_generated.pdf".
  - **from_url (bool, optional)**: Whether to generate the PDF from a URL (True) or an HTML string (False).

**Returns:**
  - **FilePath**: The file path where the PDF was saved.

**Raises:**
  - **ValueError**: If `from_url` is True and `source` is not a valid URL.


### 13. Get Advice

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
Today, do not use the words "Kind of", "Sort of" or "Maybe". It either is or it isn't.
```

### 14. Get Btc Value

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
        "rate": "93,461.895",
        "rate_float": 93461.8954,
        "symbol": "&euro;"
    },
    "GBP": {
        "code": "GBP",
        "description": "British Pound Sterling",
        "rate": "77,016.913",
        "rate_float": 77016.9129,
        "symbol": "&pound;"
    },
    "USD": {
        "code": "USD",
        "description": "United States Dollar",
        "rate": "98,427.566",
        "rate_float": 98427.5661,
        "symbol": "&#36;"
    }
}
```

### 15. Get Fake Addresses

**Description**:
Fetch fake address data from the FakerAPI.

**Args:**
  - **quantity (int, optional)**: Number of address entries to fetch (default: 1).
  - **locale (str, optional)**: Locale for the address data (default: "en_US").

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
            "street": "5948 Ward Heights",
            "streetName": "Marquardt Alley",
            "buildingNumber": "55669",
            "city": "North Titusview",
            "zipcode": "17388",
            "country": "Croatia",
            "country_code": "HR",
            "latitude": -40.762303,
            "longitude": -157.474629
        }
    ]
}
```

### 16. Get Fake Credit Cards

**Description**:
Fetch fake credit card data from the FakerAPI.

**Args:**
  - **locale (str, optional)**: Locale for the credit card data (default: "en_US").
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
            "type": "Visa",
            "number": "2492647184459864",
            "expiration": "11/27",
            "owner": "Fatima Lueilwitz"
        }
    ]
}
```

### 17. Get Fake Images

**Description**:
Fetch fake image data from the FakerAPI.

**Args:**
  - **quantity (int, optional)**: Number of images to fetch (default: 1).
  - **locale (str, optional)**: Locale for the images (default: "en_US").
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
            "title": "Quo omnis veniam ut officia.",
            "description": "Mollitia voluptas consequatur atque quia deleniti facere deleniti. Consequatur doloremque enim aut non. Voluptatibus unde assumenda omnis est corrupti illum. Qui ea ut ut ea consequatur.",
            "url": "https://picsum.photos/640/480"
        }
    ]
}
```

### 18. Get Hindi Jokes

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
Me- हैलो मैडम, मैं HDFC बैंक से बोल रहा हूं! आप क्रेडिट कार्ड लेना चाहेंगी?  
She- I have a boyfriend 
```

### 19. Get Jokes

**Description**:
Fetches a specified number of jokes.

**Args:**
  - **amount (int, optional)**: The number of jokes to retrieve. Defaults to 1.

**Returns:**
  - **str**: A single joke if `amount` is 1. If `amount` > 1, returns numbered jokes as a formatted string.

```python
from TheApi import api

result = await api.get_jokes(amount=1)
print(result)
```

#### Expected Output

```text
My husband and I were happy for 20 years. And then we met.
```

### 20. Get Uselessfact

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
Each king in a deck of playing cards represents a great king from history. Spades - King David, Clubs - Alexander the Great, Hearts - Charlemagne, and Diamonds - Julius Caesar.
```

### 21. Get Word Definitions

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

### 22. Get Words

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

result = await api.get_words(letter=None, word_type='capitalized', alphabetize=False)
print(result)
```

#### Expected Output

```text
name 'self' is not defined
```

### 23. Github Search

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
        "stargazers_count": 4835,
        "forks_count": 2825
    },
    {
        "name": "PokemonGo-Bot",
        "full_name": "PokemonGoF/PokemonGo-Bot",
        "description": "The Pokemon Go Bot, baking with community.",
        "url": "https://github.com/PokemonGoF/PokemonGo-Bot",
        "language": "Python",
        "stargazers_count": 3879,
        "forks_count": 1543
    }
]
```

### 24. Hindi Quote

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
हिचकिया मेरी गवाह है, नींदे उसकी भी तबाह है!
```

### 25. Hug

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

```json
[
    {
        "anime_name": "Karneval",
        "url": "https://nekos.best/api/v2/hug/76d225e6-6494-4c23-a4f8-9117afc5edf9.gif"
    }
]
```

### 26. Meme

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
https://preview.redd.it/ggrnni4sqg7e1.png?width=640&crop=smart&auto=webp&s=39fc3545f0ffa6fa49513a99a0821f15ca6065fa
```

### 27. Neko

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
            "artist_href": "https://twitter.com/mashiro_io",
            "artist_name": "\u771f\u767d\u3044\u304a",
            "source_url": "https://twitter.com/mashiro_io/status/1527242668182487041",
            "url": "https://nekos.best/api/v2/neko/00ea88fb-5439-4250-91b4-754d2c50b362.png"
        },
        {
            "artist_href": "https://www.pixiv.net/en/users/8886572",
            "artist_name": "nibosi",
            "source_url": "https://www.pixiv.net/en/artworks/95202859",
            "url": "https://nekos.best/api/v2/neko/baf1a187-a0fb-4aca-bc7f-923b5368f99e.png"
        },
        {
            "artist_href": "https://www.pixiv.net/en/users/29029591",
            "artist_name": "\u82b1\u7cf8Kashi",
            "source_url": "https://www.pixiv.net/en/artworks/79565443",
            "url": "https://nekos.best/api/v2/neko/86382615-776b-443a-b8be-7d0c7261485d.png"
        }
    ]
}
```

### 28. Pypi

**Description**:
Retrieves metadata information about a specified Python package from the PyPI API.

**Args:**
  - **package_name (str)**: The name of the package to search for on PyPI.

**Returns:**
  - **dict or None**: A dictionary with relevant package information if found, containing:
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

```python
from TheApi import api

result = await api.pypi(package_name='Pokemon')
print(result)
```

#### Expected Output

```json
{
    "name": "pokemon",
    "version": "0.36",
    "summary": "ascii database of pokemon... in Python!",
    "author": "Vanessa Sochat",
    "author_email": "vsoch@noreply.github.users.com",
    "license": "LICENSE",
    "home_page": "https://github.com/vsoch/pokemon",
    "package_url": "https://pypi.org/project/pokemon/",
    "requires_python": "",
    "keywords": "pokemon,avatar,ascii,gravatar",
    "classifiers": [],
    "project_urls": {
        "Homepage": "https://github.com/vsoch/pokemon"
    }
}
```

### 29. Quote

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
There is no duty we so underrate as the duty of being happy. By being happy we sow anonymous benefits upon the world.

author - Robert Louis Stevenson
```

### 30. Riddle

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

```json
{
    "riddle": "My thunder comes before the lightning; My lightning comes before the clouds; My rain dries all the land it touches. What am I?",
    "answer": "A volcano"
}
```

### 31. Stackoverflow Search

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
        "view_count": 32700,
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
        "view_count": 2033,
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

### 32. Upload Image

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


### 33. Wikipedia

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

### 34. Write

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
/home/runner/work/TheApi/TheApi/downloads/write_FWbntIoo.jpg
```


This Project is Licensed under [MIT License](https://github.com/Vivekkumar-IN/TheApi/blob/main/LICENSE)