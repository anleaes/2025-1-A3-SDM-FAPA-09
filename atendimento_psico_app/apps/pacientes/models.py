from django.db import models

# Create your models here.

class Paciente(models.Model):
    GENDER_CHOICES = [
        ('M', 'Masculino'),
        ('F', 'Feminino'),
        ('O', 'Outro'),
    ]
    name = models.CharField(max_length=100)
    cell_phone = models.CharField(max_length=15)
    email = models.EmailField(unique=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    
    photo = models.ImageField('Foto do Paciente', upload_to='photos/pacientes')
    
    class Meta:
        verbose_name = 'Pacientes'
        verbose_name_plural = 'Pacientes'
        ordering =['id']

    def __str__(self):
        return self.name
