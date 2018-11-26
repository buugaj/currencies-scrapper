from rest_framework import viewsets, pagination
from currencies.models import ExchangeRate
from currencies.serializers import ExchangeRateSerializer
from rest_framework.decorators import action
from rest_framework.response import Response

class StandardResultsSetPagination(pagination.PageNumberPagination):
    page_size = 100
    page_size_query_param = 'page_size'
    max_page_size = 1000

class ExchangeRateViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = ExchangeRate.objects.all().order_by('-date')
    serializer_class = ExchangeRateSerializer
    pagination_class = StandardResultsSetPagination

    @action(detail=False)
    def latest(self, request):
        current =  ExchangeRate.objects.all().order_by('base_currency', 'target_currency', '-date', 'rate').distinct('base_currency','target_currency')
        serializer = self.get_serializer(current, many=True)
        return Response(serializer.data)