from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return HttpReponse('<h1>Blog Home</h1>')


def about(request):
    return HttpReponse('<h1>Blog About</h1>')


