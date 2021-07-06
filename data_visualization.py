import requests
import pygal
from pygal.style import LightColorizedStyle as LCS, RotateStyle as RS, LightenStyle as LS 

url = 'https://disease.sh/v3/covid-19/countries'
request = requests.get(url)

if request.status_code != 200:
    print("failed to fetch the API...")
    quit()

response = request.json()

world_population = {}
for country in response:
    if country["countryInfo"]["iso2"] == None:
       continue 
    world_population[country["countryInfo"]["iso2"].lower()] = country["population"]

world_map = pygal.maps.world.World()
world_map.style = RS('#FFF033', base_style=LCS)
world_map.add('world population', world_population)
world_map.render_to_file('world_map.svg')


