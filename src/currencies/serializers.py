from currencies.models import ExchangeRate
from rest_framework import serializers


class ExchangeRateSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ExchangeRate
    fields = ('date', 'base_currency','target_currency','rate')