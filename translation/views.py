from django.shortcuts import render

def translations(request):
    return render(request, 'translations.html')


