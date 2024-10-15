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
from TheApi import api

result = api.bing_image(query='pokemon', limit=3)
print(result)
```

```text
['https://blog.looglebiz.com/wp-content/uploads/2022/10/og-default-image.jpeg', 'https://redtri.com/wp-content/uploads/2019/02/screen-shot-2019-03-01-at-5.26.39-pm.png?is-pending-load=1', 'https://assets.nintendo.com/image/upload/c_fill,w_1200/q_auto:best/f_auto/dpr_2.0/ncom/en_CA/games/switch/p/pokemon-violet-switch/hero']
```

### blackpink

```python
from TheApi import api

result = api.blackpink(args='pokemon', color='#ff94e0', border_color=None)
print(result)
```

```text
https://envs.sh/0Ql.jpg
```

### carbon

```python
from TheApi import api

result = api.carbon(query='pokemon')
print(result)
```

```text
https://envs.sh/0Qk.png
```

### cat

```python
from TheApi import api

result = api.cat()
print(result)
```

```text
https://cdn2.thecatapi.com/images/RIRLq-8sp.jpg
```

### chatgpt

```python
from TheApi import api

result = api.chatgpt(query='pokemon')
print(result)
```

```text
None
```

### dog

```python
from TheApi import api

result = api.dog()
print(result)
```

```text
https://random.dog/6f6ea89d-5144-49c8-8f2a-12ba7798b8bf.jpg
```

### fox

```python
from TheApi import api

result = api.fox()
print(result)
```

```text
https://randomfox.ca/?i=48
```

### gen_hashtag

```python
from TheApi import api

result = api.gen_hashtag(text='pokemon', similiar=False)
print(result)
```

```text
#pokemon  #pokemongo  #pokemoncards  #pokemontcg  #pokemoncommunity  #pokemonsun  #pokemonsunandmoon  #pokemonmoon  #pokemonxy  #pokemonart  #pokemon20  #pokemonx  #pokemony  #pokemonmemes  #pokemontrainer  #PokemonMaster  #pokemonoras  #pokemonfanart  #pokemonfan  #pokemoncollector  #pokemonred  #pokemonmeme  #pokemoncenter  #pokemonultrasun  #pokemonblue  #pokemoncard  #pokemoncollection  #pokemonultramoon  #pokemoncardsforsale  #pokemoncosplay
```

### get_advice

```python
from TheApi import api

result = api.get_advice()
print(result)
```

```text
Fail. Fail again. Fail better.
```

### get_hindi_jokes

```python
from TheApi import api

result = api.get_hindi_jokes()
print(result)
```

```text
एक एयरलाइन्स ने एक योजना शुरू की आप टिकट खरीदें – साथ में आपकी पत्नी का टिकट मुफ्त ! इस योजना में भारी सफलता मिलने के बाद कम्पनी ने सारी पत्नियों को पत्र लिख कर पूछा -यात्रा कैसी रही ? सभी का एक जैसा ही जवाब आया… कौन सी यात्रा ?? 😂 😂
```

### get_jokes

```python
from TheApi import api

result = api.get_jokes(amount=1)
print(result)
```

```text
My ex had an accident. I told the paramedics the wrong blood type for her. She'll finally experience what rejection is really like.
```

### get_uselessfact

```python
from TheApi import api

result = api.get_uselessfact()
print(result)
```

```text
Most collect calls are made on father`s day.
```

### github_search

```python
from TheApi import api

result = api.github_search(query='pokemon', search_type='repositories', max_results=3)
print(result)
```

