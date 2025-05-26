# posts/models.py (keep this exactly as is)
from django.db import models
from categories.models import Category
from django.contrib.auth.models import User

class Post(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    category = models.ManyToManyField(Category)
    author = models.ForeignKey(User, on_delete=models.CASCADE)    
    image = models.ImageField(        
        upload_to='posts/uploads/',  # This is perfect
        blank=True,
        null=True
    )
    def __str__(self):
        return self.title

#class Comment(models.Model):
#    post = models.ForeignKey(Post, on_delete= models.CASCADE, related_name='comments')    
#    name = models.CharField(max_length=30)
#    email = models.EmailField(unique=True)
#    body = models.TextField()
#    created_on = models.DateField(auto_now_add=True) # Jokhon e ei object creat hobe tokhon e time save hoye jabe
#
#    def __str__(self):
#        return f"comments by{self.name} "

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)  # For authenticated users
    name = models.CharField(max_length=30, blank=True)  # Make optional
    email = models.EmailField(blank=True)  # Remove unique constraint and make optional
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)  # Changed from DateField to DateTimeField

    def __str__(self):
        return f"Comment by {self.name or self.user.username}"    