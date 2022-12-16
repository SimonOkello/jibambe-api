from django.urls import path
from . import views

urlpatterns = [
    path('pay/',views.PayAPIView.as_view(),name='payment-api'),
]
