from django.contrib import admin
from .models import Patient, ConsultationMedicale

@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ['numero_dossier', 'nom', 'prenom', 'date_naissance', 'telephone', 'actif']
    list_filter = ['sexe', 'actif', 'groupe_sanguin']
    search_fields = ['numero_dossier', 'nom', 'prenom', 'telephone', 'email']
    readonly_fields = ['date_creation', 'date_modification']
    
    fieldsets = (
        ('Informations personnelles', {
            'fields': ('numero_dossier', 'nom', 'prenom', 'date_naissance', 'sexe')
        }),
        ('Contact', {
            'fields': ('telephone', 'email', 'adresse', 'ville', 'code_postal')
        }),
        ('Informations médicales', {
            'fields': ('groupe_sanguin', 'allergies', 'antecedents_medicaux')
        }),
        ('Métadonnées', {
            'fields': ('actif', 'date_creation', 'date_modification'),
            'classes': ('collapse',)
        }),
    )

@admin.register(ConsultationMedicale)
class ConsultationMedicaleAdmin(admin.ModelAdmin):
    list_display = ['patient', 'medecin', 'date_consultation', 'motif']
    list_filter = ['date_consultation', 'medecin']
    search_fields = ['patient__nom', 'patient__prenom', 'motif', 'diagnostic']
    date_hierarchy = 'date_consultation'
    readonly_fields = ['date_creation']
