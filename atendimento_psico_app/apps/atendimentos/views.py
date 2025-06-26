from django.shortcuts import render
from rest_framework import viewsets
from .models import Atendimento
from .serializer import AtendimentoSerializer
# Create your views here.


class AtendimentoViewSet(viewsets.ModelViewSet):
    queryset = Atendimento.objects.all()
    serializer_class = AtendimentoSerializer