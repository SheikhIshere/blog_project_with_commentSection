from django.shortcuts import render, redirect
from . import forms
from . import models
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect
from django.contrib import messages
from .models import Post  # Import your Post model



@login_required
def add_post(request):
    if request.method == 'POST':
        post_form = forms.PostForm(request.POST)  # Form with submitted data
        if post_form.is_valid():
            # post_form.cleaned_data['author'] = request.user
            post_form.instance.author = request.user
            post_form.save()
            return redirect('add_post')
        # If invalid, render the same form with errors
    else:
        post_form = forms.PostForm()  # Empty form for GET requests
    
    return render(request, 'add_post.html', {'form': post_form})

@login_required
def edit_post(request, id):
    post = models.Post.objects.get(pk=id)
    post_form.instance.author = request.user
    post_form = forms.PostForm(instance=post)  # Form with submitted data
    print(post.title)
    if request.method == 'POST':        
        post_form = forms.PostForm(request.POST, instance=post)  # Form with submitted data
        if post_form.is_valid():
            # post_form.instance.author = request.user
            post_form.save()
            return redirect('homepage')
        # If invalid, render the same form with errors
    
    return render(request, 'add_post.html', {'form': post_form})

@login_required
def delet_post(request, id):
    post = get_object_or_404(Post, id=id)
    
    # Verify the current user is the author
    if request.user != post.author:
        messages.error(request, "You don't have permission to delete this post.")
        return redirect('post_detail', id=post.id)
    
    if request.method == 'POST':
        post.delete()
        messages.success(request, "Post deleted successfully!")
        return redirect('homepage')  # Or wherever you want to redirect after deletion
    
    # If GET request, show confirmation page
    return render(request, 'post_confirm_delete.html', {'post': post})



# views.py

def post_detail(request, id):
    post = get_object_or_404(Post, id=id)
    
    # Get related posts (by same categories)
    related_posts = Post.objects.filter(
        category__in=post.category.all()
    ).exclude(id=post.id).distinct()[:4]  # Get 4 unique related posts
    
    context = {
        'post': post,
        'related_posts': related_posts
    }
    return render(request, 'post_detail.html', context)