import requests

def fetch_planet_data():
    url = "https://api.le-systeme-solaire.net/rest/bodies/"
    response = requests.get(url)
    planets = response.json()['bodies']
    
    planet_list = []
    for planet in planets:
        if planet['isPlanet']:
            name = planet['englishName']
            mass = planet['mass']['massValue']
            mass_exponent = planet['mass']['massExponent']
            orbit_period = planet['sideralOrbit']
            planet_list.append({'name': name,
                                'mass': mass * 10**mass_exponent,
                                'orbit_period': orbit_period
            })
    return planet_list

def find_heaviest_planet(planet_list):
    heaviest_planet = max(planet_list, key=lambda p: p['mass'])
    return heaviest_planet['name'], heaviest_planet['mass']


planets = fetch_planet_data()
print(planets)
name, mass = find_heaviest_planet(planets)
print(f"The heaviest planet is {name} with a mass of {mass} kg")
    