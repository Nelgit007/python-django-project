from django.shortcuts import render

from .models import Topic

# Create your views here.

def index(request):
    """Home page for learning_logs app"""
    return render(request, 'learning_logs/index.html')

def topics(request):
    """Displays all topic in learning log app"""
    topics = Topic.objects.order_by('date_added')
    context = {'topics': topics}
    return render(request, 'learning_logs/topics.html', context)

def topic(request, topic_id):
    """Display a sngle topic entry and details entered"""
    topic = Topic.objects.get(id=topic_id)
    entries = topic.entry_set.order_by('date_added')
    context = {'topic': topic, 'entries': entries}
    return render(request, 'learning_logs/topic.html', context)


