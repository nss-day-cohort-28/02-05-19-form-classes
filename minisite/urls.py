from django.urls import path
from . import views

app_name = 'minisite'
urlpatterns = [
    # home
    path('', views.index, name='index'),
    path('dogs/new', views.dogNew, name='dog_new'),
]
