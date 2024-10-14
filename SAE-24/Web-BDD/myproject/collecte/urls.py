from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name='index'),
    path('collecte/capteurs/', views.liste_capteurs, name='liste_capteurs'),
    path('collecte/capteurs/ajouter/', views.ajouter_capteur, name='ajouter_capteur'),
    path('collecte/capteurs/modifier/<str:pk>/', views.modifier_capteur, name='modifier_capteur'),
    path('collecte/capteurs/supprimer/<str:pk>/', views.supprimer_capteur, name='supprimer_capteur'),
    path('collecte/donnees/', views.liste_donnees, name='liste_donnees'),
    path('collecte/donnees/ajouter/', views.ajouter_donnee, name='ajouter_donnee'),
    path('collecte/donnees/modifier/<int:pk>/', views.modifier_donnee, name='modifier_donnee'),
    path('collecte/donnees/supprimer/<int:pk>/', views.supprimer_donnee, name='supprimer_donnee'),
    path('collecte/rechercher/', views.rechercher, name='rechercher'),
    path('collecte/graphique/', views.graphique, name='graphique'),
    path('collecte/telecharger_donnees_csv/', views.telecharger_donnees_csv, name='telecharger_donnees_csv'),
]