from django.shortcuts import render
from django.http import HttpResponse


def list_topics(request):
    return render(request, 'list_topics.html')