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
| [upload_image](#upload_image) | ❌ |
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
# Result:
https://envs.sh/0Qk.png
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
https://cdn2.thecatapi.com/images/e75.jpg
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
**Pokémon**

**Concepto**

Pokémon es una franquicia de medios japonesa que comenzó como un videojuego de rol para Game Boy en 1996. Desde entonces, se ha expandido a una serie de otros videojuegos, series de anime, películas, manga, juguetes, juegos de cartas coleccionables y otros productos.

**Pokémon**

Los Pokémon son criaturas ficticias que existen en el mundo del juego. Hay más de 1.000 especies diferentes de Pokémon, cada una con sus propias fortalezas, debilidades, habilidades y apariencia únicas.

Los Pokémon pueden capturar, entrenar y luchar entre sí los jugadores. También pueden intercambiarse entre jugadores.

**Juego**

El juego de Pokémon gira en torno a la exploración, la captura y la lucha contra Pokémon. Los jugadores controlan a un personaje que viaja por el mundo del juego, encontrando y capturando Pokémon nuevos. Los jugadores también pueden entrenar a sus Pokémon para que se vuelvan más fuertes y luchar contra otros Pokémon en batallas por turnos.

**Series de anime**

La serie de anime Pokémon sigue las aventuras de Ash Ketchum, un joven entrenador Pokémon que sueña con convertirse en un Maestro Pokémon. Junto con sus amigos Misty y Brock, Ash viaja por el mundo Pokémon, conociendo nuevos Pokémon y enfrentándose a desafíos.

**Películas**

Se han estrenado varias películas de Pokémon desde 1998. Las películas suelen contar historias independientes que no forman parte de la continuidad principal del juego o el anime.

**Otros productos**

Además de los videojuegos, la serie de anime y las películas, Pokémon también se ha expandido a una amplia gama de otros productos, incluidos manga, juguetes, juegos de cartas coleccionables y artículos de colección.

**Impacto cultural**

Pokémon se ha convertido en una de las franquicias de medios más populares y exitosas de todos los tiempos. Ha vendido más de 380 millones de copias de videojuegos en todo el mundo y ha generado más de 100 mil millones de dólares en ingresos totales. La franquicia ha inspirado varios parques temáticos, atracciones y eventos en vivo.
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
https://random.dog/08f5398d-7f89-47da-a5cd-1ed74967dc1f.jpg
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
https://randomfox.ca/?i=88
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
Don't assume anything is possible or impossible until you've asked the people who will be doing the work.
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
अगर श्रीदेवी अपना एक शोरूम खोलें, तो वह कहेंगी,  अभी  ...बोनी.. का टाइम है! 😆🤣😋😉
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
My wife and I have reached the difficult decision that we do not want children.
If anybody does, please just send me your contact details and we can drop them off tomorrow.
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
Rubber bands last longer when refrigerated.  
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
सोचो तो आप बिल्कुल अकेले हो!! ठीक से सोचों तो यही सत्य है।
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
https://preview.redd.it/j9dowcg1dksd1.png?width=1080&crop=smart&auto=webp&s=13cc496e68fa7c05c21c02eb9fa217b007eb5de7
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
The way we communicate with others and with ourselves ultimately determines the quality of our lives.

author - Tony Robbins
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
cactuses
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
{'riddle': 'If life gets tough, what do you have that you can always count on?', 'answer': 'Your fingers!'}
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
['brownnose', 'repulsing', 'koumis', 'depicts', 'pyrolyzate']
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