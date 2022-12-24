from django.urls import include, path
from rest_framework import routers

from Data import views
# from customers import views as customer_views

# router = routers.SimpleRouter()

# router.register(r'customer', customer_views.CustomerViewSet,
#                 basename="customer")

router = routers.DefaultRouter()
router.register(r'TiVA', views.TiVAViewSet, basename="TiVA_crud")
