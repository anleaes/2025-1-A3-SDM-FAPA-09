from django.shortcuts import render
from rest_framework import viewsets
from .models import Medicamento
from .serializer import MedicamentoSerializer
# Create your views here.


class MedicamentoViewSet(viewsets.ModelViewSet):
    queryset = Medicamento.objects.all()
    serializer_class = MedicamentoSerializer
