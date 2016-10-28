from django.contrib import admin
from bank.models import Transaction, Profile

admin.site.register([Transaction, Profile])
