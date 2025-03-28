from django.db import models
from django.contrib.auth.models import User

class Automobil(models.Model):
    marca = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    matricula = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.matricula} - {self.marca} {self.model}"

class Reserva(models.Model):
    automobil = models.ForeignKey(Automobil, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    data_inici = models.DateField()
    data_fi = models.DateField()

    class Meta:
        unique_together = ('automobil', 'data_inici') 

    def __str__(self):
        return f"Reserva de {self.automobil} per {self.user} del {self.data_inici} al {self.data_fi}"
