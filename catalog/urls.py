from django.urls import path

from catalog.apps import CatalogConfig
from catalog.views import homepage, contacts

app_name = CatalogConfig.name

urlpatterns = [
    path('', homepage),
    path('contacts/', contacts)
]