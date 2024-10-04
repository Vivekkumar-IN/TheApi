##### Installation

```sh
pip install git+https://github.com/Vivekkumar-IN/TheApi@main
```

---

# API Documentation

This document provides a list of all functions in `TheApi`, along with their status and usage examples.

## Function List

1. [bing_image](#bing_image)
2. [blackpink](#blackpink)
3. [carbon](#carbon)
4. [cat](#cat)
5. [chatgpt](#chatgpt)
6. [dog](#dog)
7. [fox](#fox)
8. [gen_hashtag](#gen_hashtag)
9. [get_advice](#get_advice)
10. [get_hindi_jokes](#get_hindi_jokes)
11. [get_jokes](#get_jokes)
12. [get_uselessfact](#get_uselessfact)
13. [github_search](#github_search)
14. [hindi_quote](#hindi_quote)
15. [meme](#meme)
16. [morse_code](#morse_code)
17. [pypi](#pypi)
18. [quote](#quote)
19. [randomword](#randomword)
20. [riddle](#riddle)
21. [stackoverflow_search](#stackoverflow_search)
22. [upload_image](#upload_image)
23. [wikipedia](#wikipedia)
24. [words](#words)
25. [write](#write)

## API Status

| Function Name | Status |
|---------------|--------|
| [bing_image](#bing_image) | ✅ |
| [blackpink](#blackpink) | ✅ |
| [carbon](#carbon) | ✅ |
| [cat](#cat) | ✅ |
| [chatgpt](#chatgpt) | ✅ |
| [dog](#dog) | ✅ |
| [fox](#fox) | ✅ |
| [gen_hashtag](#gen_hashtag) | ✅ |
| [get_advice](#get_advice) | ✅ |
| [get_hindi_jokes](#get_hindi_jokes) | ✅ |
| [get_jokes](#get_jokes) | ✅ |
| [get_uselessfact](#get_uselessfact) | ✅ |
| [github_search](#github_search) | ✅ |
| [hindi_quote](#hindi_quote) | ✅ |
| [meme](#meme) | ✅ |
| [morse_code](#morse_code) | ✅ |
| [pypi](#pypi) | ✅ |
| [quote](#quote) | ✅ |
| [randomword](#randomword) | ✅ |
| [riddle](#riddle) | ✅ |
| [stackoverflow_search](#stackoverflow_search) | ✅ |
| [upload_image](#upload_image) | ✅ |
| [wikipedia](#wikipedia) | ✅ |
| [words](#words) | ✅ |
| [write](#write) | ✅ |

## Code Usage and Results:

### bing_image

```python
# Usage:
from TheApi import api

result = api.bing_image(query='pokemon', limit=3)
print(result)
```

```text
# Result:
['https://nintendoeverything.com/wp-content/uploads/Rockruff_jpg_jpgcopy.jpg', 'http://www.animextremist.com/imagenes/pokemon/pokemon103.jpg', 'https://upload.wikimedia.org/wikipedia/commons/thumb/9/98/International_Pokémon_logo.svg/1200px-International_Pokémon_logo.svg.png']
```

### blackpink

```python
# Usage:
from TheApi import api

result = api.blackpink(args='pokemon', color='#ff94e0', border_color=None)
print(result)
```

```text
# Result:
https://envs.sh/0Ql.jpg
```

### carbon

```python
# Usage:
from TheApi import api

result = api.carbon(query='pokemon')
print(result)
```

```text
# Result:
https://envs.sh/0Qk.png
```

### cat

```python
from TheApi import api

result = api.cat()
print(result)
```

```text
https://cdn2.thecatapi.com/images/adh.jpg
```

### chatgpt

```python
# Usage:
from TheApi import api

result = api.chatgpt(query='pokemon')
print(result)
```

```text
# Result:
**Pokémon** (ポケットモンスター Poketto Monsutā) is a media franchise created by Satoshi Tajiri and Ken Sugimori. The franchise began as a pair of video games for the Game Boy in 1996 and has since expanded to include video games, anime, trading cards, toys, and other merchandise.

The Pokémon video games revolve around the player's quest to become a Pokémon Master by capturing, training, and battling Pokémon. There are over 900 different Pokémon species, each with its own unique type and abilities. The games have been released on a variety of Nintendo platforms, including the Game Boy, Nintendo DS, and Nintendo Switch.

The Pokémon anime is an animated television series that follows the adventures of Ash Ketchum, a young Pokémon trainer from Pallet Town. The anime has been airing since 1997 and has been translated into over 30 languages.

The Pokémon trading card game is a collectible card game that features Pokémon from the video games and anime. The cards are used to battle against other players. The game has been released in over 70 countries and has sold over 30 billion cards worldwide.

Pokémon is one of the most popular media franchises in the world. The video games, anime, and trading cards have been enjoyed by millions of people around the globe.

**Here are some of the most popular Pokémon:**

* Pikachu
* Charizard
* Mewtwo
* Snorlax
* Bulbasaur
* Squirtle
* Eevee
* Gengar
* Lucario
* Greninja

**Pokémon has also been featured in a number of other products, including:**

* Toys
* Clothing
* Food
* Home goods
* Theme parks

The Pokémon franchise continues to grow and evolve, with new video games, anime, and merchandise being released all the time. The franchise is a global phenomenon that has captured the imaginations of people of all ages.
```

### dog

```python
from TheApi import api

result = api.dog()
print(result)
```

```text
https://random.dog/a38f99d2-e34b-43d9-8f7e-318bc8277a17.JPG
```

### fox

```python
from TheApi import api

result = api.fox()
print(result)
```

```text
https://randomfox.ca/?i=37
```

### gen_hashtag

```python
# Usage:
from TheApi import api

result = api.gen_hashtag(text='pokemon', similiar=False)
print(result)
```

```text
# Result:
#pokemon  #pokemongo  #pokemoncards  #pokemontcg  #pokemoncommunity  #pokemonsun  #pokemonsunandmoon  #pokemonmoon  #pokemonxy  #pokemonart  #pokemon20  #pokemonx  #pokemony  #pokemonmemes  #pokemontrainer  #PokemonMaster  #pokemonoras  #pokemonfanart  #pokemonfan  #pokemoncollector  #pokemonred  #pokemonmeme  #pokemoncenter  #pokemonultrasun  #pokemonblue  #pokemoncard  #pokemoncollection  #pokemonultramoon  #pokemoncardsforsale  #pokemoncosplay
```

### get_advice

```python
from TheApi import api

result = api.get_advice()
print(result)
```

```text
Be brave. Even if you're not, pretend to be. No one can tell the difference.
```

### get_hindi_jokes

```python
from TheApi import api

result = api.get_hindi_jokes()
print(result)
```

```text
लड़के किसी भी ऐप में लड़कियों से बात कर सकते है... मगर इनकी आत्मा को शांति WhatsApp number मांग कर ही मिलती है...... 
```

### get_jokes

```python
# Usage:
from TheApi import api

result = api.get_jokes(amount=1)
print(result)
```

```text
# Result:
Programming is 10% science, 20% ingenuity, and 70% getting the ingenuity to work with the science.
```

### get_uselessfact

```python
from TheApi import api

result = api.get_uselessfact()
print(result)
```

```text
Canada makes up 6.67 percent of the Earth`s land area
```

### github_search

```python
# Usage:
from TheApi import api

result = api.github_search(query='pokemon', search_type='repositories', max_results=3)
print(result)
```

```text
# Result:
[{'name': 'PokemonGo-Map', 'full_name': 'AHAAAAAAA/PokemonGo-Map', 'description': '🌏 Live visualization of all the pokemon in your area... and more! (shutdown)', 'url': 'https://github.com/AHAAAAAAA/PokemonGo-Map', 'language': None, 'stargazers_count': 7530, 'forks_count': 2819}, {'name': 'pokemon-showdown', 'full_name': 'smogon/pokemon-showdown', 'description': 'Pokémon battle simulator.', 'url': 'https://github.com/smogon/pokemon-showdown', 'language': 'TypeScript', 'stargazers_count': 4743, 'forks_count': 2773}, {'name': 'PokemonGo-Bot', 'full_name': 'PokemonGoF/PokemonGo-Bot', 'description': 'The Pokemon Go Bot, baking with community.', 'url': 'https://github.com/PokemonGoF/PokemonGo-Bot', 'language': 'Python', 'stargazers_count': 3865, 'forks_count': 1540}]
```

### hindi_quote

```python
from TheApi import api

result = api.hindi_quote()
print(result)
```

```text
अगर नियत अच्छी हो तो नसीब कभी बुरा नहीं होता..!
```

### meme

```python
from TheApi import api

result = api.meme()
print(result)
```

```text
https://preview.redd.it/7xasqwn2sbsd1.png?width=1080&crop=smart&auto=webp&s=d7490361f3d895488447178c8929888b553e5b2e
```

### morse_code

```python
# Usage:
from TheApi import api

result = api.morse_code(txt='pokemon')
print(result)
```

```text
# Result:
.--. --- -.- . -- --- -.
```

### pypi

```python
# Usage:
from TheApi import api

result = api.pypi(package_name='pokemon')
print(result)
```

```text
# Result:
{'name': 'pokemon', 'version': '0.36', 'summary': 'ascii database of pokemon... in Python!', 'author': 'Vanessa Sochat', 'author_email': 'vsoch@noreply.github.users.com', 'license': 'LICENSE', 'home_page': 'https://github.com/vsoch/pokemon', 'package_url': 'https://pypi.org/project/pokemon/', 'requires_python': '', 'keywords': 'pokemon,avatar,ascii,gravatar', 'classifiers': [], 'project_urls': {'Homepage': 'https://github.com/vsoch/pokemon'}}
```

### quote

```python
from TheApi import api

result = api.quote()
print(result)
```

```text
If you change the way you look at things, the things you look at change.

author - Wayne Dyer
```

### randomword

```python
from TheApi import api

result = api.randomword()
print(result)
```

```text
triggered
```

### riddle

```python
from TheApi import api

result = api.riddle()
print(result)
```

```text
{'riddle': 'I am the fountain from which no one can drink. For many I am considered a necessary link. Like gold to all I am sought for, But my continued death brings wealth for all to want more. .What am I?', 'answer': 'Oil'}
```

### stackoverflow_search

```python
# Usage:
from TheApi import api

result = api.stackoverflow_search(query='pokemon', max_results=3, sort_type='relevance', use_cache=True)
print(result)
```

```text
# Result:
[{'tags': ['ios', 'flutter', 'dart'], 'owner': {'account_id': 19921816, 'reputation': 3, 'user_id': 14597469, 'user_type': 'registered', 'profile_image': 'https://lh6.googleusercontent.com/-aT6u2l_JT94/AAAAAAAAAAI/AAAAAAAAAAA/AMZuuclcxb94zp_q0Q2R8DQN7b6X3kgo6w/s96-c/photo.jpg?sz=256', 'display_name': 'Senem Sedef', 'link': 'https://stackoverflow.com/users/14597469/senem-sedef'}, 'is_answered': False, 'view_count': 116, 'answer_count': 0, 'score': 0, 'last_activity_date': 1701515081, 'creation_date': 1622231772, 'last_edit_date': 1701515081, 'question_id': 67744802, 'content_license': 'CC BY-SA 4.0', 'link': 'https://stackoverflow.com/questions/67744802/the-getter-pokemon-was-called-on-null-receiver-null-tried-calling-pokemon', 'title': 'The getter &#39;pokemon&#39; was called on null. Receiver: null Tried calling: pokemon'}, {'tags': ['reactjs', 'random', 'axios'], 'owner': {'account_id': 17931576, 'reputation': 1, 'user_id': 13028884, 'user_type': 'registered', 'profile_image': 'https://www.gravatar.com/avatar/7ebcdd2f784bca5dc54a1a0e17354f86?s=256&d=identicon&r=PG&f=y&so-version=2', 'display_name': 'GieGie', 'link': 'https://stackoverflow.com/users/13028884/giegie'}, 'is_answered': False, 'view_count': 1924, 'answer_count': 2, 'score': 0, 'last_activity_date': 1652730812, 'creation_date': 1642222168, 'last_edit_date': 1642223800, 'question_id': 70718940, 'content_license': 'CC BY-SA 4.0', 'link': 'https://stackoverflow.com/questions/70718940/pokemon-api-request-generate-5-pok%c3%a9mon-at-a-time', 'title': 'Pokemon API request generate 5 Pok&#233;mon at a time'}, {'tags': ['java'], 'owner': {'account_id': 919945, 'reputation': 43, 'user_id': 951797, 'user_type': 'registered', 'profile_image': 'https://www.gravatar.com/avatar/26b06d5d95992fa3780383abe5f49a3d?s=256&d=identicon&r=PG', 'display_name': 'Brian', 'link': 'https://stackoverflow.com/users/951797/brian'}, 'is_answered': True, 'view_count': 32564, 'accepted_answer_id': 7942409, 'answer_count': 3, 'score': 3, 'last_activity_date': 1577442848, 'creation_date': 1319931614, 'question_id': 7942384, 'content_license': 'CC BY-SA 3.0', 'link': 'https://stackoverflow.com/questions/7942384/simple-java-pokemon-fight-simulator', 'title': 'Simple Java Pokemon Fight Simulator'}]
```

### upload_image

```python
from TheApi import api

result = api.upload_image(file_path='file/to/image')
print(result)
```

```text
You will get the URL for the image.
```

### wikipedia

```python
# Usage:
from TheApi import api

result = api.wikipedia(query='pokemon')
print(result)
```

```text
# Result:
{'title': 'Pokémon', 'summary': 'Pokémon is a Japanese media franchise consisting of video games, animated series and films, a trading card game, and other related media. The franchise takes place in a shared universe in which humans co-exist with creatures known as Pokémon, a large variety of species endowed with special powers. The franchise\'s target audience is children aged 5 to 12, but it is known to attract people of all ages.\nThe franchise originated as a pair of role-playing games developed by Game Freak, from an original concept by its founder, Satoshi Tajiri. Released on the Game Boy on February 27, 1996, the games became sleeper hits and were followed by manga series, a trading card game, and anime series and films. From 1998 to 2000, Pokémon was exported to the rest of the world, creating an unprecedented global phenomenon dubbed "Pokémania". By 2002, the craze had ended, after which Pokémon became a fixture in popular culture, with new products being released to this day. In the summer of 2016, the franchise spawned a second craze with the release of Pokémon Go, an augmented reality game developed by Niantic. Pokémon has since been estimated to be the world\'s highest-grossing media franchise and one of the best-selling video game franchises.\nPokémon has an uncommon ownership structure. Unlike most IPs, which are owned by one company, Pokémon is jointly owned by three: Nintendo, Game Freak, and Creatures. Game Freak develops the core series role-playing games, which are published by Nintendo exclusively for their consoles, while Creatures manages the trading card game and related merchandise, occasionally developing spin-off titles. The three companies established The Pokémon Company (TPC) in 1998 to manage the Pokémon property within Asia. The Pokémon anime series and films are co-owned by Shogakukan. Since 2009, The Pokémon Company International (TPCi), a subsidiary of TPC, has managed the franchise in all regions outside of Asia.', 'url': 'https://en.wikipedia.org/?curid=23745', 'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/9/98/International_Pok%C3%A9mon_logo.svg/500px-International_Pok%C3%A9mon_logo.svg.png'}
```

### words

```python
# Usage:
from TheApi import api

result = api.words(num_words=5)
print(result)
```

```text
# Result:
['tapioca', 'overgirding', 'gargoyled', 'skylarks', 'sucker']
```

### write

```python
# Usage:
from TheApi import api

result = api.write(text='pokemon')
print(result)
```

```text
# Result:
https://envs.sh/0Q7.jpg
```


This Project is Licensed under [MIT License](https://github.com/Vivekkumar-IN/TheApi/blob/main/LICENSE)