from django.urls import path

from rest_framework.authtoken.views import obtain_auth_token
from .views import CreateAdminUserView, LoginAdminUserView

urlpatterns = [
    path('accounts/', CreateAdminUserView.as_view()),
    # path('login/', LoginAdminUserView.as_view()),
    path('login/', obtain_auth_token),
]
