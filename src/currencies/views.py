from rest_framework import viewsets, pagination
from currencies.models import ExchangeRate
from currencies.serializers import ExchangeRateSerializer

class StandardResultsSetPagination(pagination.PageNumberPagination):
    page_size = 100
    page_size_query_param = 'page_size'
    max_page_size = 1000

class ExchangeRateViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = ExchangeRate.objects.all()
    serializer_class = ExchangeRateSerializer
    pagination_class = StandardResultsSetPagination
