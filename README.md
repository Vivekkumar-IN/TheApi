##### Installation

```sh
pip install https://github.com/Vivekkumar-IN/TheApi/archive/refs/heads/main.zip
```

---

# 📘 API Documentation

Welcome to the **TheApi**! This library allows you to easily interact with the API using **asynchronous** options.

- **Async**: `from TheApi import api`

Below, we’ll cover each function, providing examples and expected results so you can get started quickly! Let’s dive in 🚀

## Status

| Function           | Status |
|--------------------|--------|
| [1. Animechan](#1-animechan) | ✅
| [2. Bing Image](#2-bing-image) | ✅
| [3. Blackpink](#3-blackpink) | ✅
| [4. Carbon](#4-carbon) | ✅
| [5. Cat](#5-cat) | ✅
| [6. Dog](#6-dog) | ✅
| [7. Domain Search](#7-domain-search) | ❌
| [8. Fox](#8-fox) | ✅
| [9. Gen Qr](#9-gen-qr) | ✅
| [10. Get Advice](#10-get-advice) | ✅
| [11. Get Hindi Jokes](#11-get-hindi-jokes) | ✅
| [12. Get Jokes](#12-get-jokes) | ✅
| [13. Get Uselessfact](#13-get-uselessfact) | ✅
| [14. Get Word Definitions](#14-get-word-definitions) | ❌
| [15. Github Search](#15-github-search) | ✅
| [16. Hindi Quote](#16-hindi-quote) | ✅
| [17. Hug](#17-hug) | ✅
| [18. Meme](#18-meme) | ✅
| [19. Neko](#19-neko) | ✅
| [20. Pypi](#20-pypi) | ✅
| [21. Quote](#21-quote) | ✅
| [22. Random Word](#22-random-word) | ✅
| [23. Riddle](#23-riddle) | ✅
| [24. Stackoverflow Search](#24-stackoverflow-search) | ✅
| [25. Upload Image](#25-upload-image) | ✅
| [26. Wikipedia](#26-wikipedia) | ✅
| [27. Words](#27-words) | ✅
| [28. Write](#28-write) | ✅


## 🎓 How to Use Each Function

### 1. Animechan

**Description**:
Fetches a random anime quote from the AnimeChan API.

**Returns:**
  - **dict**: Contains the quote content, anime name, and character details.

```python
from TheApi import api

result = await api.animechan()
print(result)
```

#### Expected Output

```json
{
    "content": "Doesn't it ever get boring always being on the winning side?",
    "anime": {
        "id": 200,
        "name": "Vinland Saga"
    },
    "character": {
        "id": 227,
        "name": "Thorkell"
    }
}
```

### 2. Bing Image

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
https://static3.cbrimages.com/wordpress/wp-content/uploads/2019/09/Pokemon-Ash-Feature-Image-1.jpg
https://images5.alphacoders.com/130/thumb-1920-1308338.jpg
http://www.animextremist.com/imagenes/pokemon/pokemon103.jpg
```

### 3. Blackpink

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
/home/runner/work/TheApi/TheApi/downloads/blackpink_4THdp6FJ.jpg
```

### 4. Carbon

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
/home/runner/work/TheApi/TheApi/downloads/carbon_hSeloFJT.png
```

### 5. Cat

**Description**:
Fetches a random cat image URL.

**Returns:**
  - **str or None**: The URL of a random cat image if available; None if no response is received.

```python
from TheApi import api

result = await api.cat()
print(result)
```

#### Expected Output

```text
https://cdn2.thecatapi.com/images/OfIuuOv07.jpg
```

### 6. Dog

**Description**:
Fetches a random dog image URL.

**Returns:**
  - **str or None**: The URL of a random dog image if available; None if no response is received.

```python
from TheApi import api

result = await api.dog()
print(result)
```

#### Expected Output

```text
https://random.dog/452f58b8-084a-4262-b43f-768768a878db.JPG
```

### 7. Domain Search

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
Request failed: 524, message='', url='https://api.domainsdb.info/v1/domains/search?domain=Pokemon&zone=com'
```

### 8. Fox

**Description**:
Fetches a random fox image URL.

**Returns:**
  - **str or None**: The URL of the fox image if available, otherwise None.

```python
from TheApi import api

result = await api.fox()
print(result)
```

#### Expected Output

```text
https://randomfox.ca/?i=66
```

### 9. Gen Qr

**Description**:
Generates a QR code and saves it to the specified file path.

**Args:**
  - **query (str)**: The data to encode in the QR code.
  - **file_path (str, optional)**: The file path to save the QR code.
    Defaults to "downloads/{random_str}_qr.png".

**Returns:**
  - **FilePath**: The file path where the QR code was saved.

```python
from TheApi import api

result = await api.gen_qr(query='Pokemon', file_path=None)
print(result)
```

#### Expected Output

```text
/home/runner/work/TheApi/TheApi/downloads/htMEmdPB_qr.png
```

### 10. Get Advice

**Description**:
Fetches a random piece of advice.

**Returns:**
  - **str**: A random advice message.

```python
from TheApi import api

result = await api.get_advice()
print(result)
```

#### Expected Output

```text
Pedantry is fine, unless you're on the receiving end. And not a pedant.
```

### 11. Get Hindi Jokes

**Description**:
Fetches a random Hindi joke.

**Returns:**
  - **str**: A random Hindi joke if available, or "No joke found" if not available.

```python
from TheApi import api

result = await api.get_hindi_jokes()
print(result)
```

#### Expected Output

```text
लड़के किसी भी ऐप में लड़कियों से बात कर सकते है... मगर इनकी आत्मा को शांति WhatsApp number मांग कर ही मिलती है...... 
```

### 12. Get Jokes

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
I have a joke about Stack Overflow, but you would say it's a duplicate.
```

### 13. Get Uselessfact

**Description**:
Fetches a random useless fact.

**Returns:**
  - **str**: A random useless fact.

```python
from TheApi import api

result = await api.get_uselessfact()
print(result)
```

#### Expected Output

```text
A family of 26 could go to the movies in Mexico city for the price of one in Tokyo.
```

### 14. Get Word Definitions

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

```text
Request failed: 404, message='Not Found', url='https://api.dictionaryapi.dev/api/v2/entries/en/Pokemon'
```

### 15. Github Search

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
        "stargazers_count": 7529,
        "forks_count": 2815
    },
    {
        "name": "pokemon-showdown",
        "full_name": "smogon/pokemon-showdown",
        "description": "Pok\u00e9mon battle simulator.",
        "url": "https://github.com/smogon/pokemon-showdown",
        "language": "TypeScript",
        "stargazers_count": 4796,
        "forks_count": 2798
    },
    {
        "name": "PokemonGo-Bot",
        "full_name": "PokemonGoF/PokemonGo-Bot",
        "description": "The Pokemon Go Bot, baking with community.",
        "url": "https://github.com/PokemonGoF/PokemonGo-Bot",
        "language": "Python",
        "stargazers_count": 3871,
        "forks_count": 1543
    }
]
```

### 16. Hindi Quote

**Description**:
Fetches a random Hindi quote.

**Returns:**
  - **str**: The content of a random Hindi quote.

```python
from TheApi import api

result = await api.hindi_quote()
print(result)
```

#### Expected Output

```text
थोड़ा डुबूंगा, मगर मैं फिर तैर आऊंगा, ऐ ज़िंदगी, तू देख, मैं फिर जीत जाऊंगा…
```

### 17. Hug

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
        "anime_name": "Darling in the Franxx",
        "url": "https://nekos.best/api/v2/hug/f6861773-08f0-4410-82cd-431711b2e2de.gif"
    }
]
```

### 18. Meme

**Description**:
Fetches a random meme image URL.

**Returns:**
  - **str or None**: The URL of the meme image if available, otherwise None.

```python
from TheApi import api

result = await api.meme()
print(result)
```

#### Expected Output

```text
https://preview.redd.it/t9zfnkbhn91e1.gif?width=640&crop=smart&format=png8&s=869e7fc28b2ac8813f4454d1f9e881e738300669
```

### 19. Neko

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
            "artist_href": "https://www.pixiv.net/en/users/68506692",
            "artist_name": "OwO",
            "source_url": "https://www.pixiv.net/en/artworks/90120431",
            "url": "https://nekos.best/api/v2/neko/625f5be7-2e13-4391-ad25-67fd9a42ac49.png"
        },
        {
            "artist_href": "https://www.pixiv.net/en/users/12173021",
            "artist_name": "\u30d5\u30a3\u30a2",
            "source_url": "https://www.pixiv.net/en/artworks/99453834",
            "url": "https://nekos.best/api/v2/neko/43ab7ed5-7630-4ea1-ba38-e1d1da8e6fd1.png"
        },
        {
            "artist_href": "https://www.pixiv.net/en/users/3163457",
            "artist_name": "\u308a\u3087\u3046\u305f\u3093",
            "source_url": "https://www.pixiv.net/en/artworks/75707226",
            "url": "https://nekos.best/api/v2/neko/95180e93-e7ae-4659-b9ea-1020d757045b.png"
        }
    ]
}
```

### 20. Pypi

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

### 21. Quote

**Description**:
Fetches a random quote.

**Returns:**
  - **str**: The content of a random quote followed by the author's name.

```python
from TheApi import api

result = await api.quote()
print(result)
```

#### Expected Output

```text
If we learn to open our hearts, anyone, including the people who drive us crazy, can be our teacher.

author - Pema Chödrön
```

### 22. Random Word

**Description**:
Fetches a random word.

**Returns:**
  - **str**: A random word if available; "None" if an error occurs.

```python
from TheApi import api

result = await api.random_word()
print(result)
```

#### Expected Output

```text
ampersands
```

### 23. Riddle

**Description**:
Fetches a random riddle from the Riddles API.

**Returns:**
  - **dict**: The riddle data in JSON format.

```python
from TheApi import api

result = await api.riddle()
print(result)
```

#### Expected Output

```json
{
    "riddle": "They can trickle down, They can tickle too. Or make you sneeze, Or comfort you. Their rustling sound, you've rarely heard, Unless you're a pillow or a bird!  What are they?",
    "answer": "They are feathers"
}
```

### 24. Stackoverflow Search

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
        "view_count": 117,
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
        "view_count": 1971,
        "answer_count": 2,
        "score": 0,
        "last_activity_date": 1652730812,
        "creation_date": 1642222168,
        "last_edit_date": 1642223800,
        "question_id": 70718940,
        "content_license": "CC BY-SA 4.0",
        "link": "https://stackoverflow.com/questions/70718940/pokemon-api-request-generate-5-pok%c3%a9mon-at-a-time",
        "title": "Pokemon API request generate 5 Pok&#233;mon at a time"
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
        "view_count": 32634,
        "accepted_answer_id": 7942409,
        "answer_count": 3,
        "score": 3,
        "last_activity_date": 1577442848,
        "creation_date": 1319931614,
        "question_id": 7942384,
        "content_license": "CC BY-SA 3.0",
        "link": "https://stackoverflow.com/questions/7942384/simple-java-pokemon-fight-simulator",
        "title": "Simple Java Pokemon Fight Simulator"
    }
]
```

### 25. Upload Image

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

```python
from TheApi import api

result = await api.upload_image(file_path='file/to/upload')
print(result)
```

#### Expected Output

```text
You will get a URL
```

### 26. Wikipedia

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
    "summary": "Pok\u00e9mon is a Japanese media franchise consisting of video games, animated series and films, a trading card game, and other related media. The franchise takes place in a shared universe in which humans co-exist with creatures known as Pok\u00e9mon, a large variety of species endowed with special powers. The franchise's target audience is children aged 5 to 12, but it is known to attract people of all ages.\nThe franchise originated as a pair of role-playing games developed by Game Freak, from an original concept by its founder, Satoshi Tajiri. Released on the Game Boy on February 27, 1996, the games became sleeper hits and were followed by manga series, a trading card game, and anime series and films. From 1998 to 2000, Pok\u00e9mon was exported to the rest of the world, creating an unprecedented global phenomenon dubbed \"Pok\u00e9mania\". By 2002, the craze had ended, after which Pok\u00e9mon became a fixture in popular culture, with new products being released to this day. In the summer of 2016, the franchise spawned a second craze with the release of Pok\u00e9mon Go, an augmented reality game developed by Niantic. Pok\u00e9mon has since been estimated to be the world's highest-grossing media franchise and one of the best-selling video game franchises.\nPok\u00e9mon has an uncommon ownership structure. Unlike most IPs, which are owned by one company, Pok\u00e9mon is jointly owned by three: Nintendo, Game Freak, and Creatures. Game Freak develops the core series role-playing games, which are published by Nintendo exclusively for their consoles, while Creatures manages the trading card game and related merchandise, occasionally developing spin-off titles. The three companies established The Pok\u00e9mon Company (TPC) in 1998 to manage the Pok\u00e9mon property within Asia. The Pok\u00e9mon anime series and films are co-owned by Shogakukan. Since 2009, The Pok\u00e9mon Company International (TPCi), a subsidiary of TPC, has managed the franchise in all regions outside of Asia.\n\n",
    "url": "https://en.wikipedia.org/?curid=23745",
    "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/9/98/International_Pok%C3%A9mon_logo.svg/500px-International_Pok%C3%A9mon_logo.svg.png"
}
```

### 27. Words

**Description**:
Fetches a specified number of random words.

**Args:**
  - **num_words (int)**: The number of random words to retrieve.

**Returns:**
  - **list**: A list of random words if available; an empty list if no response is received.

```python
from TheApi import api

result = await api.words(num_words=5)
print(result)
```

#### Expected Output

```text
publicity
shooing
prepaste
outpoll
unpack
```

### 28. Write

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
/home/runner/work/TheApi/TheApi/downloads/write_ovJM3L3T.jpg
```


This Project is Licensed under [MIT License](https://github.com/Vivekkumar-IN/TheApi/blob/main/LICENSE)