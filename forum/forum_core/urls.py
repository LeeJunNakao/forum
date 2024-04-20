from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.list_topics),
    path("topic/<int:id>/", views.topic_details)
]
