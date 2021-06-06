from django.urls import path

from .views import CreatePricingView

urlpatterns = [
    path('pricings/', CreatePricingView.as_view()),
]
