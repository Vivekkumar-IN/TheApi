##### Installation

```sh
pip install git+https://github.com/Vivekkumar-IN/TheApi@main
```

---

# API Documentation

This API provides both synchronous and asynchronous usage:

- **Sync**: `from TheApi.sync import api`
- **Async**: `from TheApi import api`

The following examples use the **async** version.

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
16. [pypi](#pypi)
17. [quote](#quote)
18. [random_word](#random_word)
19. [riddle](#riddle)
20. [stackoverflow_search](#stackoverflow_search)
21. [upload_image](#upload_image)
22. [wikipedia](#wikipedia)
23. [words](#words)
24. [write](#write)

## API Status

| Function Name | Status |
|---------------|--------|
| [bing_image](#bing_image) | ✅ |
| [blackpink](#blackpink) | ✅ |
| [carbon](#carbon) | ✅ |
| [cat](#cat) | ✅ |
| [chatgpt](#chatgpt) | ❌ |
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
| [pypi](#pypi) | ✅ |
| [quote](#quote) | ✅ |
| [random_word](#random_word) | ✅ |
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

result = await api.bing_image(query='pokemon', limit=3)
print(result)
```

```text
['https://images5.alphacoders.com/130/thumb-1920-1308338.jpg', 'https://www.pockettactics.com/wp-content/sites/pockettactics/2023/01/Pokémon-wallpapers-5.jpg', 'https://staticg.sportskeeda.com/editor/2023/02/394a3-16769313907566-1920.jpg', 'https://media.gamestop.com/i/gamestop/11103360/New-Pokemon-Snap---Nintendo-Switch', 'https://img-eshop.cdn.nintendo.net/i/00bd7efe46ab2b3ff0774172a5d4f21a5b2f467b3e324557ce1e9a9ae12c1d3b.jpg', 'https://assets-prd.ignimgs.com/2021/03/01/new-pokemon-snap-button-1614639848584.jpg', 'https://www.gamespot.com/a/uploads/screen_kubrick/123/1239113/3801204-6238037227-screenshot02.jpg', 'https://www.nme.com/wp-content/uploads/2021/05/New-Pokemon-Snap-Credit-Bandai-Namco-HERO@2000x1270.jpg', 'https://www.rpgfan.com/wp-content/uploads/2021/01/New-Pokemon-Snap-Screenshot-044.jpg', 'https://www.videogamer.com/wp-content/uploads/01d7162d-749b-43eb-bdcc-5c0cf9e49881_New_Pokmon_Snap_Main.jpg', 'https://images.launchbox-app.com/fc92b8c7-704f-43e9-ab5a-407b712bc662.jpg', 'https://i.ytimg.com/vi/e_V9nUUP2oo/maxresdefault.jpg', 'https://i.gadgets360cdn.com/products/large/New-Pokemon-Snap-Wallpaper-1440x2560-1000x1778-1646977124.jpg', 'https://i0.wp.com/mynintendonews.com/wp-content/uploads/2021/01/new_pokemon_snap_logo.jpg?ssl=1', 'https://twinfinite.net/wp-content/uploads/2021/04/New-Pokemon-Snap-scaled.jpg', 'https://cdn.vox-cdn.com/thumbor/Lgiz7lrS_auxnKixNMsWmsx_ETE=/1400x788/filters:format(jpeg)/cdn.vox-cdn.com/uploads/chorus_asset/file/22473880/Switch_NewPokemonSnap_Screenshots_Feb26__9_.jpg', 'https://images.launchbox-app.com/1f06f096-8eb6-43ac-abbb-262deb1bf596.jpg', 'https://assets.nintendo.com/image/upload/c_fill,w_1200/q_auto:best/f_auto/dpr_2.0/ncom/en_US/products/games/switch/new-pokemon-snap/110735-switch-new-pokemon-snap-us-1200x675', 'https://webgames.host/uploads/2017/09/pokemon-snap.jpg', 'https://videogamesuncovered.com/wp-content/uploads/2021/01/new-pokemon-snap-social.jpg', 'https://media.npr.org/assets/img/2021/04/29/snap-1_wide-7c41973fe9eef7cbc49beec9a59f3bf5410187d2-s1400-c100.jpg', 'https://www.nintendo.com/sg/switch/arft/img/hero_sp.jpg', 'https://cdn.mobilesyrup.com/wp-content/uploads/2021/01/new-pokemon-snap-screenshot-2.jpg', 'https://upload.wikimedia.org/wikipedia/commons/thumb/9/97/Pokemon_Type_Chart.svg/2048px-Pokemon_Type_Chart.svg.png', 'https://vignette.wikia.nocookie.net/pokemon/images/8/8c/PokemonTypes.png/revision/latest?cb=20170417193722', 'https://img.pokemondb.net/images/typechart.png', 'http://upload.wikimedia.org/wikipedia/commons/5/5e/Pokémon_types_(english).png', 'https://www.theloadout.com/wp-content/sites/theloadout/2023/06/pokemon-type-chart-icons.jpg', 'https://i.pinimg.com/originals/95/b2/6f/95b26f7cd39e206259faa20fd57e7b47.png', 'https://raw.githubusercontent.com/kennycason/cellular-automata-pokemon-types/master/data/pokemon_gen1_type_chart.png?raw=true', 'https://res.cloudinary.com/lmn/image/upload/e_sharpen:150,f_auto,fl_lossy,q_80/v1/gameskinnyc/p/o/k/pokemon-types-table-ad163.png', 'https://1.bp.blogspot.com/-A0NsVJu2Ay0/WGOgGNxAdTI/AAAAAAAABIY/amMTic8SsXYs7jfP_ITwBmkeVQHIAGZ-ACPcB/s1600/ENG-05-02-02-All-the-Pokemon-types.png', 'https://www.mandatory.gg/wp-content/uploads/mandatory-guide-pokemon-ecarlate-violet-table-types-forces-faiblesses.png', 'https://releasegaming.com/wp-content/uploads/2023/02/Pokemon-Type-Chart-Poster-960x850.jpg', 'https://img00.deviantart.net/2a60/i/2017/020/6/5/all_18_pokemon_types_by_pokemon_ranger_sumi-daw3v3d.jpg', 'http://fc09.deviantart.net/fs70/i/2013/318/0/f/pokemon_types_wheel_by_kamionero-d6u6o9i.png', 'https://static.wikia.nocookie.net/pokemongo/images/9/9c/Type_chart.png/revision/latest?cb=20191205150508', 'https://cdn1.vectorstock.com/i/1000x1000/03/95/pokemon-type-symbols-vector-2700395.jpg', 'https://orig00.deviantart.net/caf7/f/2014/046/7/2/pokemon_type_chart__offensive__by_lunicaura106-d76mcvb.png', 'https://videogamesuncovered.com/wp-content/uploads/2016/12/pokemon-types.jpg', 'https://i.ytimg.com/vi/H1w2VoRqmQQ/maxresdefault.jpg', 'https://pnghq.com/wp-content/uploads/pnghq.com-pokemon-types-png-3908-download-1024x987.png', 'https://i.pinimg.com/originals/91/69/dc/9169dce1568a24e4b0e0acb7f04ce728.jpg', 'https://i.etsystatic.com/21027128/r/il/fdbdba/2003255292/il_1588xN.2003255292_12o2.jpg', 'https://www.pokemoncenter.com/products/images/P2373PC/155-80156/P2373PC_155-80156_01.jpg', 'https://i.etsystatic.com/23914535/r/il/750695/2869449405/il_1588xN.2869449405_fr75.jpg', 'https://m.media-amazon.com/images/I/A1Ui8dsTSrS.jpg', 'https://www.totsafe.com/wp-content/uploads/2020/09/Gyarados-Ancient-Origins-Holo-1446x2048.jpg', 'https://i.pinimg.com/736x/83/e3/5a/83e35aead31fabb77b9bde3396d4351f.jpg', 'https://images.saymedia-content.com/.image/t_share/MTgzNzE1NDA2MDk0MDE3ODU1/best-vmax-pokemon-cards.png', 'https://i.pinimg.com/originals/18/28/97/18289747d16a23e3dc20cc36956b9b4b.jpg', 'https://pm1.narvii.com/6267/3e8dabe202aa4911724963a0eb1b1f0b0c875193_hq.jpg', 'https://i.pinimg.com/originals/d1/a5/fc/d1a5fc45abdf217f2ee641bb4975fa32.png', 'https://mlpnk72yciwc.i.optimole.com/cqhiHLc.WqA8~2eefa/w:auto/h:auto/q:75/https://bleedingcool.com/wp-content/uploads/2020/06/Charizard-grade-9-mint-front.jpg', 'https://images.saymedia-content.com/.image/t_share/MTc5ODE2MjE2Mjc2NDQ0Nzgz/best-v-pokemon-cards.jpg', 'https://cdn11.bigcommerce.com/s-0kvv9/images/stencil/1920w/products/371952/569692/pokemonevolvingskies041__83278.1630015209.jpg?c=2', 'https://cardmavin.com/wp-content/uploads/2016/11/pokemon-card.jpg', 'https://images-na.ssl-images-amazon.com/images/I/91UCqW1atmL.jpg', 'https://miro.medium.com/max/1400/1*I9DUHexc5eoKn1-dZs4g0A.jpeg', 'https://i2.wp.com/nypost.com/wp-content/uploads/sites/2/2020/12/pokemon-auction.jpg?quality=90&amp;strip=all&amp;ssl=1', 'http://images.nintendolife.com/news/2017/10/guide_getting_started_with_the_pokemon_trading_card_game/attachment/6/original.jpg', 'https://i1.wp.com/s3.amazonaws.com/media.completeset.com/stories/attachments/984/content_46-1.jpg?w=900', 'https://usercontent2.hubstatic.com/13535299_f120.jpg']
```

### blackpink

```python
from TheApi import api

result = await api.blackpink(query='pokemon', color='#ff94e0', border_color=None)
print(result)
```

```text
/home/runner/work/TheApi/TheApi/downloads/blackpink_07rcIKNP.jpg
```

### carbon

```python
from TheApi import api

result = await api.carbon(query='pokemon')
print(result)
```

```text
/home/runner/work/TheApi/TheApi/downloads/fcM8c2Vc.png
```

### cat

```python
from TheApi import api

result = await api.cat()
print(result)
```

```text
https://cdn2.thecatapi.com/images/Rscv6E1c5.jpg
```

### chatgpt

```python
from TheApi import api

result = await api.chatgpt(query='pokemon')
print(result)
```

```text
# Error:
Request failed: 400, message='Bad Request', url='https://chatwithai.codesearch.workers.dev/?chat=pokemon&model=gpt-4o'
```

### dog

```python
from TheApi import api

result = await api.dog()
print(result)
```

```text
https://random.dog/b85abb5b-5b9e-47d2-9938-71129cdfdb50.jpg
```

### fox

```python
from TheApi import api

result = await api.fox()
print(result)
```

```text
https://randomfox.ca/?i=85
```

### gen_hashtag

```python
from TheApi import api

result = await api.gen_hashtag(text='pokemon', similar=False)
print(result)
```

```text

```

### get_advice

```python
from TheApi import api

result = await api.get_advice()
print(result)
```

```text
Don't burn bridges.
```

### get_hindi_jokes

```python
from TheApi import api

result = await api.get_hindi_jokes()
print(result)
```

```text
रास्ते पलट देते हैं हमारे नौजवान जब कोई आकर यह कह दे कि आगे पुलिस वाले चालान काट रहे हैं 😆🤣😋😉
```

### get_jokes

```python
from TheApi import api

result = await api.get_jokes(amount=1)
print(result)
```

```text
The glass is neither half-full nor half-empty, the glass is twice as big as it needs to be.
```

### get_uselessfact

```python
from TheApi import api

result = await api.get_uselessfact()
print(result)
```

```text
Cats urine glows under a black light.
```

### github_search

```python
from TheApi import api

result = await api.github_search(query='pokemon', search_type='repositories', max_results=3)
print(result)
```

```text
[{'name': 'PokemonGo-Map', 'full_name': 'AHAAAAAAA/PokemonGo-Map', 'description': '🌏 Live visualization of all the pokemon in your area... and more! (shutdown)', 'url': 'https://github.com/AHAAAAAAA/PokemonGo-Map', 'language': None, 'stargazers_count': 7529, 'forks_count': 2815}, {'name': 'pokemon-showdown', 'full_name': 'smogon/pokemon-showdown', 'description': 'Pokémon battle simulator.', 'url': 'https://github.com/smogon/pokemon-showdown', 'language': 'TypeScript', 'stargazers_count': 4789, 'forks_count': 2796}, {'name': 'PokemonGo-Bot', 'full_name': 'PokemonGoF/PokemonGo-Bot', 'description': 'The Pokemon Go Bot, baking with community.', 'url': 'https://github.com/PokemonGoF/PokemonGo-Bot', 'language': 'Python', 'stargazers_count': 3870, 'forks_count': 1543}]
```

### hindi_quote

```python
from TheApi import api

result = await api.hindi_quote()
print(result)
```

```text
जिसने अपने को वश में कर लिया है, उसकी जीत को देवता भी हार में नही बदल सकते।
```

### meme

```python
from TheApi import api

result = await api.meme()
print(result)
```

```text
https://preview.redd.it/b2zh01zs350e1.png?width=320&crop=smart&auto=webp&s=e3ca3585990e96a9a6d9b2a9b4f5e861ce9e0df6
```

### pypi

```python
from TheApi import api

result = await api.pypi(package_name='pokemon')
print(result)
```

```text
{'name': 'pokemon', 'version': '0.36', 'summary': 'ascii database of pokemon... in Python!', 'author': 'Vanessa Sochat', 'author_email': 'vsoch@noreply.github.users.com', 'license': 'LICENSE', 'home_page': 'https://github.com/vsoch/pokemon', 'package_url': 'https://pypi.org/project/pokemon/', 'requires_python': '', 'keywords': 'pokemon,avatar,ascii,gravatar', 'classifiers': [], 'project_urls': {'Homepage': 'https://github.com/vsoch/pokemon'}}
```

### quote

```python
from TheApi import api

result = await api.quote()
print(result)
```

```text
We are all something, but none of us are everything.

author - Blaise Pascal
```

### random_word

```python
from TheApi import api

result = await api.random_word()
print(result)
```

```text
eases
```

### riddle

```python
from TheApi import api

result = await api.riddle()
print(result)
```

```text
{'riddle': 'I have no legs or arms but I still eat with a fork everyday, What am I?', 'answer': 'a snake'}
```

### stackoverflow_search

```python
from TheApi import api

result = await api.stackoverflow_search(query='pokemon', max_results=3, sort_type='relevance')
print(result)
```

```text
[{'tags': ['ios', 'flutter', 'dart'], 'owner': {'account_id': 19921816, 'reputation': 3, 'user_id': 14597469, 'user_type': 'registered', 'profile_image': 'https://lh6.googleusercontent.com/-aT6u2l_JT94/AAAAAAAAAAI/AAAAAAAAAAA/AMZuuclcxb94zp_q0Q2R8DQN7b6X3kgo6w/s96-c/photo.jpg?sz=256', 'display_name': 'Senem Sedef', 'link': 'https://stackoverflow.com/users/14597469/senem-sedef'}, 'is_answered': False, 'view_count': 117, 'answer_count': 0, 'score': 0, 'last_activity_date': 1701515081, 'creation_date': 1622231772, 'last_edit_date': 1701515081, 'question_id': 67744802, 'content_license': 'CC BY-SA 4.0', 'link': 'https://stackoverflow.com/questions/67744802/the-getter-pokemon-was-called-on-null-receiver-null-tried-calling-pokemon', 'title': 'The getter &#39;pokemon&#39; was called on null. Receiver: null Tried calling: pokemon'}, {'tags': ['reactjs', 'random', 'axios'], 'owner': {'account_id': 17931576, 'reputation': 1, 'user_id': 13028884, 'user_type': 'registered', 'profile_image': 'https://www.gravatar.com/avatar/7ebcdd2f784bca5dc54a1a0e17354f86?s=256&d=identicon&r=PG&f=y&so-version=2', 'display_name': 'GieGie', 'link': 'https://stackoverflow.com/users/13028884/giegie'}, 'is_answered': False, 'view_count': 1966, 'answer_count': 2, 'score': 0, 'last_activity_date': 1652730812, 'creation_date': 1642222168, 'last_edit_date': 1642223800, 'question_id': 70718940, 'content_license': 'CC BY-SA 4.0', 'link': 'https://stackoverflow.com/questions/70718940/pokemon-api-request-generate-5-pok%c3%a9mon-at-a-time', 'title': 'Pokemon API request generate 5 Pok&#233;mon at a time'}, {'tags': ['java'], 'owner': {'account_id': 919945, 'reputation': 43, 'user_id': 951797, 'user_type': 'registered', 'profile_image': 'https://www.gravatar.com/avatar/26b06d5d95992fa3780383abe5f49a3d?s=256&d=identicon&r=PG', 'display_name': 'Brian', 'link': 'https://stackoverflow.com/users/951797/brian'}, 'is_answered': True, 'view_count': 32622, 'accepted_answer_id': 7942409, 'answer_count': 3, 'score': 3, 'last_activity_date': 1577442848, 'creation_date': 1319931614, 'question_id': 7942384, 'content_license': 'CC BY-SA 3.0', 'link': 'https://stackoverflow.com/questions/7942384/simple-java-pokemon-fight-simulator', 'title': 'Simple Java Pokemon Fight Simulator'}]
```

### upload_image

```python
from TheApi import api

result = await api.upload_image(file_path='file/to/image')
print(result)
```

```text
You will get the URL for the image.
```

### wikipedia

```python
from TheApi import api

result = await api.wikipedia(query='pokemon')
print(result)
```

```text
{'title': 'Pokémon', 'summary': 'Pokémon is a Japanese media franchise consisting of video games, animated series and films, a trading card game, and other related media. The franchise takes place in a shared universe in which humans co-exist with creatures known as Pokémon, a large variety of species endowed with special powers. The franchise\'s target audience is children aged 5 to 12, but it is known to attract people of all ages.\nThe franchise originated as a pair of role-playing games developed by Game Freak, from an original concept by its founder, Satoshi Tajiri. Released on the Game Boy on February 27, 1996, the games became sleeper hits and were followed by manga series, a trading card game, and anime series and films. From 1998 to 2000, Pokémon was exported to the rest of the world, creating an unprecedented global phenomenon dubbed "Pokémania". By 2002, the craze had ended, after which Pokémon became a fixture in popular culture, with new products being released to this day. In the summer of 2016, the franchise spawned a second craze with the release of Pokémon Go, an augmented reality game developed by Niantic. Pokémon has since been estimated to be the world\'s highest-grossing media franchise and one of the best-selling video game franchises.\nPokémon has an uncommon ownership structure. Unlike most IPs, which are owned by one company, Pokémon is jointly owned by three: Nintendo, Game Freak, and Creatures. Game Freak develops the core series role-playing games, which are published by Nintendo exclusively for their consoles, while Creatures manages the trading card game and related merchandise, occasionally developing spin-off titles. The three companies established The Pokémon Company (TPC) in 1998 to manage the Pokémon property within Asia. The Pokémon anime series and films are co-owned by Shogakukan. Since 2009, The Pokémon Company International (TPCi), a subsidiary of TPC, has managed the franchise in all regions outside of Asia.', 'url': 'https://en.wikipedia.org/?curid=23745', 'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/9/98/International_Pok%C3%A9mon_logo.svg/500px-International_Pok%C3%A9mon_logo.svg.png'}
```

### words

```python
from TheApi import api

result = await api.words(num_words=5)
print(result)
```

```text
['etherealnesses', 'consignations', 'stonecrops', 'placatory', 'acylated']
```

### write

```python
from TheApi import api

result = await api.write(text='pokemon')
print(result)
```

```text
/home/runner/work/TheApi/TheApi/downloads/write_YBJ6N1hk.jpg
```


This Project is Licensed under [MIT License](https://github.com/Vivekkumar-IN/TheApi/blob/main/LICENSE)