from django.db import models

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
