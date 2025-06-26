from django.db import models

class Especialidade(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name


class Profissional(models.Model):
    GENDER_CHOICES = [
        ('M', 'Masculino'),
        ('F', 'Feminino'),
        ('O', 'Outro'),
    ]
    name = models.CharField(max_length=100)
    cell_phone = models.CharField(max_length=15)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)

    def __str__(self):
        return self.name


class ProfissionalEspecialidade(models.Model):
    profissional = models.ForeignKey(Profissional, on_delete=models.CASCADE)
    especialidade = models.ForeignKey(Especialidade, on_delete=models.CASCADE)
    
    class Meta:
        unique_together = ('profissional', 'especialidade')

    def __str__(self):
        return f"{self.profissional.name} - {self.especialidade.name}"
