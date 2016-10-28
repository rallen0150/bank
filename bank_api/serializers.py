from rest_framework import serializers

from bank.models import Transaction

class BalanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields='__all__'
