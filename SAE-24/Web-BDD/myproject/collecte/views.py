from django.shortcuts import render, redirect, get_object_or_404
from .forms import CapteurForm, DonneeForm
from .models import Capteur, Donnee
from django.db.models import Q
from datetime import datetime
from django.db.models import Count
import csv
from django.http import HttpResponse
import os
from django.conf import settings


def index(request):
    return render(request, 'collecte/index.html')

def liste_capteurs(request):
    attribute = request.GET.get('attribute', 'id')
    order = request.GET.get('order', 'asc')
    filter_query = request.GET.get('filter_query', '')

    if order == 'asc':
        capteurs = Capteur.objects.order_by(attribute)
    else:
        capteurs = Capteur.objects.order_by(f'-{attribute}')

    if filter_query:
        capteurs = capteurs.filter(
            Q(id__contains=filter_query) |
            Q(nom__contains=filter_query) |
            Q(piece__contains=filter_query) |
            Q(emplacement__contains=filter_query)
        )

    context = {
        'capteurs': capteurs,
        'filter_query': filter_query,
    }
    return render(request, 'collecte/liste_capteurs.html', context)



def ajouter_capteur(request):
    if request.method == 'POST':
        form = CapteurForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('liste_capteurs')
    else:
        form = CapteurForm()
    return render(request, 'collecte/ajouter_capteur.html', {'form': form})


def modifier_capteur(request, pk):
    capteur = get_object_or_404(Capteur, pk=pk)
    if request.method == 'POST':
        form = CapteurForm(request.POST, instance=capteur)
        if form.is_valid():
            form.save()
            return redirect('liste_capteurs')
    else:
        form = CapteurForm(instance=capteur)
    return render(request, 'collecte/modifier_capteur.html', {'form': form})


def supprimer_capteur(request, pk):
    capteur = get_object_or_404(Capteur, pk=pk)
    if request.method == 'POST':
        capteur.delete()
        return redirect('liste_capteurs')
    return render(request, 'collecte/supprimer_capteur.html', {'capteur': capteur})


def liste_donnees(request):
    attribute = request.GET.get('attribute', 'id')
    order = request.GET.get('order', 'asc')
    filter_query = request.GET.get('filter_query', '')

    if order == 'asc':
        donnees = Donnee.objects.order_by(attribute)
    else:
        donnees = Donnee.objects.order_by(f'-{attribute}')

    if filter_query:
        donnees = donnees.filter(
            Q(id__icontains=filter_query) |
            Q(capteur__nom__icontains=filter_query) |
            Q(timestamp__icontains=filter_query) |
            Q(temperature__icontains=filter_query) |
            Q(presence__icontains=filter_query) |
            Q(nombre_individus__icontains=filter_query)
        )

    context = {
        'donnees': donnees,
        'filter_query': filter_query
    }
    return render(request, 'collecte/liste_donnees.html', context)

def ajouter_donnee(request):
    if request.method == 'POST':
        form = DonneeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('liste_donnees')
    else:
        form = DonneeForm()
    
    return render(request, 'collecte/ajouter_donnee.html', {'form': form})



def modifier_donnee(request, pk):
    donnee = get_object_or_404(Donnee, pk=pk)
    if request.method == 'POST':
        form = DonneeForm(request.POST, instance=donnee)
        if form.is_valid():
            form.save()
            return redirect('liste_donnees')
    else:
        form = DonneeForm(instance=donnee)
    return render(request, 'collecte/modifier_donnee.html', {'form': form})


def supprimer_donnee(request, pk):
    donnee = get_object_or_404(Donnee, pk=pk)
    if request.method == 'POST':
        donnee.delete()
        return redirect('liste_donnees')
    return render(request, 'collecte/supprimer_donnee.html', {'donnee': donnee})

def rechercher(request):
    if 'query' in request.GET:
        query = request.GET['query']
        capteurs = Capteur.objects.filter(Q(nom__icontains=query) | Q(piece__icontains=query) | Q(emplacement__icontains=query))
        donnees = Donnee.objects.filter(Q(capteur__nom__icontains=query) | Q(presence__icontains=query) | Q(nombre_individus__icontains=str(query)))

        try:
            timestamp_query = datetime.strptime(query, "%Y-%m-%d %H:%M:%S")
            donnees = donnees | Donnee.objects.filter(timestamp=timestamp_query)
        except ValueError:
            pass

        results = {
            'capteurs': capteurs,
            'donnees': donnees,
        }   
    else:
        results = {}

    return render(request, 'collecte/search_results.html', {'results': results})

def graphique(request):
    capteurs = Capteur.objects.all()

    attributs = ['temperature', 'presence', 'nombre_individus']

    capteurs_json = []
    for capteur in capteurs:
        donnees = capteur.donnee_set.all().values('timestamp', 'temperature', 'presence', 'nombre_individus')
        capteurs_json.append({
            'nom': capteur.nom,
            'piece': capteur.piece,
            'emplacement': capteur.emplacement,
            'donnees': list(donnees)
        })

    context = {
        'capteurs': capteurs,
        'attributs': attributs,
        'capteurs_json': capteurs_json
    }

    return render(request, 'collecte/graphique.html', context)


def telecharger_donnees_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="donnees.csv"'

    writer = csv.writer(response)
    writer.writerow(['ID Capteur', 'Nom Capteur', 'Pièce', 'Emplacement', 'ID Donnée', 'Timestamp', 'Température', 'Présence', 'Nombre d\'individus'])

    capteurs = Capteur.objects.all()
    for capteur in capteurs:
        donnees = capteur.donnee_set.all()
        for donnee in donnees:
            writer.writerow([capteur.id, capteur.nom, capteur.piece, capteur.emplacement, donnee.id, donnee.timestamp, donnee.temperature, donnee.presence, donnee.nombre_individus])

    return response