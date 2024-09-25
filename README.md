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
20. [stackoverflow_search](#stackoverflow_search)
21. [wikipedia](#wikipedia)
22. [words](#words)
23. [write](#write)

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
| [stackoverflow_search](#stackoverflow_search) | ✅ |
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
['https://twinfinite.net/wp-content/uploads/2019/09/PokemonTypes.png', 'https://pokeguide.neocities.org/Pic/pokemontype.png', 'https://www.mandatory.gg/wp-content/uploads/mandatory-guide-pokemon-ecarlate-violet-table-types-forces-faiblesses.png', 'http://fc09.deviantart.net/fs70/i/2013/318/0/f/pokemon_types_wheel_by_kamionero-d6u6o9i.png', 'https://3.bp.blogspot.com/-b8i_WR7eoI0/WV8bxYVOZBI/AAAAAAAAGck/5nEIhuF-zMASQfxBF6JhSw6SRfjVh7ocACKgBGAs/s1600/ENG-05-02-02-Pokemon-type-chart.png', 'https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/748002fd-52dc-423a-9160-d0684fac6120/d7rzf8m-38e64a38-18de-4363-9772-e399931c2438.jpg/v1/fill/w_1024,h_2256,q_75,strp/pokemon_type_chart_by_freebynature_d7rzf8m-fullview.jpg?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7ImhlaWdodCI6Ijw9MjI1NiIsInBhdGgiOiJcL2ZcLzc0ODAwMmZkLTUyZGMtNDIzYS05MTYwLWQwNjg0ZmFjNjEyMFwvZDdyemY4bS0zOGU2NGEzOC0xOGRlLTQzNjMtOTc3Mi1lMzk5OTMxYzI0MzguanBnIiwid2lkdGgiOiI8PTEwMjQifV1dLCJhdWQiOlsidXJuOnNlcnZpY2U6aW1hZ2Uub3BlcmF0aW9ucyJdfQ.kYZkyCN-RS4wkvCSj2-xHLJEb6opIWi8GP2dI6V8gvA', 'https://usercontent2.hubstatic.com/13982569_f1024.jpg', 'http://images6.fanpop.com/image/photos/34100000/Pokemon-types-pokemon-34164928-846-1824.jpg', 'http://pm1.narvii.com/5911/046836f42227a84ce0e275253646658e383b0e2d_hq.jpg', 'https://videogamesuncovered.com/wp-content/uploads/2016/12/pokemon-types.jpg', 'https://upload.wikimedia.org/wikipedia/commons/5/5e/Pokémon_types_(english).png', 'https://www.theloadout.com/wp-content/sites/theloadout/2023/06/pokemon-type-chart-icons.jpg', 'https://static0.thegamerimages.com/wordpress/wp-content/uploads/2017/07/Every-Pokemon-Type-Lead.jpg', 'https://www.pngitem.com/pimgs/m/510-5102094_http-image-noelshack-pokemon-artefact-all-types-pokemon.png', 'https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/4c70150d-f366-4c4f-b81e-767588eefdbf/dg76yyu-fb4ac701-2233-4d50-93e9-bb04b22514b7.png/v1/fill/w_639,h_866,q_80,strp/fanmade_pokemon_types_by_ljb2009_dg76yyu-fullview.jpg?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7ImhlaWdodCI6Ijw9ODY2IiwicGF0aCI6IlwvZlwvNGM3MDE1MGQtZjM2Ni00YzRmLWI4MWUtNzY3NTg4ZWVmZGJmXC9kZzc2eXl1LWZiNGFjNzAxLTIyMzMtNGQ1MC05M2U5LWJiMDRiMjI1MTRiNy5wbmciLCJ3aWR0aCI6Ijw9NjM5In1dXSwiYXVkIjpbInVybjpzZXJ2aWNlOmltYWdlLm9wZXJhdGlvbnMiXX0.5AO-s7OJNtzLSN5LrUV4gndFYjAYR7t6KZmjM-K3L8U', 'https://external-preview.redd.it/R9F2DLaTJR3JERoJ7seiKjyCoQolSXGmgV8ohXO8ad4.jpg?auto=webp&amp;s=a835bd840816135095c70b72b7ef0b43ec65b3f3', 'https://external-preview.redd.it/UcrlB9ltgijNDnXesm06BysNLAuV4QJprZXhha81yQI.png?auto=webp&amp;s=f7fb592f8077c96a2ba8394f3cffec9808322afb', 'https://sixprizes.com/wp-content/uploads/2015/06/pokemon-types-rulebook.jpg', 'https://exputer.com/wp-content/uploads/2023/01/Pokemon-Types-chart.jpg', 'https://pre00.deviantart.net/0750/th/pre/f/2013/104/8/3/my_favourite_pokemon_types__by_sirnorm-d61pavo.png', 'https://static3.cbrimages.com/wordpress/wp-content/uploads/2019/09/Pokemon-Ash-Feature-Image-1.jpg', 'https://townsquare.media/site/622/files/2016/08/poke-feat.jpg?w=1200&amp;h=0&amp;zc=1&amp;s=0&amp;a=t&amp;q=89', 'http://clipart-library.com/image_gallery2/Pokemon-Transparent.png']
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

result = api.carbon(code='pokemon')
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
https://cdn2.thecatapi.com/images/MTUyNjg2NA.gif
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
Sure! What would you like to know or discuss about Pokémon? Are you interested in games, trading cards, specific Pokémon, or something else?
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
https://random.dog/486cc9cd-f850-4639-983d-fe7531879573.gif
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
https://randomfox.ca/?i=43
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
Don't wear clean trousers when walking your dog in the park.
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
नेट प्लान के सस्ते होने से चोरों का सबसे ज्यादा नुकसान हुआ हैं जिस घर में चोरी करने जाते हैं कोई न कोई जाग रहा होता हैं 😆🤣😋😉 
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
Hey Girl,
Roses are #ff0000,
Violets are #0000ff,
I use hex codes,
But I'd use RGB for you.
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
Steely Dan got their name from a sexual device depicted in the book `The Naked Lunch`.  
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
[{'name': 'PokemonGo-Map', 'full_name': 'AHAAAAAAA/PokemonGo-Map', 'description': '🌏 Live visualization of all the pokemon in your area... and more! (shutdown)', 'url': 'https://github.com/AHAAAAAAA/PokemonGo-Map', 'language': None, 'stargazers_count': 7533, 'forks_count': 2819}, {'name': 'pokemon-showdown', 'full_name': 'smogon/pokemon-showdown', 'description': 'Pokémon battle simulator.', 'url': 'https://github.com/smogon/pokemon-showdown', 'language': 'TypeScript', 'stargazers_count': 4731, 'forks_count': 2766}, {'name': 'PokemonGo-Bot', 'full_name': 'PokemonGoF/PokemonGo-Bot', 'description': 'The Pokemon Go Bot, baking with community.', 'url': 'https://github.com/PokemonGoF/PokemonGo-Bot', 'language': 'Python', 'stargazers_count': 3864, 'forks_count': 1540}]
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
जो दौर गुजरता नहीं, हम उस दौर से गुजरे है।
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
https://preview.redd.it/091h9q9sgpqd1.png?width=640&crop=smart&auto=webp&s=0a9ad395223a74fb37ca039b810d9b15efbf1ef5
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
The two most powerful warriors are patience and time.

author - Leo Tolstoy
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
pinnacles
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
[{'tags': ['ios', 'flutter', 'dart'], 'owner': {'account_id': 19921816, 'reputation': 3, 'user_id': 14597469, 'user_type': 'registered', 'profile_image': 'https://lh6.googleusercontent.com/-aT6u2l_JT94/AAAAAAAAAAI/AAAAAAAAAAA/AMZuuclcxb94zp_q0Q2R8DQN7b6X3kgo6w/s96-c/photo.jpg?sz=256', 'display_name': 'Senem Sedef', 'link': 'https://stackoverflow.com/users/14597469/senem-sedef'}, 'is_answered': False, 'view_count': 116, 'answer_count': 0, 'score': 0, 'last_activity_date': 1701515081, 'creation_date': 1622231772, 'last_edit_date': 1701515081, 'question_id': 67744802, 'content_license': 'CC BY-SA 4.0', 'link': 'https://stackoverflow.com/questions/67744802/the-getter-pokemon-was-called-on-null-receiver-null-tried-calling-pokemon', 'title': 'The getter &#39;pokemon&#39; was called on null. Receiver: null Tried calling: pokemon'}, {'tags': ['reactjs', 'random', 'axios'], 'owner': {'account_id': 17931576, 'reputation': 1, 'user_id': 13028884, 'user_type': 'registered', 'profile_image': 'https://www.gravatar.com/avatar/7ebcdd2f784bca5dc54a1a0e17354f86?s=256&d=identicon&r=PG&f=y&so-version=2', 'display_name': 'GieGie', 'link': 'https://stackoverflow.com/users/13028884/giegie'}, 'is_answered': False, 'view_count': 1908, 'answer_count': 2, 'score': 0, 'last_activity_date': 1652730812, 'creation_date': 1642222168, 'last_edit_date': 1642223800, 'question_id': 70718940, 'content_license': 'CC BY-SA 4.0', 'link': 'https://stackoverflow.com/questions/70718940/pokemon-api-request-generate-5-pok%c3%a9mon-at-a-time', 'title': 'Pokemon API request generate 5 Pok&#233;mon at a time'}, {'tags': ['java'], 'owner': {'account_id': 919945, 'reputation': 43, 'user_id': 951797, 'user_type': 'registered', 'profile_image': 'https://www.gravatar.com/avatar/26b06d5d95992fa3780383abe5f49a3d?s=256&d=identicon&r=PG', 'display_name': 'Brian', 'link': 'https://stackoverflow.com/users/951797/brian'}, 'is_answered': True, 'view_count': 32550, 'accepted_answer_id': 7942409, 'answer_count': 3, 'score': 3, 'last_activity_date': 1577442848, 'creation_date': 1319931614, 'question_id': 7942384, 'content_license': 'CC BY-SA 3.0', 'link': 'https://stackoverflow.com/questions/7942384/simple-java-pokemon-fight-simulator', 'title': 'Simple Java Pokemon Fight Simulator'}]
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
['gelatinized', 'kaiaks', 'volvox', 'imprint', 'completeness']
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