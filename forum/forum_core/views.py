from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.db.models import Count
from .models import Topic, Reply
from forum_core.forms import ReplyForm
from forum_core.widgets import Pagination

def reply_topic(request, topic):
    form = ReplyForm(request.POST)
    if form.is_valid():
        reply = form.save(commit=False)
        reply.topic = topic
        reply.creator = request.user
        reply.save()
        return redirect('topic_details', id=topic.id)

def list_topics(request):
    topics = Topic.objects.annotate(num_posts=Count('reply')).order_by("created_at")[:10]
    topics = topics.select_related("creator")

    return render(request, 'list_topics.html', { "topics": topics })

def topic_details(request, id):
    topic = get_object_or_404(Topic, pk=id)
    posts = topic.reply_set.all()

    page = request.GET.get('page') or 1
    pagination = Pagination(data=posts)
    paginated_posts = pagination.get_page(page)

    if request.method == 'POST':
        if 'save' in request.POST:
            reply_topic(request, topic)

    return render(request, 'topic.html', { "topic": topic, "posts": paginated_posts, "form": ReplyForm(), "id": id, "pagination": pagination.render(page) })