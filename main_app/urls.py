from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('characters/', views.characters_index, name='characters_index'),
  path('characters/<int:character_id>/', views.characters_detail, name='characters_detail'),
]