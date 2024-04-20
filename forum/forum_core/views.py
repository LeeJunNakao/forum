from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Count
from .models import Post, Topic


def list_topics(request):
    topics = Topic.objects.annotate(num_posts=Count('post')).order_by("created_at")[:10]
    return render(request, 'list_topics.html', { "topics": topics })

def topic_details(request, id):
    topic = Topic.objects.get(id=id)
    return render(request, 'topic.html', { "topic": topic })