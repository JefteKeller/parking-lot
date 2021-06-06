from django.urls import path

from .views import CreateListLevelView

urlpatterns = [
    path('levels/', CreateListLevelView.as_view()),
]
