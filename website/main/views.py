from django.http import response
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')
# Create your views here.

def about(request):
    return render(request, 'main/index.html')
