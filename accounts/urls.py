from django.urls import path

from rest_framework.authtoken import views
from .views import CreateAdminUserView

urlpatterns = [
    path('accounts/', CreateAdminUserView.as_view()),
    path('login/', views.obtain_auth_token),
]
