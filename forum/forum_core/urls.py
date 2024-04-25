from django.urls import path, include
from forum_core.views.topic import TopicListView, TopicDetailsView
from forum_core.views.auth import LoginView, LogoutView

urlpatterns = [
    path("", TopicListView.as_view(), name="homepage"),
    path("topic/<int:id>/", TopicDetailsView.as_view(), name='topic_details'),
    path("login", LoginView.as_view(), name="login"),
    path('logout', LogoutView.as_view(), name='logout')
]
