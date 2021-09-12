from django.urls import path

from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('world_population/', views.world_population, name='world_population'),
    path('covid_total_cases/', views.covid_total_cases, name='covid_total_cases'),
]