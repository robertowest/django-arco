from django.urls import path

from . import views

app_name = 'homepage'

urlpatterns = [
    path('', views.home, name='home'),
    path('original/', views.original, name='original'),
    # path('', views.IndexView.as_view(), name='home'),
]
