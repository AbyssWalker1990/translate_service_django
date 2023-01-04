from django.urls import path
from . import views

urlpatterns = [
    path('', views.translations, name="translations"),
    path('translation/<str:pk>/', views.translation_single, name="translation-single")
]