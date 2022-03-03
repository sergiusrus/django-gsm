from django.urls import path

from organizations import views

urlpatterns = [
    path('organization/', views.OrganizationList.as_view()),
    path('organization/file/', views.OrganizationListFile.as_view({'get': 'list'})),
    path('shops/<int:pk>/', views.ShopUpdate.as_view()),
]
