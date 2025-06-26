from django.shortcuts import render
from rest_framework import viewsets
from .models import Prescricao, MedicamentoItem
from .serializer import PrescricaoSerializer, MedicamentoItemSerializer
# Create your views here.

class PrescricaoViewSet(viewsets.ModelViewSet):
    queryset = Prescricao.objects.all()
    serializer_class = PrescricaoSerializer

class MedicamentoItemViewSet(viewsets.ModelViewSet):
    queryset = MedicamentoItem.objects.all()
    serializer_class = MedicamentoItemSerializer
