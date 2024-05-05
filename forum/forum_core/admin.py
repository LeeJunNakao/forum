from django.contrib import admin
from .models.topic import Topic, Reply
from .models.settings import UserProfile

admin.site.register(Topic)
admin.site.register(Reply)
admin.site.register(UserProfile)
