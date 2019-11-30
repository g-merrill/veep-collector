from django.shortcuts import render
from .models import Character, Quote

# Create your views here.
def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def characters_index(request):
  characters = Character.objects.all()
  return render(request, 'characters/index.html', { 'characters': characters })

def characters_detail(request, character_id):
  character = Character.objects.get(id=character_id)
  quotes = Quote.objects.filter(said_by_id=character.id)
  rec_quotes = Quote.objects.filter(aimed_at_id=character.id)
  return render(request, 'characters/detail.html', { 'character': character, 'quotes': quotes, 'rec_quotes': rec_quotes })