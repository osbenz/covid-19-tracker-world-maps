from django.shortcuts import render
import requests
import pygal
from pygal.style import LightColorizedStyle as LCS, RotateStyle as RS, LightenStyle as LS 

def index(request):
    return render(request, 'covid_stats/index.html')

def world_population(request):
    url = 'https://disease.sh/v3/covid-19/countries'
    api_request = requests.get(url)

    if api_request.status_code != 200:
        print("failed to fetch the API...")
        quit()

    response = api_request.json()
    world_population = {}
    for country in response:
        if country["countryInfo"]["iso2"] == None:
            continue 

        world_population[country["countryInfo"]["iso2"].lower()] = country["population"]


    world_map = pygal.maps.world.World()
    world_map.style = RS('#FFF033', base_style=LCS)
    world_map.add('world population', world_population)
    world_map.render_to_file('covid_stats/static/covid_stats/images/world_population.svg')

    return render(request, 'covid_stats/world_population.html')

def covid_total_cases(request):
    url = 'https://disease.sh/v3/covid-19/countries'
    api_request = requests.get(url)

    if api_request.status_code != 200:
        print("failed to fetch the API...")
        quit()

    response = api_request.json()
    covid_total_cases = {}
    for country in response:
        if country["countryInfo"]["iso2"] == None:
            continue 

        covid_total_cases[country["countryInfo"]["iso2"].lower()] = country["cases"]


    world_map = pygal.maps.world.World()
    world_map.style = RS('#FFF033', base_style=LCS)
    world_map.add('covid total cases', covid_total_cases)
    world_map.render_to_file('covid_stats/static/covid_stats/images/covid_total_cases.svg')

    return render(request, 'covid_stats/covid_total_cases.html')

