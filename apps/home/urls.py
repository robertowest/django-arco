from django.urls import path

from . import views

app_name = 'homepage'

urlpatterns = [
    path('original/', views.home, name='original'),
    path('', views.IndexView.as_view(), name='home'),
]
