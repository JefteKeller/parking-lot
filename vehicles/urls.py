from django.urls import path

from .views import CreateUpdateVehicleView

urlpatterns = [
    path('vehicles/', CreateUpdateVehicleView.as_view()),
    path('vehicles/<int:vehicle_id>/', CreateUpdateVehicleView.as_view()),
]
