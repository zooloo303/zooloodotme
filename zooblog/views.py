import os
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Post
from .models import ChatMessage
from .forms import PostForm
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(
    api_key = os.getenv("OPENAI_API_KEY"),
)

# Create your views here.
def index(request):
    posts = Post.objects.all()
    return render(request, 'index.html', {'posts': posts})

def about(request):
    return render(request, 'about.html')
    
def chatbot(request):
    return render(request, 'chatbot.html')

# functions for use within the app
def getResponse(request):
    userMessage = request.GET.get('userMessage')
    
    chat_completion = client.chat.completions.create(
        messages=[
        {"role": "user", 
        "content": userMessage
        }
    ],
        model="gpt-4-0125-preview",
    )
    botsResponse = (chat_completion.choices[0].message)

    return HttpResponse(botsResponse.content) # this will be sent back to the client

def add_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = PostForm()
    return render(request, 'add_post.html', {'form': form})

@login_required
def chat_view(request):
    if request.method == 'POST':
        message_text = request.POST.get('message')
        ChatMessage.objects.create(user=request.user, message=message_text)
        return redirect('chat_url')  # Replace 'chat_url' with the name of your chat URL.

    messages = ChatMessage.objects.all().order_by('-timestamp')
    return render(request, 'chatbot.html', {'messages': messages})