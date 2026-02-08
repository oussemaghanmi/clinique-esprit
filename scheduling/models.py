from django.db import models
from appointments.models import Medecin

class PlageHoraire(models.Model):
    JOURS_SEMAINE = [
        (0, 'Lundi'),
        (1, 'Mardi'),
        (2, 'Mercredi'),
        (3, 'Jeudi'),
        (4, 'Vendredi'),
        (5, 'Samedi'),
        (6, 'Dimanche'),
    ]
    
    medecin = models.ForeignKey(Medecin, on_delete=models.CASCADE, related_name='plages_horaires', verbose_name="Médecin")
    jour_semaine = models.IntegerField(choices=JOURS_SEMAINE)
    heure_debut = models.TimeField(verbose_name="Heure de début")
    heure_fin = models.TimeField(verbose_name="Heure de fin")
    actif = models.BooleanField(default=True)
    
    class Meta:
        ordering = ['jour_semaine', 'heure_debut']
        verbose_name = 'Plage horaire'
        verbose_name_plural = 'Plages horaires'
        unique_together = ['medecin', 'jour_semaine', 'heure_debut']
    
    def __str__(self):
        return f"{self.medecin} - {self.get_jour_semaine_display()} {self.heure_debut}-{self.heure_fin}"

class Absence(models.Model):
    TYPE_CHOICES = [
        ('CONGE', 'Congé'),
        ('FORMATION', 'Formation'),
        ('MALADIE', 'Maladie'),
        ('AUTRE', 'Autre'),
    ]
    
    medecin = models.ForeignKey(Medecin, on_delete=models.CASCADE, related_name='absences', verbose_name="Médecin")
    date_debut = models.DateField(verbose_name="Date de début")
    date_fin = models.DateField(verbose_name="Date de fin")
    type_absence = models.CharField(max_length=10, choices=TYPE_CHOICES)
    motif = models.TextField(blank=True)
    
    class Meta:
        ordering = ['-date_debut']
        verbose_name = 'Absence'
        verbose_name_plural = 'Absences'
    
    def __str__(self):
        return f"{self.medecin} - {self.get_type_absence_display()} ({self.date_debut} au {self.date_fin})"
