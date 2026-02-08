from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.db.models import Count, Sum
from django.utils import timezone
from datetime import timedelta

from patients.models import Patient, ConsultationMedicale
from appointments.models import RendezVous
from billing.models import Facture, Paiement

@login_required
def dashboard_view(request):
    """Dashboard principal avec statistiques"""
    
    # Statistiques
    total_patients = Patient.objects.filter(actif=True).count()
    
    # Rendez-vous aujourd'hui
    today = timezone.now().date()
    rdv_today = RendezVous.objects.filter(
        date_heure__date=today,
        statut__in=['ATTENTE', 'CONFIRME']
    ).count()
    
    # Revenu du mois
    first_day_month = today.replace(day=1)
    revenus_mois = Paiement.objects.filter(
        date_paiement__gte=first_day_month
    ).aggregate(total=Sum('montant'))['total'] or 0
    
    # Factures en attente
    factures_attente = Facture.objects.filter(
        statut__in=['EMISE', 'BROUILLON']
    ).aggregate(total=Sum('montant_ttc'))['total'] or 0
    
    context = {
        'total_patients': total_patients,
        'rdv_today': rdv_today,
        'revenus_mois': revenus_mois,
        'factures_attente': factures_attente,
    }
    
    return render(request, 'dashboard/index.html', context)
