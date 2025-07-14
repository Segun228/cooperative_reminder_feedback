from django.urls import path, include
from .views import getFeedbackView


urlpatterns = [
    path('api/', getFeedbackView.as_view(), name="get-feedback-endpoint"),
]
