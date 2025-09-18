from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from myapp.models import Client, Order
from .serializers import ClientSerializer, OrderSerializer
from .permissions import IsClientOwner
from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework.decorators import action
from rest_framework.response import Response
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page


class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    permission_classes = [IsAuthenticated]


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated, IsClientOwner]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['date_order']


class PublicProductViewSet(ReadOnlyModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    @action(detail=True, methods=['post'])
    def cancelar(self, request, pk=None):
        order = self.get_object()
        if order.status != 'pendente':
            return Response({'error': 'Pedido não pode ser cancelado.'}, status=400)
        order.status = 'cancelado'
        order.save()
        return Response({'status': 'Pedido cancelado com sucesso.'})

    @method_decorator(cache_page(30))
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
