from rest_framework import serializers
from .models import Medicamento
class MedicamentoSerializer(serializers.ModelSerializer):
    categoria_nome = serializers.CharField(source='category.name', read_only=True)

    class Meta:
        model = Medicamento
        fields = ['id', 'name', 'description', 'price', 'category', 'categoria_nome']
