from rest_framework.serializers import ModelSerializer

from organizations.models import Organization, Shop


class ShopSerializer(ModelSerializer):
    class Meta:
        model = Shop
        fields = ['name', 'description', 'address', 'index']


class OrganizationSerializer(ModelSerializer):
    shops = ShopSerializer(many=True, source='get_active_shops')

    class Meta:
        model = Organization
        fields = ['name', 'description', 'shops']


class ShopDetailSerializer(ModelSerializer):
    class Meta:
        model = Shop
        fields = '__all__'

