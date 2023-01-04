from django.shortcuts import render
from .models import TranslationCard

def translations(request):
    cards = TranslationCard.objects.all()
    print(cards)
    context = {'cards': cards}
    return render(request, 'translations.html', context)


def translation_single(request, pk):
    card = TranslationCard.objects.get(id=pk)
    context = {"card": card}
    return render(request, 'translation-single.html', context)


