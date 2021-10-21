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
    world_map.style = RS('#FF6E33', base_style=LCS)
    world_map.add('covid total cases', covid_total_cases)
    world_map.render_to_file('covid_stats/static/covid_stats/images/covid_total_cases.svg')

    return render(request, 'covid_stats/covid_total_cases.html')

def today_cases(request):
    url = 'https://disease.sh/v3/covid-19/countries'
    api_request = requests.get(url)

    if api_request.status_code != 200:
        print("failed to fetch the API...")
        quit()

    response = api_request.json()
    covid_today_cases = {}
    for country in response:
        if country["countryInfo"]["iso2"] == None:
            continue 

        covid_today_cases[country["countryInfo"]["iso2"].lower()] = country["todayCases"]


    world_map = pygal.maps.world.World()
    world_map.style = RS('#37807F', base_style=LCS)
    world_map.add('covid today cases', covid_today_cases)
    world_map.render_to_file('covid_stats/static/covid_stats/images/today_cases.svg')

    return render(request, 'covid_stats/today_cases.html')

def total_deaths(request):
    url = 'https://disease.sh/v3/covid-19/countries'
    api_request = requests.get(url)

    if api_request.status_code != 200:
        print("failed to fetch the API...")
        quit()

    response = api_request.json()
    covid_total_deaths = {}
    for country in response:
        if country["countryInfo"]["iso2"] == None:
            continue 

        covid_total_deaths[country["countryInfo"]["iso2"].lower()] = country["deaths"]


    world_map = pygal.maps.world.World()
    world_map.style = RS('#338BFF', base_style=LCS)
    world_map.add('covid total deaths', covid_total_deaths)
    world_map.render_to_file('covid_stats/static/covid_stats/images/total_deaths.svg')

    return render(request, 'covid_stats/total_deaths.html')

def cases_per_one_million(request):
    url = 'https://disease.sh/v3/covid-19/countries'
    api_request = requests.get(url)

    if api_request.status_code != 200:
        print("failed to fetch the API...")
        quit()

    response = api_request.json()
    covid_cases_per_one_million = {}
    for country in response:
        if country["countryInfo"]["iso2"] == None:
            continue 

        covid_cases_per_one_million[country["countryInfo"]["iso2"].lower()] = country["casesPerOneMillion"]


    world_map = pygal.maps.world.World()
    world_map.style = RS('#478641', base_style=LCS)
    world_map.add('covid cases per one million', covid_cases_per_one_million)
    world_map.render_to_file('covid_stats/static/covid_stats/images/cases_per_one_million.svg')

    return render(request, 'covid_stats/cases_per_one_million.html')
