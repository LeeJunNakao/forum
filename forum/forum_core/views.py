from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate, login as do_login, logout as do_logout
from django.db.models import Count
from django.contrib.auth.decorators import login_required
from .models import Topic
from forum_core.forms.topic import ReplyForm
from forum_core.forms.auth import LoginForm
from forum_core.widgets import Pagination



def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)

        user = authenticate(username=form['username'].value(), password=form['password'].value())
        if user is not None:
            do_login(request, user)
            return redirect('homepage')


    return render(request, 'auth/login.html', { "login_form": LoginForm()})

def logout(request):
    do_logout(request)
    return redirect('homepage')


@login_required(login_url="login")
def list_topics(request):
    topics = Topic.objects.annotate(num_posts=Count('reply')).order_by("created_at")[:10]
    topics = topics.select_related("creator")
    
    return render(request, 'list_topics.html', { "topics": topics })

def reply_topic(request, topic):
    form = ReplyForm(request.POST)
    if form.is_valid():
        reply = form.save(commit=False)
        reply.topic = topic
        reply.creator = request.user
        reply.save()
        return redirect('topic_details', id=topic.id)
    
@login_required(login_url="login")
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