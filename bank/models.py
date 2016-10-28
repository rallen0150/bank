from django.db import models


OPTION = [
    ('+', '+'),
    ('-', '-'),
]


class Transaction(models.Model):
    user = models.ForeignKey('auth.User')
    num1 = models.FloatField()
    num2 = models.FloatField(null=True, blank=True, default=0)
    num3 = models.FloatField(null=True, blank=True, default=0)
    operator1 = models.CharField(max_length=1, choices=OPTION)
    operator2 = models.CharField(max_length=1, null=True, blank=True, choices=OPTION)
    operator3 = models.CharField(max_length=1, null=True, blank=True, choices=OPTION)
    created = models.DateTimeField(auto_now_add=True)

    @property
    def calc_total(self):
        num1, operator1, num2, operator2, num3, operator3 = [self.num1, self.operator1, self.num2,
                                                             self.operator2, self.num3, self.operator3]
        if operator1 == '-':
            if operator2 == '-':
                if operator3 == '-':
                    return round(-num1 - num2 - num3, 2)
                elif operator3 == '+':
                    return round(-num1 - num2 + num3, 2)
                else:
                    return round(-num1 - num2, 2)
            elif operator2 == '+':
                if operator3 == '-':
                    return round(-num1 + num2 - num3, 2)
                elif operator3 == '+':
                    return round(-num1 + num2 + num3, 2)
                else:
                    return round(-num1 + num2, 2)
            else:
                return round(-num1, 2)
        else:
            if operator2 == '-':
                if operator3 == '-':
                    return round(num1 - num2 - num3, 2)
                elif operator3 == '+':
                    return round(num1 - num2 + num3, 2)
                else:
                    return round(num1 - num2, 2)
            elif operator2 == '+':
                if operator3 == '-':
                    return round(num1 + num2 - num3, 2)
                elif operator3 == '+':
                    return round(num1 + num2 + num3, 2)
                else:
                    return round(num1 + num2, 2)
            else:
                return round(num1, 2)
