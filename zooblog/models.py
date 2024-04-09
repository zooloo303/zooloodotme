from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# Model for the blog post
class Post(models.Model):
    title = models.CharField(null=False, 
                             blank=False,
                             max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)
    author = models.CharField(max_length=100)

    def __str__(self):
        return self.title
    
# Model for ChatMessages
class ChatMessage(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username}: {self.message[:20]}..."
