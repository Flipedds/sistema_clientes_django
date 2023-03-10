from django.urls import path
from .views import CustomerlistView, CustomerCreateView
app_name = "customer"

urlpatterns = [
    path('list/', CustomerlistView.as_view(), name="customer-list"),
    path('', CustomerCreateView.as_view(), name="customer-create"),
]