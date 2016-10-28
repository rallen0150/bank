from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from bank_api.serializers import BalanceSerializer
from bank_api.permission import IsUser
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from bank.models import Transaction, Profile

class BalanceListCreateAPIView(ListCreateAPIView):
    queryset = Transaction.objects.all()
    serializer_class = BalanceSerializer
    permission_classes = (IsAuthenticated, )

    def get(self, request, format=None):
        contents = {
            'status': 'You are permitted to view your OWN records'
        }
        return Response(contents)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
        return super().perform_create(serializer)

class BalanceDetailUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Transaction.objects.all()
    serializer_class = BalanceSerializer
    permission_classes = (IsUser, )
