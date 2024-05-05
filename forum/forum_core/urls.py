from django.urls import path, include
from forum_core.views.topic import TopicListView, TopicDetailsView, TopicCreateView
from forum_core.views.auth import LoginView, LogoutView, RegisterView
from forum_core.views.settings import SettingsView

urlpatterns = [
    path("", TopicListView.as_view(), name="homepage"),
    path("topic/<int:id>/", TopicDetailsView.as_view(), name='topic_details'),
    path("topic/new/", TopicCreateView.as_view(), name='topic_create'),
    path("login", LoginView.as_view(), name="login"),
    path("register", RegisterView.as_view(), name="register"),
    path('logout', LogoutView.as_view(), name='logout'),
    path('settings', SettingsView.as_view(), name="settings")
]
