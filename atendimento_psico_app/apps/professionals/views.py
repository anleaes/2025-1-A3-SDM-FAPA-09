from django.shortcuts import render
from rest_framework import viewsets
from .models import Especialidade, Profissional, ProfissionalEspecialidade
from .serializer import EspecialidadeSerializer, ProfissionalSerializer, ProfissionalEspecialidadeSerializer
# Create your views here.


class EspecialidadeViewSet(viewsets.ModelViewSet):
    queryset = Especialidade.objects.all()
    serializer_class = EspecialidadeSerializer

class ProfissionalViewSet(viewsets.ModelViewSet):
    queryset = Profissional.objects.all()
    serializer_class = ProfissionalSerializer

class ProfissionalEspecialidadeViewSet(viewsets.ModelViewSet):
    queryset = ProfissionalEspecialidade.objects.all()
    serializer_class = ProfissionalEspecialidadeSerializer
