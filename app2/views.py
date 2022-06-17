from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def kohli(request):
    return HttpResponse('kohli is one of the best batsman')