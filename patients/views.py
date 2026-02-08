from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Patient

@login_required
def patient_list(request):
    patients = Patient.objects.filter(actif=True).order_by('-date_creation')[:50]
    return render(request, 'patients/list.html', {'patients': patients})
