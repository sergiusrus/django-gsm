from django.contrib.auth.models import User
from rest_framework.serializers import ModelSerializer

from organizations.models import Organization, Shop


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']


class ShopSerializer(ModelSerializer):
    class Meta:
        model = Shop
        fields = ['name', 'description', 'address', 'index']


class OrganizationSerializer(ModelSerializer):
    shops = ShopSerializer(many=True, read_only=True)

    class Meta:
        model = Organization
        fields = ['name', 'description', 'shops']


class ShopDetailSerializer(ModelSerializer):
    class Meta:
        model = Shop
        fields = '__all__'


class ShopDetailUserSerializer(ModelSerializer):
    users = UserSerializer(many=True, read_only=True)

    class Meta:
        model = Shop
        fields = ['users']
