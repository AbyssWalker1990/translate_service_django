from django.shortcuts import render
from .models import TranslationCard

def translations(request):
    cards = TranslationCard.objects.all()
    print(cards)
    context = {'cards': cards}
    return render(request, 'translations.html', context)


