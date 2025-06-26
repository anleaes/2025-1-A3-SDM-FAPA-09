from rest_framework import serializers
from .models import Especialidade, Profissional, ProfissionalEspecialidade

class EspecialidadeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Especialidade
        fields = '__all__'

class ProfissionalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profissional
        fields = '__all__'

class ProfissionalEspecialidadeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProfissionalEspecialidade
        fields = '__all__'
