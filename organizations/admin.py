from django.contrib import admin

from organizations.models import Organization, Shop


@admin.register(Organization)
class OrganizationAdmin(admin.ModelAdmin):
    pass


@admin.register(Shop)
class ShopAdmin(admin.ModelAdmin):
    list_display = ('name', 'organization_name', 'is_deleted')
