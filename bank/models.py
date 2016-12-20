from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

## Found this on a website to help generate a token to a new user
from rest_framework.authtoken.models import Token
from django.conf import settings

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)


OPTION = [
    ('W', 'Withdraw'),
    ('D', 'Deposit'),
]


class Transaction(models.Model):
    user = models.ForeignKey('auth.User')
    num1 = models.FloatField()
    operator1 = models.CharField(max_length=1, choices=OPTION)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ("created", )

@receiver(post_save, sender=User)
def create(**kwargs):
    created = kwargs['created']
    instance = kwargs['instance']
    if created:
        Profile.objects.create(user=instance)

class Profile(models.Model):
    user = models.OneToOneField('auth.User')

    @property
    def balance(self):
        deposit_total = 0
        withdraw_total = 0
        transactions = Transaction.objects.filter(user=self.user)
        for transaction in transactions:
            if transaction.operator1 =='D':
                deposit_total += transaction.num1
            else:
                withdraw_total += transaction.num1
        return round(deposit_total - withdraw_total, 2)
