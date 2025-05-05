from django.shortcuts import render, redirect
from . import forms
from . import models

def add_post(request):
    if request.method == 'POST':
        post_form = forms.PostForm(request.POST)  # Form with submitted data
        if post_form.is_valid():
            post_form.save()
            return redirect('add_post')
        # If invalid, render the same form with errors
    else:
        post_form = forms.PostForm()  # Empty form for GET requests
    
    return render(request, 'add_post.html', {'form': post_form})


def edit_post(request, id):
    post = models.Post.objects.get(pk=id)
    post_form = forms.PostForm(instance=post)  # Form with submitted data
    print(post.title)
    if request.method == 'POST':
        post_form = forms.PostForm(request.POST, instance=post)  # Form with submitted data
        if post_form.is_valid():
            post_form.save()
            return redirect('homepage')
        # If invalid, render the same form with errors
    
    return render(request, 'add_post.html', {'form': post_form})


def delet_post(request, id):
    post = models.Post.objects.get(pk=id)
    post.delete()
    return redirect('homepage')

from django.shortcuts import get_object_or_404

def post_detail(request, id):
    post = get_object_or_404(models.Post, pk=id)
    return render(request, 'post_detail.html', {'post': post})