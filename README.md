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
| [22. Get Words](#22-get-words) | ✅
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
    "content": "When you're hiding a secret from the whole world, it puts a weight on your shoulders.",
    "anime": {
        "id": 549,
        "name": "Kokoro Connect",
        "altName": "Kokoro Connect"
    },
    "character": {
        "id": 1187,
        "name": "Taichi Yaegashi"
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
    "file_name": "sally",
    "file_type": "image/jpeg",
    "file_url": "https://cofuvfbkdyfchroaxcvi.supabase.co/storage/v1/object/public/avatars/sally.jpg"
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
https://i.ytimg.com/vi/kJQGJS1A3Ww/maxresdefault.jpg
https://selphie1999gaming.com/wp-content/uploads/2021/04/New-Pokemon-Snap-Wall-2.jpg
https://poketouch.files.wordpress.com/2021/01/new_pokemon_snap_main_player_character_with_professor_mirror.png
https://www.nintendo-insider.com/wp-content/uploads/2021/05/new_pokemon_snap_review_screenshot_1.jpg
https://i.ytimg.com/vi/dYuNkNJUyeA/maxresdefault.jpg
https://www.pokemoncenter.com/images/DAMRoot/Full-Size/10000/P7967_716-59686_04.jpg
https://images.launchbox-app.com/13c88f8c-c89e-4a8a-9440-0b8b318c0656.png
https://www.vgfacts.com/media/boxart/1/519.png
https://www.fredzone.org/wp-content/uploads/2022/06/pokemon-snap.png
https://media.wired.com/photos/608b3b24e749509a585173ba/1:1/w_1080,h_1080,c_limit/games_pokemon-snap.jpg
https://www.speedrun.com/static/game/j1lqqj6g/cover.png?v=e37621d
https://static0.gamerantimages.com/wordpress/wp-content/uploads/2022/10/New-Pokemon-Snap.jpg
https://thirdpersonblog.files.wordpress.com/2021/02/pokemon-snap-pikachu.jpg
https://cdn.mos.cms.futurecdn.net/UzF4GbdrS4wWAyTBf2MsvH.jpg
https://s31092.pcdn.co/wp-content/uploads/2022/06/Pokemon-Snap-00-1320x743.jpg
https://images.nintendolife.com/83ea7826f3df6/new-pokemon-snap.large.jpg
https://as01.epimg.net/meristation/imagenes/2021/08/04/noticias/1628066475_409388_1628066698_portada_normal.jpg
https://assets.pokemon.com/assets/cms2/img/video-games/video-games/pokemon_snap/pokemon-snap-december-update-169.jpg
https://static1.thegamerimages.com/wordpress/wp-content/uploads/2021/12/New-Pokemon-Snap-Complete-Guide.jpg
https://cdn.mos.cms.futurecdn.net/9QoXnCMCXRxhWrzD5hECFD-1200-80.jpg
https://i.pinimg.com/originals/03/74/d1/0374d1f4d1adeee44cab9fc4a3322624.jpg
https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/4533470f-692e-4f8c-afd0-2bcb90c6eda0/d5i3e0k-a37a922d-439b-4082-add5-da001d10ddbb.png?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7InBhdGgiOiJcL2ZcLzQ1MzM0NzBmLTY5MmUtNGY4Yy1hZmQwLTJiY2I5MGM2ZWRhMFwvZDVpM2Uway1hMzdhOTIyZC00MzliLTQwODItYWRkNS1kYTAwMWQxMGRkYmIucG5nIn1dXSwiYXVkIjpbInVybjpzZXJ2aWNlOmZpbGUuZG93bmxvYWQiXX0.mPFq-dr0f2AXiHq1exP-gCh1Z09fMKhmW0eRKwpbOec
https://4.bp.blogspot.com/-VIHqrKz_dOo/VwhxKVhLqyI/AAAAAAAAGGU/TLEPIcT_V_0dJco6r2uUhrAOJc5-NdhaA/s1600/151%2BPokemon.png
https://pnghq.com/wp-content/uploads/pnghq.com-pokemon-types-321x400.png
https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/2142bea7-aad9-4fb5-b160-b94f39ddb6f7/d61pavo-522f70e2-1ef9-417e-9034-033e34a808cf.png?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7InBhdGgiOiJcL2ZcLzIxNDJiZWE3LWFhZDktNGZiNS1iMTYwLWI5NGYzOWRkYjZmN1wvZDYxcGF2by01MjJmNzBlMi0xZWY5LTQxN2UtOTAzNC0wMzNlMzRhODA4Y2YucG5nIn1dXSwiYXVkIjpbInVybjpzZXJ2aWNlOmZpbGUuZG93bmxvYWQiXX0.Wn6SG8_fJPE9WGctYsd8WjMa7XzYErPikYDhn_ixW_Q
http://thewonderfulworldofpokemon.weebly.com/uploads/1/5/2/9/15296782/5322676.png?522
https://i.ytimg.com/vi/4651Wp3SOOI/maxresdefault.jpg
https://i.imgur.com/ktnGV4O.jpg
https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/dc175766-6e5d-4e29-a6c5-ecc6a37db16a/d8vkfwp-b481a558-5c32-44b6-b4d0-df9f1e8ed8f1.png/v1/fill/w_977,h_818,q_70,strp/illustrated_pokemon_type_chart_by_jojostory_d8vkfwp-pre.jpg?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7ImhlaWdodCI6Ijw9MTM0MCIsInBhdGgiOiJcL2ZcL2RjMTc1NzY2LTZlNWQtNGUyOS1hNmM1LWVjYzZhMzdkYjE2YVwvZDh2a2Z3cC1iNDgxYTU1OC01YzMyLTQ0YjYtYjRkMC1kZjlmMWU4ZWQ4ZjEucG5nIiwid2lkdGgiOiI8PTE2MDAifV1dLCJhdWQiOlsidXJuOnNlcnZpY2U6aW1hZ2Uub3BlcmF0aW9ucyJdfQ.7rruD0XfA3p4nDeOv404ZBC2Wl_QB2hCOO0xsTdi1R0
https://i.pinimg.com/originals/76/85/aa/7685aa1ec874b44788de1edd91b14dc2.jpg
https://static0.srcdn.com/wordpress/wp-content/uploads/2021/04/Pokemon-Weaknesses-Explained.png
https://metro.co.uk/wp-content/uploads/2016/07/18.jpg?quality=80&amp;strip=all
https://upload.wikimedia.org/wikipedia/commons/5/5e/Pokémon_types_(english).png
https://i.redd.it/85g3dnq914h91.png
https://i.redd.it/40pq92pf63tb1.png
https://www.typecalendar.com/wp-content/uploads/2023/09/Free-Download-Pokemon-Type-Chart.jpg
https://i2.wp.com/pokemongymwalkthrough.weebly.com/uploads/2/4/9/0/24904210/5318426.png?902
https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/0726fbdd-a6a6-4871-bed6-e8e0b9ce2af0/da2u6to-feebac03-0e08-46e3-8237-1a054ed64723.png/v1/fill/w_1000,h_550,q_80,strp/22_pokemon_type_symbols_by_maskadra42_da2u6to-fullview.jpg?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7ImhlaWdodCI6Ijw9NTUwIiwicGF0aCI6IlwvZlwvMDcyNmZiZGQtYTZhNi00ODcxLWJlZDYtZThlMGI5Y2UyYWYwXC9kYTJ1NnRvLWZlZWJhYzAzLTBlMDgtNDZlMy04MjM3LTFhMDU0ZWQ2NDcyMy5wbmciLCJ3aWR0aCI6Ijw9MTAwMCJ9XV0sImF1ZCI6WyJ1cm46c2VydmljZTppbWFnZS5vcGVyYXRpb25zIl19.wkZllLshskbwMxQqiCsgsUwTkDMm3FJxhBbTvQ0-cqg
https://i.pinimg.com/originals/e5/9d/9f/e59d9ff9f8d9b4828a8e479411b91d16.png
https://i.imgur.com/HkW6weP.png
https://i.pinimg.com/originals/18/28/97/18289747d16a23e3dc20cc36956b9b4b.jpg
https://images.saymedia-content.com/.image/t_share/MTc5ODE2MjE2Mjc2NDQ0Nzgz/best-v-pokemon-cards.jpg
https://mlpnk72yciwc.i.optimole.com/cqhiHLc.WqA8~2eefa/w:auto/h:auto/q:75/https://bleedingcool.com/wp-content/uploads/2020/06/Charizard-grade-9-mint-front.jpg
https://m.media-amazon.com/images/I/A1Ui8dsTSrS.jpg
https://images.saymedia-content.com/.image/t_share/MTgzNzE1NDA2MDk0MDE3ODU1/best-vmax-pokemon-cards.png
https://i.pinimg.com/736x/83/e3/5a/83e35aead31fabb77b9bde3396d4351f.jpg
https://www.pokemoncenter.com/products/images/P2373PC/155-80156/P2373PC_155-80156_01.jpg
https://i.etsystatic.com/23914535/r/il/750695/2869449405/il_1588xN.2869449405_fr75.jpg
https://pm1.narvii.com/6267/3e8dabe202aa4911724963a0eb1b1f0b0c875193_hq.jpg
https://i.etsystatic.com/21027128/r/il/fdbdba/2003255292/il_1588xN.2003255292_12o2.jpg
https://www.totsafe.com/wp-content/uploads/2020/09/Gyarados-Ancient-Origins-Holo-1446x2048.jpg
https://i2.wp.com/nypost.com/wp-content/uploads/sites/2/2020/12/pokemon-auction.jpg?quality=90&amp;strip=all&amp;ssl=1
https://miro.medium.com/max/1400/1*I9DUHexc5eoKn1-dZs4g0A.jpeg
https://cdn11.bigcommerce.com/s-0kvv9/images/stencil/1920w/products/371952/569692/pokemonevolvingskies041__83278.1630015209.jpg?c=2
https://i.etsystatic.com/24353291/r/il/358485/2689751041/il_fullxfull.2689751041_ofmo.jpg
https://m.media-amazon.com/images/I/91lXJ99OooL.jpg
https://i.pinimg.com/originals/d1/a5/fc/d1a5fc45abdf217f2ee641bb4975fa32.png
https://www.oldsportscards.com/wp-content/uploads/2019/12/Most-Valuable-First-Edition-Pokemon-Cards.jpg
https://www.printablee.com/postpic/2013/12/rare-pokemon-cards-printable_23336.jpg
https://www.printablee.com/postpic/2014/04/rare-pokemon-cards-printable_23606.jpg
https://townsquare.media/site/622/files/2016/08/poke-feat.jpg?w=1200&amp;h=0&amp;zc=1&amp;s=0&amp;a=t&amp;q=89
https://upload.wikimedia.org/wikipedia/en/thumb/9/9e/150_Pokemon_from_Pokemon_Stadium.png/330px-150_Pokemon_from_Pokemon_Stadium.png
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
/home/runner/work/TheApi/TheApi/downloads/blackpink_PxwEQktR.jpg
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
/home/runner/work/TheApi/TheApi/downloads/carbon_TLzD5jNr.png
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
https://cdn2.thecatapi.com/images/MTgzMzkzNQ.jpg
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
https://random.dog/92636626-a00d-4ac7-8f39-c15524f5d810.mp4
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
quantity (int, optional): Number of rows to fetch (default: 3, max: 1000). locale (str, optional): Locale for the data (default: 'en_US').  [ See Valid locale ](https://fakerapi.it/#params_locale)

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
https://randomfox.ca/?i=88
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
/home/runner/work/TheApi/TheApi/downloads/Z9P5vEt4_qr.png
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
You can have too much of a good thing.
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
        "rate": "92,222.266",
        "rate_float": 92222.2655,
        "symbol": "&euro;"
    },
    "GBP": {
        "code": "GBP",
        "description": "British Pound Sterling",
        "rate": "76,660.033",
        "rate_float": 76660.0328,
        "symbol": "&pound;"
    },
    "USD": {
        "code": "USD",
        "description": "United States Dollar",
        "rate": "96,127.844",
        "rate_float": 96127.8437,
        "symbol": "&#36;"
    }
}
```

### 15. Get Fake Addresses

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
            "street": "85946 Volkman Isle",
            "streetName": "Joey Grove",
            "buildingNumber": "755",
            "city": "Lake Ianborough",
            "zipcode": "85706",
            "country": "Sierra Leone",
            "country_code": "SL",
            "latitude": 73.299008,
            "longitude": -13.864332
        }
    ]
}
```

### 16. Get Fake Credit Cards

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
            "type": "Visa",
            "number": "4916436343907011",
            "expiration": "09/27",
            "owner": "Maverick Rempel"
        }
    ]
}
```

### 17. Get Fake Images

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
            "title": "Aut quo nam voluptatem quasi.",
            "description": "Quia nihil reprehenderit adipisci quam maxime temporibus. Ratione qui est ea repellendus eveniet. Similique possimus quisquam quia minus.",
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
हम मध्यम वर्ग वाले धनतेरस के दिन झाड़ू और बर्तन खरीदने के बाद मन मे ये सोचते है कि ...अगले साल गाड़ी घोड़ा जरूर खरीदेंगें ...
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
I'm reading a book about anti-gravity. It's impossible to put down!
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
It has NEVER rained in Calama, a town in the Atacama Desert of Chile.
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

result = await api.get_words(words=10, letter=None, word_type='capitalized', alphabetize=False)
print(result)
```

