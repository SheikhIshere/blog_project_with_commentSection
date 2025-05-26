# posts/models.py (keep this exactly as is)
from django.db import models
from categories.models import Category
from django.contrib.auth.models import User

class Post(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField(blank=True)
    category = models.ManyToManyField(Category)
    author = models.ForeignKey(User, on_delete=models.CASCADE)    
    created_at = models.DateTimeField(auto_now_add=True)   
    
    def is_liked_by(self, user):
        return self.likes.filter(user=user).exists() 
    
    image = models.ImageField(        
        upload_to='posts/',  # This is perfect
        blank=True,
        null=True
    )
    def __str__(self):
        return self.title
    
    def total_likes(self):
        return self.likes.count()
    
    


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
    created_on = models.DateTimeField(auto_now_add=True)     

    def __str__(self):
        return f"Comment by {self.name or self.user.username}"    
    

class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)    
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='likes')
    timestamp = models.DateTimeField(auto_now_add=True)    
    class Meta:
        unique_together = ('user', 'post')  # Prevent duplicate likes

    def __str__(self):
        return f"{self.user.username} likes {self.post.title}"    