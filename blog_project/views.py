# from django.shortcuts import render
# from posts.models import Post
# from categories.models import Category

# def home(request, catetory_slug = None):
#     data = Post.objects.all()
#     if category_slug is not None:
#         category = Category.objects.get(slug = catetory_slug)
#         data = Post.objects.filter(category = category)
#     categories = Category.objects.all()
#     return render(request, 'home.html',{'data': data, 'category': categories})


from django.shortcuts import render, get_object_or_404
from posts.models import Post
from categories.models import Category
from django.db.models import Count

def home(request, category_slug=None):
    # Base queryset with annotations
    posts = Post.objects.annotate(
        total_likes=Count('likes'),
        comment_count=Count('comments')
    ).order_by('-created_at')  # newest posts first
    
    # Apply category filter if specified
    if category_slug is not None:
        category = get_object_or_404(Category, slug=category_slug)
        posts = posts.filter(category=category)
    
    categories = Category.objects.all()
    return render(request, 'home.html', {
        'data': posts,
        'category': categories,
        'active_category': category_slug  # Pass the active category slug to template
    })