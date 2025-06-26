from rest_framework import serializers
from .models import Prescricao, MedicamentoItem

class MedicamentoItemSerializer(serializers.ModelSerializer):
    medicamento_nome = serializers.CharField(source='medicamento.name', read_only=True)

    class Meta:
        model = MedicamentoItem
        fields = ['id', 'prescricao', 'medicamento', 'medicamento_nome']

class PrescricaoSerializer(serializers.ModelSerializer):
    total_medicamento = serializers.ReadOnlyField()
    itens = MedicamentoItemSerializer(many=True, read_only=True)

    class Meta:
        model = Prescricao
        fields = ['id', 'name', 'description', 'atendimento', 'total_medicamento', 'itens']
