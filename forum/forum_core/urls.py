from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.list_topics, name="homepage"),
    path("topic/<int:id>/", views.topic_details, name='topic_details'),
    path("login", views.login, name="login"),
    path('logout', views.logout, name='logout')
]