```text
[{'name': 'PokemonGo-Map', 'full_name': 'AHAAAAAAA/PokemonGo-Map', 'description': '🌏 Live visualization of all the pokemon in your area... and more! (shutdown)', 'url': 'https://github.com/AHAAAAAAA/PokemonGo-Map', 'language': None, 'stargazers_count': 7531, 'forks_count': 2817}, {'name': 'pokemon-showdown', 'full_name': 'smogon/pokemon-showdown', 'description': 'Pokémon battle simulator.', 'url': 'https://github.com/smogon/pokemon-showdown', 'language': 'TypeScript', 'stargazers_count': 4764, 'forks_count': 2783}, {'name': 'PokemonGo-Bot', 'full_name': 'PokemonGoF/PokemonGo-Bot', 'description': 'The Pokemon Go Bot, baking with community.', 'url': 'https://github.com/PokemonGoF/PokemonGo-Bot', 'language': 'Python', 'stargazers_count': 3864, 'forks_count': 1542}]
```

### hindi_quote

```python
from TheApi import api

result = api.hindi_quote()
print(result)
```

```text
लाख दलदल हो पांव जमाए रखिए, हात खाली ही सही उपर उठाये रखिए, कौन कहता है छलनी में पानी रुक नहीं सकता, बर्फ बनने तक हौसला बनाये रखिए।
```

### meme

```python
from TheApi import api

result = api.meme()
print(result)
```

```text
https://preview.redd.it/0lsqqxf8npud1.png?width=960&crop=smart&auto=webp&s=26a5bb5a0f031a1117e56dce59fe85135f8866c1
```

### morse_code

```python
from TheApi import api

result = api.morse_code(txt='pokemon')
print(result)
```

```text
.--. --- -.- . -- --- -.
```

### pypi

```python
from TheApi import api

result = api.pypi(package_name='pokemon')
print(result)
```

```text
{'name': 'pokemon', 'version': '0.36', 'summary': 'ascii database of pokemon... in Python!', 'author': 'Vanessa Sochat', 'author_email': 'vsoch@noreply.github.users.com', 'license': 'LICENSE', 'home_page': 'https://github.com/vsoch/pokemon', 'package_url': 'https://pypi.org/project/pokemon/', 'requires_python': '', 'keywords': 'pokemon,avatar,ascii,gravatar', 'classifiers': [], 'project_urls': {'Homepage': 'https://github.com/vsoch/pokemon'}}
```

### quote

```python
from TheApi import api

result = api.quote()
print(result)
```

```text
Nothing in life is to be feared. It is only to be understood.

author - Marie Curie
```

### randomword

```python
from TheApi import api

result = api.randomword()
print(result)
```

```text
None
```

### riddle

```python
from TheApi import api

result = api.riddle()
print(result)
```

```text
{'riddle': 'What can be heard and caught but never seen?', 'answer': 'A Remark'}
```

### stackoverflow_search

```python
from TheApi import api

result = api.stackoverflow_search(query='pokemon', max_results=3, sort_type='relevance', use_cache=True)
print(result)
```

