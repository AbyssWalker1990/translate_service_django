from django.shortcuts import render
from django.http import HttpResponse

def translations(request):
    return render(request, 'translations.html')


