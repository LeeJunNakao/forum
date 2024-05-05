from django.views import View
from django.db.models import Count
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from forum_core.models.topic import Topic
from forum_core.widgets.pagination import Pagination
from forum_core.forms.topic import ReplyForm, CreateTopicForm
from forum_core.widgets.titles import PageTitle

class TopicListView(View):
    @method_decorator(login_required(login_url="login"))
    def get(self, request):
        topics = Topic.objects.annotate(num_posts=Count('reply')).order_by("created_at")[:10]
        topics = topics.select_related("creator")
    
        return render(request, 'topic/list_topics.html', { "topics": topics })

class TopicCreateView(View):
    @method_decorator(login_required(login_url="login"))
    def get(self, request):

        form = CreateTopicForm()

        return render(request, 'topic/create_topic.html', { "title":  PageTitle().render("Create a new topic"), "form": form })
    
    @method_decorator(login_required(login_url="login"))
    def post(self, request):
        user = request.user
        form = CreateTopicForm(request.POST)
        if form.is_valid():
            topic = Topic(**form.cleaned_data, creator=user)
            topic.save()

            return redirect("homepage")

        return redirect("topic_create")

class TopicDetailsView(View):
    @method_decorator(login_required(login_url="login"))
    def get(self, request, id):
        topic = get_object_or_404(Topic, pk=id)
        posts = topic.reply_set.all()

        page = request.GET.get('page') or 1
        pagination = Pagination(data=posts)
        paginated_posts = pagination.get_page(page)

        return render(request, 'topic/topic.html', { "topic": topic, "posts": paginated_posts, "form": ReplyForm(), "id": id, "pagination": pagination.render(page) })

    @method_decorator(login_required(login_url="login"))
    def post(self, request, id):
        topic = get_object_or_404(Topic, pk=id)

        if 'save' in request.POST:
            self.reply_topic(request, topic)
        
        return redirect('topic_details', id=topic.id)

    def reply_topic(self, request, topic):
        form = ReplyForm(request.POST)

        if form.is_valid():
            reply = form.save(commit=False)
            reply.topic = topic
            reply.creator = request.user
            reply.save()

        
    
