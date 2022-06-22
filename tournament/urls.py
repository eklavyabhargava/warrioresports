from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('tdm/', views.tdm, name='teamdeathmatch'),
    path('tdm/success/', views.tdm, name='success'),
    path('classic/', views.classic, name='classicmatch'),
    path('tdm/success/', views.tdm, name='success'),
]