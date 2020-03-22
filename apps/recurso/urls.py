from django.urls import path

from . import views

app_name = 'recurso'

urlpatterns = [
    path('', views.RecursoTemplateView.as_view(), name='index'),
    path('list/', views.RecursoListView.as_view(), name='list'),
]
