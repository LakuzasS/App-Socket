from django.urls import path
from gestionnaire import views

urlpatterns = [
    path('', views.accueil, name='accueil'),
    
    # Étudiants
    path('gestionnaire/etudiants/', views.liste_etudiants, name='liste_etudiants'),
    path('gestionnaire/etudiants/ajouter/', views.ajouter_etudiant, name='ajouter_etudiant'),
    path('gestionnaire/etudiants/modifier/<int:numero_etudiant>/', views.modifier_etudiant, name='modifier_etudiant'),
    path('gestionnaire/etudiants/supprimer/<int:numero_etudiant>/', views.supprimer_etudiant, name='supprimer_etudiant'),
    
    # Unités d'enseignement
    path('gestionnaire/unites/', views.liste_unites, name='liste_unites'),
    path('gestionnaire/unites/ajouter/', views.ajouter_unite, name='ajouter_unite'),
    path('gestionnaire/unites/modifier/<str:code>/', views.modifier_unite, name='modifier_unite'),
    path('gestionnaire/unites/supprimer/<str:code>/', views.supprimer_unite, name='supprimer_unite'),
    
    # Ressources
    path('gestionnaire/ressources/', views.liste_ressources, name='liste_ressources'),
    path('gestionnaire/ressources/ajouter/', views.ajouter_ressource, name='ajouter_ressource'),
    path('gestionnaire/ressources/modifier/<str:code_ressource>/', views.modifier_ressource, name='modifier_ressource'),
    path('gestionnaire/ressources/supprimer/<str:code_ressource>/', views.supprimer_ressource, name='supprimer_ressource'),
    
    # Enseignants
    path('gestionnaire/enseignants/', views.liste_enseignants, name='liste_enseignants'),
    path('gestionnaire/enseignants/ajouter/', views.ajouter_enseignant, name='ajouter_enseignant'),
    path('gestionnaire/enseignants/modifier/<int:enseignant_id>/', views.modifier_enseignant, name='modifier_enseignant'),
    path('gestionnaire/enseignants/supprimer/<int:enseignant_id>/', views.supprimer_enseignant, name='supprimer_enseignant'),
    
    # Examens
    path('gestionnaire/examens/', views.liste_examens, name='liste_examens'),
    path('gestionnaire/examens/ajouter/', views.ajouter_examen, name='ajouter_examen'),
    path('gestionnaire/examens/modifier/<int:examen_id>/', views.modifier_examen, name='modifier_examen'),
    path('gestionnaire/examens/supprimer/<int:examen_id>/', views.supprimer_examen, name='supprimer_examen'),
    
    # Notes
    path('gestionnaire/notes/', views.liste_notes, name='liste_notes'),
    path('gestionnaire/notes/ajouter/', views.ajouter_note, name='ajouter_note'),
    path('gestionnaire/notes/modifier/<int:pk>/', views.modifier_note, name='modifier_note'),
    path('gestionnaire/notes/supprimer/<int:pk>/', views.supprimer_note, name='supprimer_note'),

    path('gestionnaire/rechercher/', views.rechercher, name='rechercher'),
    path('gestionnaire/choose_student/', views.choose_student, name='choose_student'),
    path('gestionnaire/generate_transcript/<int:student_id>/', views.generate_transcript, name='generate_transcript'),
]

