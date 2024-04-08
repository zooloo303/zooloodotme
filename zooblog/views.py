import os
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Post
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

def getResponse(request):
    userMessage = request.GET.get('userMessage')
    
    chat_completion = client.chat.completions.create(
        messages=[
        {"role": "user", 
        "content": userMessage
        }
    ],
        model="gpt-3.5-turbo",
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