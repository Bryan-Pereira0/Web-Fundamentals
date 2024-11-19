import requests

url = "https://pokeapi.co/api/v2/pokemon/pikachu"

response = requests.get(url)
data = response.json()

name = data['name']

abilities = [ability['ability']['name'] for ability in data['abilities']]

print(f"{name} can use: ")
for ability in abilities:
    print(f"{ability}")

def fetch_pokemon_data(pokemon_name):
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_name}"
    response = requests.get(url)
    data = response.json()
    return data

def calculate_average_weight(pokemon_list):
    total_weight = 0
    for pokemon in pokemon_list:
        total_weight += pokemon['weight']
    avg_weight = total_weight / len(pokemon_list)
    print(f"The average weight of the pokemon is {avg_weight}")


pokemon_names = ["pikachu", "bulbasaur", "charmander"]

calculate_average_weight([fetch_pokemon_data(name) for name in pokemon_names])