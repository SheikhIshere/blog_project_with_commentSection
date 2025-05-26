from django.shortcuts import render, redirect
from . import forms
from . import models
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect
from django.contrib import messages
from .models import Post  # Import your Post model
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, UpdateView, DetailView
from django.utils.decorators import method_decorator
from django.db.models import Q
from .forms import CommentForm
from django.http import HttpResponseRedirect


#@login_required
#def edit_post(request, id):
#    post = models.Post.objects.get(pk=id)
#    post_form.instance.author = request.user
#    post_form = forms.PostForm(instance=post)  # Form with submitted data
#    print(post.title)
#    if request.method == 'POST':        
#        post_form = forms.PostForm(request.POST, instance=post)  # Form with submitted data
#        if post_form.is_valid():
#            # post_form.instance.author = request.user
#            post_form.save()
#            return redirect('homepage')
#        # If invalid, render the same form with errors
#    
#    return render(request, 'add_post.html', {'form': post_form})

class EditPostView(UpdateView):
    model = models.Post
    form_class = forms.PostForm
    template_name = 'add_post.html'
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('profile')






#@login_required
#def delet_post(request, id):
#    post = get_object_or_404(Post, id=id)
#    
#    # Verify the current user is the author
#    if request.user != post.author:
#        messages.error(request, "You don't have permission to delete this post.")
#        return redirect('post_detail', id=post.id)
#    
#    if request.method == 'POST':
#        post.delete()
#        messages.success(request, "Post deleted successfully!")
#        return redirect('homepage')  # Or wherever you want to redirect after deletion
#    
#    # If GET request, show confirmation page
#    return render(request, 'post_confirm_delete.html', {'post': post})

# class based delet views
class ModelDeleteView(DeleteView):
    model = models.Post
    template_name = 'post_confirm_delete.html'
    success_url = reverse_lazy('profile')
    pk_url_kwarg = 'id'



# views.py

#def post_detail(request, id):
#    post = get_object_or_404(Post, id=id)
#    
#    # Get related posts (by same categories)
#    related_posts = Post.objects.filter(
#        category__in=post.category.all()
#    ).exclude(id=post.id).distinct()[:4]  # Get 4 unique related posts
#    
#    context = {
#        'post': post,
#        'related_posts': related_posts
#    }
#    return render(request, 'post_detail.html', context)
# class based post_details

class ModelDetailView(DetailView):
    model = models.Post
    pk_url_kwarg = 'id'
    template_name = 'post_detail.html'
    context_object_name = 'post'

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        comment_form = CommentForm(request.POST)
        
        if comment_form.is_valid():
            if request.user.is_authenticated:
                new_comment = comment_form.save(commit=False)
                new_comment.post = self.object
                new_comment.user = request.user
                new_comment.name = request.user.get_full_name() or request.user.username
                new_comment.email = request.user.email
                new_comment.save()
                messages.success(request, "Your comment has been posted!")
                return HttpResponseRedirect(self.request.path_info)
            else:
                messages.error(request, "You must be logged in to comment.")
                return redirect('login')
        else:
            messages.error(request, "There was an error with your comment.")
            return self.get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post = self.object
        
        # Get related posts
        related_posts = models.Post.objects.filter(
            Q(category__in=post.category.all()) & 
            ~Q(id=post.id)
        ).distinct()[:4]
        
        # Get comments for the post (ordered by newest first)
        comments = post.comments.all().order_by('-created_on')
        
        # Add fresh form to context
        context.update({
            'related_posts': related_posts,
            'comments': comments,
            'comment_form': CommentForm()
        })
        return context
    

#@login_required
#def add_post(request):
#    if request.method == 'POST':
#        post_form = forms.PostForm(request.POST)  # Form with submitted data
#        if post_form.is_valid():
#            # post_form.cleaned_data['author'] = request.user
#            post_form.instance.author = request.user
#            post_form.save()
#            return redirect('add_post')
#        # If invalid, render the same form with errors
#    else:
#        post_form = forms.PostForm()  # Empty form for GET requests
#    
#    return render(request, 'add_post.html', {'form': post_form})
#



# add post using class based views
@method_decorator(login_required, name='dispatch')
class AddPostCreateView(CreateView):
    model = models.Post
    form_class = forms.PostForm
    template_name = 'add_post.html'
    success_url = reverse_lazy('add_post')
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    

