from django.db import models
from apps.profissionais.models import Profissional
from apps.pacientes.models import Paciente
# Create your models here.


class Atendimento(models.Model):
    profissional = models.ForeignKey(Profissional, on_delete=models.CASCADE)
    cliente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    status = models.BooleanField(default=True)
    data = models.DateField()

    def __str__(self):
        return f"{self.profissional} - {self.cliente} - {self.data}"
