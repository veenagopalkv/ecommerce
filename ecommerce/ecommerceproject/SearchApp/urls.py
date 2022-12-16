from django.urls import path
from . import views
app_name='SearchApp'
urlpatterns=[
    path("",views.searchResults,name='searchResults')
]