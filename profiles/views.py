from django.shortcuts import render, redirect
from . import forms

def add_profile(request):
    if request.method == 'POST':
        profile_form = forms.ProfileForm(request.POST)  # Form with submitted data
        if profile_form.is_valid():
            profile_form.save()
            return redirect('add_profile')
        # If invalid, render the same form with errors
    else:
        profile_form = forms.ProfileForm()  # Empty form for GET requests
    
    return render(request, 'add_profile.html', {'form': profile_form})