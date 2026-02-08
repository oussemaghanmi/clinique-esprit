from django.contrib import admin
from .models import Medecin, RendezVous

@admin.register(Medecin)
class MedecinAdmin(admin.ModelAdmin):
    list_display = ['user', 'specialite', 'numero_ordre', 'telephone_cabinet']
    list_filter = ['specialite']
    search_fields = ['user__first_name', 'user__last_name', 'numero_ordre']

@admin.register(RendezVous)
class RendezVousAdmin(admin.ModelAdmin):
    list_display = ['patient', 'medecin', 'date_heure', 'duree_minutes', 'statut']
    list_filter = ['statut', 'medecin', 'date_heure']
    search_fields = ['patient__nom', 'patient__prenom', 'motif']
    date_hierarchy = 'date_heure'
    readonly_fields = ['date_creation', 'date_modification']
