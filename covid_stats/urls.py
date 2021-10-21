from django.urls import path

from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('world_population/', views.world_population, name='world_population'),
    path('covid_total_cases/', views.covid_total_cases, name='covid_total_cases'),
    path('today_cases/', views.today_cases, name='today_cases'),
    path('total_deaths/', views.total_deaths, name='total_deaths'),
    path('cases_per_one_million/', views.cases_per_one_million, name='cases_per_one_million'),
]