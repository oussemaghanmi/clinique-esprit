from django.db import models
from django.contrib.auth.models import User

class Patient(models.Model):
    SEXE_CHOICES = [
        ('M', 'Masculin'),
        ('F', 'Féminin'),
    ]
    
    GROUPE_SANGUIN_CHOICES = [
        ('A+', 'A+'), ('A-', 'A-'),
        ('B+', 'B+'), ('B-', 'B-'),
        ('AB+', 'AB+'), ('AB-', 'AB-'),
        ('O+', 'O+'), ('O-', 'O-'),
    ]
    
    # Informations personnelles
    numero_dossier = models.CharField(max_length=20, unique=True, verbose_name="Numéro de dossier")
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100, verbose_name="Prénom")
    date_naissance = models.DateField(verbose_name="Date de naissance")
    sexe = models.CharField(max_length=1, choices=SEXE_CHOICES)
    
    # Contact
    telephone = models.CharField(max_length=20, verbose_name="Téléphone")
    email = models.EmailField(blank=True, null=True)
    adresse = models.TextField()
    ville = models.CharField(max_length=100)
    code_postal = models.CharField(max_length=10)
    
    # Informations médicales
    groupe_sanguin = models.CharField(max_length=3, choices=GROUPE_SANGUIN_CHOICES, blank=True)
    allergies = models.TextField(blank=True)
    antecedents_medicaux = models.TextField(blank=True, verbose_name="Antécédents médicaux")
    
    # Métadonnées
    date_creation = models.DateTimeField(auto_now_add=True)
    date_modification = models.DateTimeField(auto_now=True)
    actif = models.BooleanField(default=True)
    
    class Meta:
        ordering = ['-date_creation']
        verbose_name = 'Patient'
        verbose_name_plural = 'Patients'
    
    def __str__(self):
        return f"{self.numero_dossier} - {self.nom} {self.prenom}"
    
    @property
    def nom_complet(self):
        return f"{self.prenom} {self.nom}"

class ConsultationMedicale(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='consultations')
    medecin = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, verbose_name="Médecin")
    date_consultation = models.DateTimeField()
    motif = models.CharField(max_length=200)
    symptomes = models.TextField(verbose_name="Symptômes")
    diagnostic = models.TextField()
    traitement_prescrit = models.TextField()
    observations = models.TextField(blank=True)
    
    date_creation = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-date_consultation']
        verbose_name = 'Consultation médicale'
        verbose_name_plural = 'Consultations médicales'
    
    def __str__(self):
        return f"Consultation {self.patient} - {self.date_consultation.strftime('%d/%m/%Y')}"
