from django.shortcuts import render

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login

from django.views.generic import TemplateView, DetailView, ListView
from django.views.generic.edit import CreateView, FormView
from django.urls import reverse_lazy

from bank.models import Transaction, Profile

class IndexView(TemplateView):
    template_name = "index.html"

    def get_context_data(self):
        context = super().get_context_data()
        context['login'] = AuthenticationForm
        return context

class UserCreateView(FormView):
    template_name = "auth/user_form.html"
    model = User
    form_class = UserCreationForm
    success_url = reverse_lazy('index_view')

    def form_valid(self, form):
      #save the new user first
      form.save()
      #get the username and password
      username = self.request.POST['username']
      password = self.request.POST['password1']
      #authenticate user then login
      user = authenticate(username=username, password=password)
      login(self.request, user)
      return super(UserCreateView, self).form_valid(form)

class BalanceCreateView(CreateView):
    model = Transaction
    success_url = reverse_lazy('balance_create_view')
    fields = ('num1', 'operator1')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["transaction"] = Transaction.objects.filter(user=self.request.user)
        return context

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.user = self.request.user
        return super().form_valid(form)

class TransactionDetailView(ListView):
    model = Transaction

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["accounts"] = Transaction.objects.filter(user=self.request.user)
        return context

class TransferCreateView(CreateView):
    model = Transaction
    fields = ("user", "num1")
    success_url = reverse_lazy('balance_create_view')

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.operator1 = "D"
        x = Profile.objects.get(id=instance.user.id)
        if not x:
            instance.user = self.request.user.user


        Transaction.objects.create(operator1='W', num1=instance.num1, user=self.request.user)
        return super().form_valid(form)
