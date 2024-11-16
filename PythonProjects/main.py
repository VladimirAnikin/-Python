import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '3a318bb05b9e9ecc5af849e349d1cc57'
HEADER = {'Content-Type':'application/json','trainer_token':TOKEN}
body_registration = {
    "trainer_token": TOKEN,
    "email": "avg7555anikin@yandex.ru",
    "password": "P1e9r9u5n33"
}
body_confirmation = {
    "trainer_token" : TOKEN
}
body_create = {
    "name": "Бульбазавр",
    "photo_id": 1
}

body_change = {
    "pokemon_id": "134148",
    "name": "123",
    "photo_id": 1
}

body_catch = {
    "pokemon_id": "134501"
}

'''response = requests.post(url = f'{URL}/trainers/reg', headers = HEADER, json = body_registration)
print(response.text)'''

'''response_create = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = body_create)
print(response_create.text)'''

'''response_change = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = body_change)
print(response_change.text)'''

response_catch = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADER, json = body_catch)
print(response_catch.text)

message = response_catch.json()['message']