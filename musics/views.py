from django.shortcuts import render
from musics.models import Music
from rest_framework import viewsets
# Create your views here.
class MusicViewSet(viewsets.ModelViewSet):
    queryset = Music.objects.all()

def about(request):
    """
    About page view.
    """
    return render(request, 'about.html', {
        'title': 'About Us'
    })