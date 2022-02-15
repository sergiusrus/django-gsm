from drf_renderer_xlsx.mixins import XLSXFileMixin
from drf_renderer_xlsx.renderers import XLSXRenderer
from rest_framework import generics
from rest_framework.viewsets import ReadOnlyModelViewSet

from organizations.models import Organization
from organizations.serializers import OrganizationSerializer


class OrganizationList(generics.ListAPIView):
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer


class OrganizationListFile(XLSXFileMixin, ReadOnlyModelViewSet):
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer
    renderer_classes = [XLSXRenderer]
    filename = 'export.xlsx'
