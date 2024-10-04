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
| [carbon](#carbon) | ❌ |
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
| [upload_image](#upload_image) | ❌ |
| [wikipedia](#wikipedia) | ✅ |
| [words](#words) | ✅ |
| [write](#write) | ❌ |

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
['https://images5.alphacoders.com/130/thumb-1920-1308338.jpg', 'https://images.wallpapersden.com/image/download/pokemon-scarlet-and-violet-hd_bW1qamqUmZqaraWkpJRmbmdlrWZlbWU.jpg', 'https://staticg.sportskeeda.com/editor/2023/07/0c8e6-16887208209298-1920.jpg']
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
# Error:
name 'self' is not defined
```

### cat

```python
# Usage:
from TheApi import api

result = api.cat()
print(result)
```

```text
# Result:
https://cdn2.thecatapi.com/images/da1.jpg
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
**What is Pokémon?**

Pokémon is a Japanese media franchise created by Satoshi Tajiri in 1996. It revolves around fictional creatures called "Pokémon", which can be captured, trained, and battled against each other. The franchise has grown into a global phenomenon, with video games, trading card games, animated television series, films, and various merchandise.

**Pokémon Characteristics**

* **Types:** Pokémon come in 18 different types, each with its own strengths and weaknesses against other types.
* **Abilities:** Pokémon have special abilities that can affect battles, such as increasing their attack power or healing themselves.
* **Evolutions:** Many Pokémon can evolve into more powerful forms through training or specific events.
* **Legendary Pokémon:** Rare and powerful Pokémon that are often featured as story bosses or event rewards.
* **Mythical Pokémon:** Similar to Legendary Pokémon, but even rarer and often associated with lore or special events.

**Main Pokémon Video Games**

* **Pokémon Red, Blue, and Green (1996):** The original Pokémon games for the Game Boy, which introduced the basic gameplay mechanics.
* **Pokémon Gold, Silver, and Crystal (1999):** Sequels to Red, Blue, and Green, which introduced the second generation of Pokémon.
* **Pokémon Ruby, Sapphire, and Emerald (2002):** Introduced the third generation of Pokémon and introduced the concept of double battles.
* **Pokémon Diamond, Pearl, and Platinum (2006):** Set in the Sinnoh region, these games introduced the fourth generation of Pokémon.
* **Pokémon Black, White, Black 2, and White 2 (2010-2012):** Introduced the fifth generation of Pokémon and explored themes of truth and ideals.
* **Pokémon X and Y (2013):** Set in the Kalos region, these games introduced the sixth generation of Pokémon and featured 3D graphics for the first time.
* **Pokémon Sun, Moon, Ultra Sun, and Ultra Moon (2016-2017):** Set in the Alola region, these games introduced the seventh generation of Pokémon and featured unique regional variants.
* **Pokémon Sword and Shield (2019):** Set in the Galar region, these games introduced the eighth generation of Pokémon and featured the Dynamax and Gigantamax mechanics.

**Other Pokémon Games**

In addition to the main series, there are numerous spin-off games in the Pokémon franchise, including:

* **Pokémon GO:** A mobile game that uses augmented reality technology to allow players to catch Pokémon in the real world.
* **Pokémon Snap:** A photography game where players take pictures of Pokémon in the wild.
* **Pokémon Stadium:** A fighting game where players can battle their Pokémon against each other.
* **Pokémon Mystery Dungeon:** A dungeon-crawling RPG where players control Pokémon and explore randomly generated dungeons.
* **Pokémon Masters EX:** A mobile strategy game where players team up with popular Pokémon trainers from the anime series.
```

### dog

```python
# Usage:
from TheApi import api

result = api.dog()
print(result)
```

```text
# Result:
https://random.dog/a38f99d2-e34b-43d9-8f7e-318bc8277a17.JPG
```

### fox

```python
# Usage:
from TheApi import api

result = api.fox()
print(result)
```

```text
# Result:
https://randomfox.ca/?i=5
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
# Usage:
from TheApi import api

result = api.get_advice()
print(result)
```

```text
# Result:
Never pay full price for a sofa at DFS.
```

### get_hindi_jokes

```python
# Usage:
from TheApi import api

result = api.get_hindi_jokes()
print(result)
```

```text
# Result:
सुबह बैंक में एकाउंट खुलवाने गया बोले दो प्रतिष्ठित लोगो का रेफरेन्स दो मैंने  कहा–विजय माल्या नीरव मोदी चार लोग घसीट के बाहर तक छोड़ने आए।
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
Four engineers get into a car. The car won't start.
The Mechanical engineer says "It's a broken starter".
The Electrical engineer says "Dead battery".
The Chemical engineer says "Impurities in the gasoline".
The IT engineer says "Hey guys, I have an idea: How about we all get out of the car and get back in".
```

### get_uselessfact

```python
# Usage:
from TheApi import api

result = api.get_uselessfact()
print(result)
```

```text
# Result:
111,111,111 x 111,111,111 = 12,345,678,987,654,321
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
# Usage:
from TheApi import api

result = api.hindi_quote()
print(result)
```

```text
# Result:
पसन्द आया तो दिल में… नही तो दिमाग में भी नहीं!!
```

### meme

```python
# Usage:
from TheApi import api

result = api.meme()
print(result)
```

```text
# Result:
https://preview.redd.it/bmo1fgpioosd1.png?width=1080&crop=smart&auto=webp&s=3f6e52ba7050058891ce240bf27abcff03499984
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
# Usage:
from TheApi import api

result = api.quote()
print(result)
```

```text
# Result:
The thing that is disliked by me is also disliked by others. Since I dislike this thing, how can I inflict it on someone else?

author - The Buddha
```

### randomword

```python
# Usage:
from TheApi import api

result = api.randomword()
print(result)
```

```text
# Result:
hennery
```

### riddle

```python
# Usage:
from TheApi import api

result = api.riddle()
print(result)
```

```text
# Result:
{'riddle': 'How many of each type of animal did Moses take on the Ark?', 'answer': 'None, it was Noah'}
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
# Usage:
from TheApi import api

result = api.upload_image(file_path='pokemon')
print(result)
```

```text
# Error:
File not found: 'pokemon' - Ensure the file path is correct.
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
['footloose', 'meridian', 'flexing', 'cachinnate', 'photophase']
```

### write

```python
# Usage:
from TheApi import api

result = api.write(text='pokemon')
print(result)
```

```text
# Error:
name 'self' is not defined
```


This Project is Licensed under [MIT License](https://github.com/Vivekkumar-IN/TheApi/blob/main/LICENSE)