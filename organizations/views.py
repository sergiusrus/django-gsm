from drf_renderer_xlsx.mixins import XLSXFileMixin
from drf_renderer_xlsx.renderers import XLSXRenderer
from rest_framework import generics
from rest_framework.viewsets import ReadOnlyModelViewSet

from organizations.models import Organization, Shop
from organizations.serializers import OrganizationSerializer, ShopDetailSerializer


class OrganizationList(generics.ListAPIView):
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer


class OrganizationListFile(XLSXFileMixin, ReadOnlyModelViewSet):
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer
    renderer_classes = [XLSXRenderer]
    filename = 'export.xlsx'


class ShopUpdate(generics.UpdateAPIView):
    queryset = Shop.objects.all()
    serializer_class = ShopDetailSerializer
