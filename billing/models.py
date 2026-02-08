from django.db import models
from patients.models import Patient, ConsultationMedicale
from decimal import Decimal

class Facture(models.Model):
    STATUT_CHOICES = [
        ('BROUILLON', 'Brouillon'),
        ('EMISE', 'Émise'),
        ('PAYEE', 'Payée'),
        ('PARTIELLE', 'Paiement partiel'),
        ('ANNULEE', 'Annulée'),
    ]
    
    numero_facture = models.CharField(max_length=20, unique=True, verbose_name="Numéro de facture")
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='factures')
    consultation = models.ForeignKey(ConsultationMedicale, on_delete=models.SET_NULL, null=True, blank=True)
    
    date_emission = models.DateField(auto_now_add=True, verbose_name="Date d'émission")
    date_echeance = models.DateField(verbose_name="Date d'échéance")
    statut = models.CharField(max_length=10, choices=STATUT_CHOICES, default='BROUILLON')
    
    montant_ht = models.DecimalField(max_digits=10, decimal_places=3, verbose_name="Montant HT")
    tva = models.DecimalField(max_digits=5, decimal_places=2, default=19.00, verbose_name="TVA (%)")
    montant_ttc = models.DecimalField(max_digits=10, decimal_places=3, verbose_name="Montant TTC")
    montant_paye = models.DecimalField(max_digits=10, decimal_places=3, default=0, verbose_name="Montant payé")
    
    notes = models.TextField(blank=True)
    
    class Meta:
        ordering = ['-date_emission']
        verbose_name = 'Facture'
        verbose_name_plural = 'Factures'
    
    def __str__(self):
        return f"Facture {self.numero_facture} - {self.patient}"
    
    def save(self, *args, **kwargs):
        # Calcul automatique TTC
        self.montant_ttc = self.montant_ht * (Decimal('1') + self.tva / Decimal('100'))
        super().save(*args, **kwargs)
    
    @property
    def reste_a_payer(self):
        return self.montant_ttc - self.montant_paye

class LigneFacture(models.Model):
    facture = models.ForeignKey(Facture, on_delete=models.CASCADE, related_name='lignes')
    designation = models.CharField(max_length=200, verbose_name="Désignation")
    quantite = models.IntegerField(default=1, verbose_name="Quantité")
    prix_unitaire = models.DecimalField(max_digits=10, decimal_places=3, verbose_name="Prix unitaire")
    montant_total = models.DecimalField(max_digits=10, decimal_places=3, verbose_name="Montant total")
    
    def save(self, *args, **kwargs):
        self.montant_total = Decimal(self.quantite) * self.prix_unitaire
        super().save(*args, **kwargs)
    
    def __str__(self):
        return f"{self.designation} - {self.montant_total} TND"

class Paiement(models.Model):
    MODE_CHOICES = [
        ('ESPECES', 'Espèces'),
        ('CHEQUE', 'Chèque'),
        ('CARTE', 'Carte bancaire'),
        ('VIREMENT', 'Virement'),
    ]
    
    facture = models.ForeignKey(Facture, on_delete=models.CASCADE, related_name='paiements')
    date_paiement = models.DateTimeField(auto_now_add=True)
    montant = models.DecimalField(max_digits=10, decimal_places=3)
    mode_paiement = models.CharField(max_length=10, choices=MODE_CHOICES)
    reference = models.CharField(max_length=100, blank=True, verbose_name="Référence")
    notes = models.TextField(blank=True)
    
    class Meta:
        ordering = ['-date_paiement']
        verbose_name = 'Paiement'
        verbose_name_plural = 'Paiements'
    
    def __str__(self):
        return f"Paiement {self.montant} TND - {self.facture.numero_facture}"
