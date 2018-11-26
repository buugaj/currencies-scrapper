from django.db import models

# Create your models here.
class Currency(models.Model):
    code = models.CharField(max_length=3, primary_key=True)

class ExchangeRate(models.Model):
    date = models.DateTimeField()
    base_currency = models.ForeignKey(Currency,related_name='base_currency', on_delete=models.PROTECT)
    target_currency = models.ForeignKey(Currency,related_name='target_currency', on_delete=models.PROTECT)
    rate = models.DecimalField(max_digits=16,decimal_places=8)


