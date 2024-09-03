from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics
from .serializers import menuSerializer
from .models import Menu

# Create your views here.
def index(request):
    return render(request, 'index.html', {})

  
class MenutItemView(generics.ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = menuSerializer

class SingleMenuItemView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = menuSerializer

