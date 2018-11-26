from django.db import models
# Create your models here.

class CurrencyManager(models.Manager):
    def bulk_insert_new(self, currency_code_set):
        values = self.filter(code__in=currency_code_set)
        set_copy = list(currency_code_set)
        for value in values:
            if value.code in set_copy:
                set_copy.remove(value.code)
        new_currencies = []
        for value in set_copy:
            new_currencies.append(Currency(code=value))
        self.bulk_create(new_currencies)

class Currency(models.Model):
    code = models.CharField(max_length=3, primary_key=True)
    objects = CurrencyManager()

class ExchangeRateManager(models.Manager):
    def bulk_insert_or_update_insert_new_related(self, scrap_result_set):
        currency_codes_set = set()
        for rate in scrap_result_set:
            currency_codes_set.add(rate.base_currency)
            currency_codes_set.add(rate.target_currency)
        Currency.objects.bulk_insert_new(currency_codes_set)
        values = { currency.code: currency for currency in Currency.objects.filter(code__in=currency_codes_set)}
        for rate in scrap_result_set:
            ExchangeRate.objects.update_or_create(
                date = rate.date, base_currency = values[rate.base_currency], target_currency = values[rate.target_currency],
                rate = rate.exchange_rate
            )

class ExchangeRate(models.Model):
    date = models.DateTimeField()
    base_currency = models.ForeignKey(Currency,related_name='base_currency', on_delete=models.PROTECT)
    target_currency = models.ForeignKey(Currency,related_name='target_currency', on_delete=models.PROTECT)
    rate = models.DecimalField(max_digits=16,decimal_places=8)
    objects = ExchangeRateManager()


