from django.shortcuts import render, redirect
from . import forms

def add_author(request):
    if request.method == 'POST':
        author_form = forms.AuthorForm(request.POST)  # Form with submitted data
        if author_form.is_valid():
            author_form.save()
            return redirect('add_author')
        # If invalid, render the same form with errors
    else:
        author_form = forms.AuthorForm()  # Empty form for GET requests
    
    return render(request, 'add_author.html', {'form': author_form})