from django.contrib import admin
from .models import PlageHoraire, Absence

@admin.register(PlageHoraire)
class PlageHoraireAdmin(admin.ModelAdmin):
    list_display = ['medecin', 'jour_semaine', 'heure_debut', 'heure_fin', 'actif']
    list_filter = ['jour_semaine', 'actif', 'medecin']
    search_fields = ['medecin__user__first_name', 'medecin__user__last_name']

@admin.register(Absence)
class AbsenceAdmin(admin.ModelAdmin):
    list_display = ['medecin', 'type_absence', 'date_debut', 'date_fin']
    list_filter = ['type_absence', 'date_debut']
    search_fields = ['medecin__user__first_name', 'medecin__user__last_name', 'motif']
    date_hierarchy = 'date_debut'
