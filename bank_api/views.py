from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from bank_api.serializers import BalanceSerializer
from bank.models import Transaction

class BalanceListCreateAPIView(ListCreateAPIView):
    queryset = Transaction.objects.all()
    serializer_class = BalanceSerializer

class BalanceDetailUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Transaction.objects.all()
    serializer_class = BalanceSerializer
