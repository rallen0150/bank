from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView

from bank.models import Transaction
from django.urls import reverse_lazy

class IndexView(TemplateView):
    template_name = "index.html"

class UserCreateView(CreateView):
    model = User
    form_class = UserCreationForm
    success_url = reverse_lazy('index_view')

class BalanceCreateView(CreateView):
    model = Transaction
    success_url = reverse_lazy('balance_create_view')
    fields = ('num1', 'operator1', 'num2', 'operator2', 'num3', 'operator3')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["transaction"] = Transaction.objects.all()
        return context

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.user = self.request.user
        return super().form_valid(form)