#### Expected Output

```text
Transpire
Unsure
Curled
Twiddle
Dancing
Napping
Puma
Ivy
Tweezers
Tacky
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
        "stargazers_count": 7526,
        "forks_count": 2815
    },
    {
        "name": "pokemon-showdown",
        "full_name": "smogon/pokemon-showdown",
        "description": "Pok\u00e9mon battle simulator.",
        "url": "https://github.com/smogon/pokemon-showdown",
        "language": "TypeScript",
        "stargazers_count": 4838,
        "forks_count": 2828
    },
    {
        "name": "PokemonGo-Bot",
        "full_name": "PokemonGoF/PokemonGo-Bot",
        "description": "The Pokemon Go Bot, baking with community.",
        "url": "https://github.com/PokemonGoF/PokemonGo-Bot",
        "language": "Python",
        "stargazers_count": 3880,
        "forks_count": 1542
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
हम मोहब्बत में no.1 तो attitude में star है…
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
        "anime_name": "Sword Art Online",
        "url": "https://nekos.best/api/v2/hug/f33d03b0-fb25-4592-b48c-4de029596488.gif"
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
https://preview.redd.it/zcgd57k8n59e1.gif?width=320&crop=smart&format=png8&s=74e0c735ee639681511bf300ab1bd0169edf4989
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
            "artist_href": "https://twitter.com/habanero_mgmg",
            "artist_name": "habanero_mgmg",
            "source_url": "https://twitter.com/i/web/status/1286244046315241473",
            "url": "https://nekos.best/api/v2/neko/ab179db6-9eb6-489f-aa63-7b2c2cc643fb.png"
        },
        {
            "artist_href": "https://www.pixiv.net/en/users/8861015",
            "artist_name": "\u304f\u307e\u306e\u305d\u3089",
            "source_url": "https://www.pixiv.net/en/artworks/97655458",
            "url": "https://nekos.best/api/v2/neko/ec9554a0-5682-4997-ad8a-659e335b4321.png"
        },
        {
            "artist_href": "https://www.pixiv.net/en/users/38436050",
            "artist_name": "\u3086\u304d\u3046\u306a\u304e",
            "source_url": "https://www.pixiv.net/en/artworks/81115452",
            "url": "https://nekos.best/api/v2/neko/d780dca1-8a98-4c79-93a3-de2d8647191b.png"
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
We never understand how little we need in this world until we know the loss of it.

author - J. M. Barrie
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
    "riddle": "What can bring back the dead; make us cry, make us laugh, make us young; born in an instant yet lasts a life time?",
    "answer": "Memories"
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
        "view_count": 32707,
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
        "view_count": 2039,
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
    "summary": "Pok\u00e9mon is a Japanese media franchise consisting of video games, animated series and films, a trading card game, and other related media. The franchise takes place in a shared universe in which humans co-exist with creatures known as Pok\u00e9mon, a large variety of species endowed with special powers. The franchise's primary target audience is children aged 5 to 12, but it is known to attract people of all ages.\nThe franchise originated as a pair of role-playing games developed by Game Freak, from an original concept by its founder, Satoshi Tajiri. Released on the Game Boy on February 27, 1996, the games became sleeper hits and were followed by manga series, a trading card game, and anime series and films. From 1998 to 2000, Pok\u00e9mon was exported to the rest of the world, creating an unprecedented global phenomenon dubbed \"Pok\u00e9mania\". By 2002, the craze had ended, after which Pok\u00e9mon became a fixture in popular culture, with new products being released to this day. In the summer of 2016, the franchise spawned a second craze with the release of Pok\u00e9mon Go, an augmented reality game developed by Niantic. Pok\u00e9mon has since been estimated to be the world's highest-grossing media franchise and one of the best-selling video game franchises.\nPok\u00e9mon has an uncommon ownership structure. Unlike most IPs, which are owned by one company, Pok\u00e9mon is jointly owned by three: Nintendo, Game Freak, and Creatures. Game Freak develops the core series role-playing games, which are published by Nintendo exclusively for their consoles, while Creatures manages the trading card game and related merchandise, occasionally developing spin-off titles. The three companies established The Pok\u00e9mon Company (TPC) in 1998 to manage the Pok\u00e9mon property within Asia. The Pok\u00e9mon anime series and films are co-owned by Shogakukan. Since 2009, The Pok\u00e9mon Company International (TPCi), a subsidiary of TPC, has managed the franchise in all regions outside of Asia.\n\n",
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
/home/runner/work/TheApi/TheApi/downloads/write_EjRJU8bW.jpg
```


This Project is Licensed under [MIT License](https://github.com/Vivekkumar-IN/TheApi/blob/main/LICENSE)