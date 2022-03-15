from asgiref.sync import async_to_sync
from drf_renderer_xlsx.mixins import XLSXFileMixin
from drf_renderer_xlsx.renderers import XLSXRenderer
from rest_framework import generics
from rest_framework.viewsets import ReadOnlyModelViewSet
from channels.layers import get_channel_layer

from gsm_app.tasks import send_email_from_put
from organizations.models import Organization, Shop
from organizations.serializers import OrganizationSerializer, ShopDetailSerializer, ShopDetailUserSerializer


class OrganizationList(generics.ListAPIView):
    queryset = Organization.objects.all().prefetch_related('shops')
    serializer_class = OrganizationSerializer


class OrganizationListFile(XLSXFileMixin, ReadOnlyModelViewSet):
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer
    renderer_classes = [XLSXRenderer]
    filename = 'export.xlsx'


class ShopUpdate(generics.UpdateAPIView):
    queryset = Shop.objects.all().prefetch_related('users')
    serializer_class = ShopDetailSerializer

    def put(self, request, *args, **kwargs):
        _send_to_websocket(self.get_object())
        send_email_from_put()
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        _send_to_websocket(self.get_object())
        send_email_from_put()
        return self.update(request, *args, **kwargs)


class ShopDetailUserList(generics.RetrieveAPIView):
    queryset = Shop.objects.all()
    serializer_class = ShopDetailUserSerializer


def _send_to_websocket(obj):
    shop = Shop.objects.values().get(pk=obj.id)
    channel_layer = get_channel_layer()
    async_to_sync(channel_layer.group_send)("shop", {
        "type": "shop.message",
        "text": shop
    })
