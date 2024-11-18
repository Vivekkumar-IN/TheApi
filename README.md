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
| [2. Bing Image](#2-bing-image) | ✅
| [3. Blackpink](#3-blackpink) | ✅
| [4. Carbon](#4-carbon) | ✅
| [5. Cat](#5-cat) | ✅
| [6. Dog](#6-dog) | ✅
| [7. Domain Search](#7-domain-search) | ❌
| [8. Fox](#8-fox) | ✅
| [9. Gen Qr](#9-gen-qr) | ✅
| [10. Generate Pdf](#10-generate-pdf) | ✅
| [11. Get Advice](#11-get-advice) | ✅
| [12. Get Btc Value](#12-get-btc-value) | ✅
| [13. Get Hindi Jokes](#13-get-hindi-jokes) | ✅
| [14. Get Jokes](#14-get-jokes) | ✅
| [15. Get Uselessfact](#15-get-uselessfact) | ✅
| [16. Get Word Definitions](#16-get-word-definitions) | ✅
| [17. Github Search](#17-github-search) | ✅
| [18. Hindi Quote](#18-hindi-quote) | ✅
| [19. Hug](#19-hug) | ✅
| [20. Meme](#20-meme) | ✅
| [21. Neko](#21-neko) | ✅
| [22. Pypi](#22-pypi) | ✅
| [23. Quote](#23-quote) | ✅
| [24. Random Word](#24-random-word) | ✅
| [25. Riddle](#25-riddle) | ✅
| [26. Stackoverflow Search](#26-stackoverflow-search) | ✅
| [27. Upload Image](#27-upload-image) | ✅
| [28. Wikipedia](#28-wikipedia) | ✅
| [29. Words](#29-words) | ✅
| [30. Write](#30-write) | ✅


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
    "content": "After all.. love is all about timing. If you don't say the right thing at the right moment, no matter how much fate was involved in the relationship, everything will be ruined. Even if you regret it, it'll be too late.",
    "anime": {
        "id": 528,
        "name": "Bokura ga Ita"
    },
    "character": {
        "id": 1419,
        "name": "Masafumi Takeuchi"
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
https://media.gamestop.com/i/gamestop/11103360/New-Pokemon-Snap---Nintendo-Switch
https://img-eshop.cdn.nintendo.net/i/00bd7efe46ab2b3ff0774172a5d4f21a5b2f467b3e324557ce1e9a9ae12c1d3b.jpg
https://assets-prd.ignimgs.com/2021/03/01/new-pokemon-snap-button-1614639848584.jpg
https://www.gamespot.com/a/uploads/screen_kubrick/123/1239113/3801204-6238037227-screenshot02.jpg
https://www.nme.com/wp-content/uploads/2021/05/New-Pokemon-Snap-Credit-Bandai-Namco-HERO@2000x1270.jpg
https://www.rpgfan.com/wp-content/uploads/2021/01/New-Pokemon-Snap-Screenshot-044.jpg
https://www.videogamer.com/wp-content/uploads/01d7162d-749b-43eb-bdcc-5c0cf9e49881_New_Pokmon_Snap_Main.jpg
https://assets.nintendo.com/image/upload/c_fill,w_1200/q_auto:best/f_auto/dpr_2.0/ncom/en_US/products/games/switch/new-pokemon-snap/110735-switch-new-pokemon-snap-us-1200x675
https://images.launchbox-app.com/fc92b8c7-704f-43e9-ab5a-407b712bc662.jpg
https://i.ytimg.com/vi/e_V9nUUP2oo/maxresdefault.jpg
https://cdn.vox-cdn.com/thumbor/Lgiz7lrS_auxnKixNMsWmsx_ETE=/1400x788/filters:format(jpeg)/cdn.vox-cdn.com/uploads/chorus_asset/file/22473880/Switch_NewPokemonSnap_Screenshots_Feb26__9_.jpg
https://i.gadgets360cdn.com/products/large/New-Pokemon-Snap-Wallpaper-1440x2560-1000x1778-1646977124.jpg
https://twinfinite.net/wp-content/uploads/2021/04/New-Pokemon-Snap-scaled.jpg
https://i0.wp.com/mynintendonews.com/wp-content/uploads/2021/01/new_pokemon_snap_logo.jpg?ssl=1
https://assets.gamepur.com/wp-content/uploads/2021/01/14074110/new-pokemon-snap-arrives-on-nintendo-switch-this-april.jpg
https://webgames.host/uploads/2017/09/pokemon-snap.jpg
https://images.launchbox-app.com/1f06f096-8eb6-43ac-abbb-262deb1bf596.jpg
https://www.nintendo.com/sg/switch/arft/img/hero_sp.jpg
https://cdn.mobilesyrup.com/wp-content/uploads/2021/01/new-pokemon-snap-screenshot-2.jpg
https://videogamesuncovered.com/wp-content/uploads/2021/01/new-pokemon-snap-social.jpg
https://upload.wikimedia.org/wikipedia/commons/thumb/9/97/Pokemon_Type_Chart.svg/2048px-Pokemon_Type_Chart.svg.png
https://vignette.wikia.nocookie.net/pokemon/images/8/8c/PokemonTypes.png/revision/latest?cb=20170417193722
https://img.pokemondb.net/images/typechart.png
http://upload.wikimedia.org/wikipedia/commons/5/5e/Pokémon_types_(english).png
https://www.theloadout.com/wp-content/sites/theloadout/2023/06/pokemon-type-chart-icons.jpg
https://www.mandatory.gg/wp-content/uploads/mandatory-guide-pokemon-ecarlate-violet-table-types-forces-faiblesses.png
https://i.pinimg.com/originals/95/b2/6f/95b26f7cd39e206259faa20fd57e7b47.png
https://res.cloudinary.com/lmn/image/upload/e_sharpen:150,f_auto,fl_lossy,q_80/v1/gameskinnyc/p/o/k/pokemon-types-table-ad163.png
https://raw.githubusercontent.com/kennycason/cellular-automata-pokemon-types/master/data/pokemon_gen1_type_chart.png?raw=true
https://1.bp.blogspot.com/-A0NsVJu2Ay0/WGOgGNxAdTI/AAAAAAAABIY/amMTic8SsXYs7jfP_ITwBmkeVQHIAGZ-ACPcB/s1600/ENG-05-02-02-All-the-Pokemon-types.png
https://releasegaming.com/wp-content/uploads/2023/02/Pokemon-Type-Chart-Poster-960x850.jpg
http://fc09.deviantart.net/fs70/i/2013/318/0/f/pokemon_types_wheel_by_kamionero-d6u6o9i.png
https://orig00.deviantart.net/caf7/f/2014/046/7/2/pokemon_type_chart__offensive__by_lunicaura106-d76mcvb.png
https://cdn1.vectorstock.com/i/1000x1000/03/95/pokemon-type-symbols-vector-2700395.jpg
https://pnghq.com/wp-content/uploads/pnghq.com-pokemon-types-png-3908-download-1024x987.png
https://static.wikia.nocookie.net/pokemongo/images/9/9c/Type_chart.png/revision/latest?cb=20191205150508
https://videogamesuncovered.com/wp-content/uploads/2016/12/pokemon-types.jpg
https://metro.co.uk/wp-content/uploads/2016/07/01.jpg?quality=80&amp;strip=all
https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/7b386f5f-9a3f-497c-ad22-b2b574b05b37/dfkk1g6-bb82e195-fc59-410e-9d67-88283d33d704.png/v1/fill/w_1920,h_2148/original_pokemon_type_symbols_by_adeptcharon_dfkk1g6-fullview.png?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7ImhlaWdodCI6Ijw9MjE0OCIsInBhdGgiOiJcL2ZcLzdiMzg2ZjVmLTlhM2YtNDk3Yy1hZDIyLWIyYjU3NGIwNWIzN1wvZGZrazFnNi1iYjgyZTE5NS1mYzU5LTQxMGUtOWQ2Ny04ODI4M2QzM2Q3MDQucG5nIiwid2lkdGgiOiI8PTE5MjAifV1dLCJhdWQiOlsidXJuOnNlcnZpY2U6aW1hZ2Uub3BlcmF0aW9ucyJdfQ.EqLMXobU7LF7_CupNDFpDBYEvuGZEVc7HxZDt4y1LFA
https://i.imgur.com/bnV5eKv.png
https://i.etsystatic.com/21027128/r/il/fdbdba/2003255292/il_1588xN.2003255292_12o2.jpg
https://www.pokemoncenter.com/products/images/P2373PC/155-80156/P2373PC_155-80156_01.jpg
https://m.media-amazon.com/images/I/A1Ui8dsTSrS.jpg
https://i.etsystatic.com/23914535/r/il/750695/2869449405/il_1588xN.2869449405_fr75.jpg
https://www.hillscards.co.uk/images/pokemon-trading-card-game-xy-evolutions-4-sealed-booster-packs-xy-12-p2357-102135_image.jpg
https://cdn11.bigcommerce.com/s-0kvv9/images/stencil/2560w/products/175831/251398/pokemonshininglegends28__52193.1509648391.jpg?c=2
https://cdn11.bigcommerce.com/s-0kvv9/images/stencil/1920w/products/371952/569692/pokemonevolvingskies041__83278.1630015209.jpg?c=2
https://i.pinimg.com/736x/83/e3/5a/83e35aead31fabb77b9bde3396d4351f.jpg
https://www.totsafe.com/wp-content/uploads/2020/09/Gyarados-Ancient-Origins-Holo-1446x2048.jpg
https://i.etsystatic.com/22089514/r/il/ecff88/4140836231/il_1080xN.4140836231_cpmu.jpg
https://images.saymedia-content.com/.image/t_share/MTgzNzE1NDA2MDk0MDE3ODU1/best-vmax-pokemon-cards.png
https://i.etsystatic.com/22089514/r/il/c4b57e/2338029595/il_1140xN.2338029595_sei2.jpg
https://i.etsystatic.com/22089514/r/il/c9fa64/4093173358/il_1140xN.4093173358_jv87.jpg
https://images.saymedia-content.com/.image/t_share/MTc5ODE2MjE2Mjc2NDQ0Nzgz/best-v-pokemon-cards.jpg
https://i.pinimg.com/originals/18/28/97/18289747d16a23e3dc20cc36956b9b4b.jpg
https://imgix.ranker.com/user_node_img/3181/63618188/original/blastoise-u16?fit=crop&amp;fm=pjpg&amp;q=60&amp;w=650&amp;dpr=2
https://mlpnk72yciwc.i.optimole.com/cqhiHLc.WqA8~2eefa/w:auto/h:auto/q:75/https://bleedingcool.com/wp-content/uploads/2020/06/Charizard-grade-9-mint-front.jpg
https://pm1.narvii.com/6267/3e8dabe202aa4911724963a0eb1b1f0b0c875193_hq.jpg
https://i.etsystatic.com/24353291/r/il/358485/2689751041/il_fullxfull.2689751041_ofmo.jpg
https://cardmavin.com/wp-content/uploads/2016/11/pokemon-card.jpg
https://images5.alphacoders.com/130/thumb-1920-1308338.jpg
http://www.animextremist.com/imagenes/pokemon/pokemon103.jpg
http://www.animextremist.com/imagenes/pokemon/pokemon97.jpg
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
/home/runner/work/TheApi/TheApi/downloads/blackpink_7HzL1r7r.jpg
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
/home/runner/work/TheApi/TheApi/downloads/carbon_9XP0G6BO.png
```

### 5. Cat

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
https://cdn2.thecatapi.com/images/5n3.jpg
```

### 6. Dog

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
https://random.dog/5e0deefd-427f-478f-9d04-0103d8969d67.jpg
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
from Pokemon import api

result = await api.fox()
print(result)
```

#### Expected Output

```text
https://randomfox.ca/?i=112
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
/home/runner/work/TheApi/TheApi/downloads/Xft5QYk2_qr.png
```

### 10. Generate Pdf

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


### 11. Get Advice

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
You're not that important; it's what you do that counts.
```

### 12. Get Btc Value

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
        "rate": "87,051.196",
        "rate_float": 87051.196,
        "symbol": "&euro;"
    },
    "GBP": {
        "code": "GBP",
        "description": "British Pound Sterling",
        "rate": "72,616.604",
        "rate_float": 72616.6041,
        "symbol": "&pound;"
    },
    "USD": {
        "code": "USD",
        "description": "United States Dollar",
        "rate": "91,775.815",
        "rate_float": 91775.815,
        "symbol": "&#36;"
    }
}
```

### 13. Get Hindi Jokes

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
पति को बाजार जाते हुए देख पत्नी ने पैसे देकर कहा  कुछ ऐसी चीज़ लाना जिस से मैं सुन्दर दिखूं  👗👓💄👠🎀 पति खुद के लिए Whisky की दो बोतल ले आया। 😜😃
```

### 14. Get Jokes

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
I went to the zoo the other day. There was only a dog in it – it was a shihtzu.
```

### 15. Get Uselessfact

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
PEZ candy even comes in a Coffee flavor.
```

### 16. Get Word Definitions

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

### 17. Github Search

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
        "stargazers_count": 4797,
        "forks_count": 2799
    },
    {
        "name": "PokemonGo-Bot",
        "full_name": "PokemonGoF/PokemonGo-Bot",
        "description": "The Pokemon Go Bot, baking with community.",
        "url": "https://github.com/PokemonGoF/PokemonGo-Bot",
        "language": "Python",
        "stargazers_count": 3872,
        "forks_count": 1543
    }
]
```

### 18. Hindi Quote

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
फिर सामने हुस्न की मलिका हो या दुश्मन, सब अपने ही fan है”
```

### 19. Hug

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
        "anime_name": "Kamisama Hajimemashita",
        "url": "https://nekos.best/api/v2/hug/6729fa94-442a-4f75-bfae-4ab5ad644d39.gif"
    }
]
```

### 20. Meme

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
https://preview.redd.it/6xb7edebui1e1.png?width=1080&crop=smart&auto=webp&s=4566bd414f4c09c7b913ec0286b08cef77766aee
```

### 21. Neko

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
            "artist_href": "https://www.pixiv.net/en/users/3684923",
            "artist_name": "\u3072\u3085\u3089\u3055\u3093",
            "source_url": "https://www.pixiv.net/en/artworks/79697176",
            "url": "https://nekos.best/api/v2/neko/3daed3c4-152b-4e8b-aaf9-3b93d8fbb4b7.png"
        },
        {
            "artist_href": "https://www.pixiv.net/en/users/8159347",
            "artist_name": "\u30d5\u4e8c\u30a3",
            "source_url": "https://www.pixiv.net/en/artworks/83150105",
            "url": "https://nekos.best/api/v2/neko/cc9177ad-8224-4e94-a0c1-007caba531b8.png"
        },
        {
            "artist_href": "https://www.pixiv.net/en/users/5553495",
            "artist_name": "\u30e2\u30df\u30df",
            "source_url": "https://www.pixiv.net/en/artworks/101781166",
            "url": "https://nekos.best/api/v2/neko/f57e7256-1cef-4a12-b46e-ac1a104da040.png"
        }
    ]
}
```

### 22. Pypi

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

### 23. Quote

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
Ability is what you're capable of doing. Motivation determines what you do. Attitude determines how well you do it.

author - Lou Holtz
```

### 24. Random Word

**Description**:
Fetches a random word.

**Returns:**
  - **str**: A random word if available; "None" if an error occurs.

```python
from Pokemon import api

result = await api.random_word()
print(result)
```

#### Expected Output

```text
fillip
```

### 25. Riddle

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
    "riddle": "A man takes a barrel that weighs 20 pounds, and then puts something in it. It now weighs less than 20 pounds. What did he put in the barrel?",
    "answer": "Get a drill He put a hole in the barrel to make it weigh less"
}
```

### 26. Stackoverflow Search

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
        "view_count": 123,
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
        "view_count": 1974,
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
        "view_count": 32638,
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

### 27. Upload Image

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


### 28. Wikipedia

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

### 29. Words

**Description**:
Fetches a specified number of random words.

**Args:**
  - **num_words (int)**: The number of random words to retrieve.

**Returns:**
  - **list**: A list of random words if available; an empty list if no response is received.

```python
from TheApi import api

result = await api.words(num_words=2)
print(result)
```

#### Expected Output

```text
varnished
grits
```

### 30. Write

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
/home/runner/work/TheApi/TheApi/downloads/write_p99SWL2r.jpg
```


This Project is Licensed under [MIT License](https://github.com/Vivekkumar-IN/TheApi/blob/main/LICENSE)