from django.contrib import admin
from django.urls import path
from django.urls.conf import include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(('covid_stats.urls', 'covid_stats'), namespace='covid_stats')),
]