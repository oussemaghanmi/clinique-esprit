from django.contrib import admin
from .models import Facture, LigneFacture, Paiement

class LigneFactureInline(admin.TabularInline):
    model = LigneFacture
    extra = 1

class PaiementInline(admin.TabularInline):
    model = Paiement
    extra = 0
    readonly_fields = ['date_paiement']

@admin.register(Facture)
class FactureAdmin(admin.ModelAdmin):
    list_display = ['numero_facture', 'patient', 'date_emission', 'montant_ttc', 'statut']
    list_filter = ['statut', 'date_emission']
    search_fields = ['numero_facture', 'patient__nom', 'patient__prenom']
    date_hierarchy = 'date_emission'
    readonly_fields = ['date_emission', 'montant_ttc']
    inlines = [LigneFactureInline, PaiementInline]
    
    fieldsets = (
        ('Informations générales', {
            'fields': ('numero_facture', 'patient', 'consultation', 'statut')
        }),
        ('Montants', {
            'fields': ('montant_ht', 'tva', 'montant_ttc', 'montant_paye', 'date_echeance')
        }),
        ('Notes', {
            'fields': ('notes',),
            'classes': ('collapse',)
        }),
    )

@admin.register(Paiement)
class PaiementAdmin(admin.ModelAdmin):
    list_display = ['facture', 'montant', 'mode_paiement', 'date_paiement']
    list_filter = ['mode_paiement', 'date_paiement']
    search_fields = ['facture__numero_facture', 'reference']
    readonly_fields = ['date_paiement']
