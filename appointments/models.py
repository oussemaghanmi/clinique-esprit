from django.db import models
from django.contrib.auth.models import User
from patients.models import Patient

class Medecin(models.Model):
    SPECIALITES = [
        ('GEN', 'Médecine générale'),
        ('CARD', 'Cardiologie'),
        ('DERM', 'Dermatologie'),
        ('PED', 'Pédiatrie'),
        ('ORT', 'Orthopédie'),
        ('OPH', 'Ophtalmologie'),
        ('GYN', 'Gynécologie'),
        ('NEUR', 'Neurologie'),
        ('PSY', 'Psychiatrie'),
    ]
    
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    specialite = models.CharField(max_length=4, choices=SPECIALITES, verbose_name="Spécialité")
    numero_ordre = models.CharField(max_length=50, unique=True, verbose_name="Numéro d'ordre")
    telephone_cabinet = models.CharField(max_length=20, verbose_name="Téléphone cabinet")
    bio = models.TextField(blank=True, verbose_name="Biographie")
    
    class Meta:
        verbose_name = 'Médecin'
        verbose_name_plural = 'Médecins'
    
    def __str__(self):
        return f"Dr. {self.user.get_full_name()} - {self.get_specialite_display()}"

class RendezVous(models.Model):
    STATUT_CHOICES = [
        ('ATTENTE', 'En attente'),
        ('CONFIRME', 'Confirmé'),
        ('ANNULE', 'Annulé'),
        ('TERMINE', 'Terminé'),
    ]
    
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='rendez_vous')
    medecin = models.ForeignKey(Medecin, on_delete=models.CASCADE, related_name='rendez_vous', verbose_name="Médecin")
    date_heure = models.DateTimeField(verbose_name="Date et heure")
    duree_minutes = models.IntegerField(default=30, verbose_name="Durée (minutes)")
    motif = models.CharField(max_length=200)
    statut = models.CharField(max_length=10, choices=STATUT_CHOICES, default='ATTENTE')
    notes = models.TextField(blank=True)
    
    date_creation = models.DateTimeField(auto_now_add=True)
    date_modification = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['date_heure']
        verbose_name = 'Rendez-vous'
        verbose_name_plural = 'Rendez-vous'
        unique_together = ['medecin', 'date_heure']
    
    def __str__(self):
        return f"{self.patient} - {self.medecin} - {self.date_heure.strftime('%d/%m/%Y %H:%M')}"