```text
[{'tags': ['ios', 'flutter', 'dart'], 'owner': {'account_id': 19921816, 'reputation': 3, 'user_id': 14597469, 'user_type': 'registered', 'profile_image': 'https://lh6.googleusercontent.com/-aT6u2l_JT94/AAAAAAAAAAI/AAAAAAAAAAA/AMZuuclcxb94zp_q0Q2R8DQN7b6X3kgo6w/s96-c/photo.jpg?sz=256', 'display_name': 'Senem Sedef', 'link': 'https://stackoverflow.com/users/14597469/senem-sedef'}, 'is_answered': False, 'view_count': 117, 'answer_count': 0, 'score': 0, 'last_activity_date': 1701515081, 'creation_date': 1622231772, 'last_edit_date': 1701515081, 'question_id': 67744802, 'content_license': 'CC BY-SA 4.0', 'link': 'https://stackoverflow.com/questions/67744802/the-getter-pokemon-was-called-on-null-receiver-null-tried-calling-pokemon', 'title': 'The getter &#39;pokemon&#39; was called on null. Receiver: null Tried calling: pokemon'}, {'tags': ['reactjs', 'random', 'axios'], 'owner': {'account_id': 17931576, 'reputation': 1, 'user_id': 13028884, 'user_type': 'registered', 'profile_image': 'https://www.gravatar.com/avatar/7ebcdd2f784bca5dc54a1a0e17354f86?s=256&d=identicon&r=PG&f=y&so-version=2', 'display_name': 'GieGie', 'link': 'https://stackoverflow.com/users/13028884/giegie'}, 'is_answered': False, 'view_count': 1931, 'answer_count': 2, 'score': 0, 'last_activity_date': 1652730812, 'creation_date': 1642222168, 'last_edit_date': 1642223800, 'question_id': 70718940, 'content_license': 'CC BY-SA 4.0', 'link': 'https://stackoverflow.com/questions/70718940/pokemon-api-request-generate-5-pok%c3%a9mon-at-a-time', 'title': 'Pokemon API request generate 5 Pok&#233;mon at a time'}, {'tags': ['java'], 'owner': {'account_id': 919945, 'reputation': 43, 'user_id': 951797, 'user_type': 'registered', 'profile_image': 'https://www.gravatar.com/avatar/26b06d5d95992fa3780383abe5f49a3d?s=256&d=identicon&r=PG', 'display_name': 'Brian', 'link': 'https://stackoverflow.com/users/951797/brian'}, 'is_answered': True, 'view_count': 32585, 'accepted_answer_id': 7942409, 'answer_count': 3, 'score': 3, 'last_activity_date': 1577442848, 'creation_date': 1319931614, 'question_id': 7942384, 'content_license': 'CC BY-SA 3.0', 'link': 'https://stackoverflow.com/questions/7942384/simple-java-pokemon-fight-simulator', 'title': 'Simple Java Pokemon Fight Simulator'}]
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
from TheApi import api

result = api.wikipedia(query='pokemon')
print(result)
```

```text
{'title': 'Pokémon', 'summary': 'Pokémon is a Japanese media franchise consisting of video games, animated series and films, a trading card game, and other related media. The franchise takes place in a shared universe in which humans co-exist with creatures known as Pokémon, a large variety of species endowed with special powers. The franchise\'s target audience is children aged 5 to 12, but it is known to attract people of all ages.\nThe franchise originated as a pair of role-playing games developed by Game Freak, from an original concept by its founder, Satoshi Tajiri. Released on the Game Boy on February 27, 1996, the games became sleeper hits and were followed by manga series, a trading card game, and anime series and films. From 1998 to 2000, Pokémon was exported to the rest of the world, creating an unprecedented global phenomenon dubbed "Pokémania". By 2002, the craze had ended, after which Pokémon became a fixture in popular culture, with new products being released to this day. In the summer of 2016, the franchise spawned a second craze with the release of Pokémon Go, an augmented reality game developed by Niantic. Pokémon has since been estimated to be the world\'s highest-grossing media franchise and one of the best-selling video game franchises.\nPokémon has an uncommon ownership structure. Unlike most IPs, which are owned by one company, Pokémon is jointly owned by three: Nintendo, Game Freak, and Creatures. Game Freak develops the core series role-playing games, which are published by Nintendo exclusively for their consoles, while Creatures manages the trading card game and related merchandise, occasionally developing spin-off titles. The three companies established The Pokémon Company (TPC) in 1998 to manage the Pokémon property within Asia. The Pokémon anime series and films are co-owned by Shogakukan. Since 2009, The Pokémon Company International (TPCi), a subsidiary of TPC, has managed the franchise in all regions outside of Asia.\n\n', 'url': 'https://en.wikipedia.org/?curid=23745', 'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/9/98/International_Pok%C3%A9mon_logo.svg/500px-International_Pok%C3%A9mon_logo.svg.png'}
```

### words

```python
from TheApi import api

result = api.words(num_words=5)
print(result)
```

```text
[]
```

### write

```python
from TheApi import api

result = api.write(text='pokemon')
print(result)
```

```text
https://envs.sh/0Q7.jpg
```


This Project is Licensed under [MIT License](https://github.com/Vivekkumar-IN/TheApi/blob/main/LICENSE)