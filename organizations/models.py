from django.contrib.auth.models import User
from django.db import models


class Organization(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class Shop(models.Model):
    organization_id = models.ForeignKey(Organization, on_delete=models.CASCADE, related_name='shops')
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True, null=True)
    address = models.CharField(max_length=50)
    index = models.PositiveIntegerField(default=0)
    is_deleted = models.BooleanField(default=False)
    users = models.ManyToManyField(User, related_name='shop_users')

    @property
    def organization_name(self):
        return self.organization_id.name

    def __str__(self):
        return self.name
