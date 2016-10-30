from django import forms
from bank.models import Transaction

class TransferForm(forms.ModelForm):
    class Meta:
        fields = ("user", "num1")
        model = Transaction
