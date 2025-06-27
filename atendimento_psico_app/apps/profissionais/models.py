from django.db import models

class Especialidade(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    
    class Meta:
        verbose_name = 'Especialidade'
        verbose_name_plural = 'Especialidade'
        ordering =['id']

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
    
    photo = models.ImageField('Foto do Profissional', upload_to='photos/profissionais')
    
    class Meta:
        verbose_name = 'Profissionais'
        verbose_name_plural = 'Profissionais'
        ordering =['id']

    def __str__(self):
        return self.name


class ProfissionalEspecialidade(models.Model):
    profissional = models.ForeignKey(Profissional, on_delete=models.CASCADE)
    especialidade = models.ForeignKey(Especialidade, on_delete=models.CASCADE)
    
    class Meta:
        unique_together = ('profissional', 'especialidade')

    def __str__(self):
        return f"{self.profissional.name} - {self.especialidade.name}"
