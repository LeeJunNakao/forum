from django.contrib import admin
from .models.topic import Topic, Reply

admin.site.register(Topic)
admin.site.register(Reply)
