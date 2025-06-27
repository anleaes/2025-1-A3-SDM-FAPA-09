from django.db import models
from atendimentos.models import Atendimento
from medicamentos.models import Medicamento
# Create your models here.

class Prescricao(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    total_medicamento = models.IntegerField()
    atendimento = models.ForeignKey(Atendimento, on_delete=models.CASCADE)
    
    doc = models.FileField('Documentos', upload_to='docs')
    
    class Meta:
        verbose_name = 'Prescricoes'
        verbose_name_plural = 'Prescricoes'
        ordering =['id']

    def __str__(self):
        return f"{self.name} - {self.atendimento}"
    
    @property
    def total_medicamento(self):
        return self.itens.count()
    
class MedicamentoItem(models.Model):
    prescricao = models.ForeignKey(Prescricao, on_delete=models.CASCADE, related_name='itens')
    medicamento = models.ForeignKey(Medicamento, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.medicamento.name} - {self.prescricao.name}"
