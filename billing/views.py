from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Facture

@login_required
def facture_list(request):
    factures = Facture.objects.select_related('patient').order_by('-date_emission')[:50]
    return render(request, 'billing/list.html', {'factures': factures})
