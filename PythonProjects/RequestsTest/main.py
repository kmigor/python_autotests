import requests


#создание покемона
responseForCreate = requests.post(
    url='https://api.pokemonbattle.me:9104/pokemons' , 
    json = {
        "name": "Бульбазавр",
        "photo": "https://dolnikov.ru/pokemons/albums/001.png"
    },
    headers={
        'trainer_token' : 'c2aeccd8a035f5e9f1e27a542fdb7d4d',
        'Content-Type' : 'application/json'
    }
)

pokemonId = responseForCreate.json()['id']
pokemonPhoto = "https://dolnikov.ru/pokemons/albums/001.png"

print(responseForCreate.json())

# смена имени
responseForRename = requests.put(
    url='https://api.pokemonbattle.me:9104/pokemons' , 
    json = {
    "pokemon_id": pokemonId,
    "name": "Pokemon",
    "photo": pokemonPhoto
    },
    headers={
        'trainer_token' : 'enterYourToken',
        'Content-Type' : 'application/json'
    }
)
print(responseForRename.json())

# ловля покемона в покебол
responseForCatchPokemon = requests.post(
    url='https://api.pokemonbattle.me:9104/trainers/add_pokeball' , 
    json = {
    "pokemon_id": pokemonId,
    },
    headers={
        'trainer_token' : 'enterYourToken',
        'Content-Type' : 'application/json'
    }
)
print(responseForCatchPokemon.json())