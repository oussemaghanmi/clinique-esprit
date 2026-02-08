from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import RendezVous

@login_required
def appointment_list(request):
    rdv = RendezVous.objects.select_related('patient', 'medecin').order_by('date_heure')[:50]
    return render(request, 'appointments/list.html', {'rdv_list': rdv})
