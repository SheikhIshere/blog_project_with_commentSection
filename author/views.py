from django.shortcuts import render, redirect
from . import forms
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth import authenticate, login, update_session_auth_hash, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from posts.models import Post
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator

#def add_author(request):
#    if request.method == 'POST':
#        author_form = forms.AuthorForm(request.POST)  # Form with submitted data
#        if author_form.is_valid():
#            author_form.save()
#            return redirect('add_author')
#        # If invalid, render the same form with errors
#    else:
#        author_form = forms.AuthorForm()  # Empty form for GET requests
#    
#    return render(request, 'add_author.html', {'form': author_form})



def register(request):
    if request.method == 'POST':
        register_form = forms.RegistrationForm(request.POST)  # Form with submitted data
        if register_form.is_valid():
            register_form.save()
            messages.success(request, 'Account created successfully :)')
            return redirect('user_login')
        # If invalid, render the same form with errors
    else:
        register_form = forms.RegistrationForm()  # Empty form for GET requests
    
    return render(request, 'register.html', {'form': register_form, 'type': 'register'})


#def user_login(request):
#   if request.method == 'POST':
#       form = AuthenticationForm(request, request.POST)
#       if form.is_valid():
#           user_name = form.cleaned_data['username']
#           user_pass = form.cleaned_data['password']
#           user = authenticate(username=user_name, password=user_pass)
#           if user is not None:
#               messages.success(request, 'logged in succesfully :)')
#               login(request, user)
#               return redirect('profile')
#           else:
#               messages.warning(request, 'informaiton is incorrect :(')
#               return redirect('user_login')  # This was missing - now added
#           
#       # If form is invalid, we also need to return something
#       return render(request, 'register.html', {'form': form, 'type': 'Login'})
#   
#   # GET request
#   form = AuthenticationForm()
#   return render(request, 'register.html', {'form': form, 'type': 'Login'})

#user based login
class UserLoginView(LoginView):
    template_name = 'register.html'

    def get_success_url(self):
        return reverse_lazy('profile')
    
    def form_valid(self, form):
        messages.success(self.request, 'Logged in successfully')
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.warning(self.request, 'logged in incorrect')
        return super().form_invalid(form)        
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['type'] = 'login'
        return context
    

        

@login_required
def profile(request):    
    data = Post.objects.filter(author = request.user)
    return render(request, 'profile.html', {'data': data})



def pass_change(request):
    if request.method == 'POST':
        form = PasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Correct usage
            messages.success(request, 'Password updated successfully!')
            return redirect('profile')
    else:
        form = PasswordChangeForm(user=request.user)
    
    return render(request, 'pass_change.html', {'form': form})


def user_logout(request):
   logout(request)
   messages.success(request, 'You have been successfully logged out.')
   return redirect('user_login')

# class based logout (problem is this is not wroking thing may be i will found out in the future but till keep coding keep prograssing)
# class ProductionLogoutView(LogoutView):    
    # next_page = reverse_lazy('login')  

@login_required
def edit_profile(request):
    if request.method == 'POST':
        edit_profile = forms.ChangeUserForm(request.POST, instance = request.user)  # Form with submitted data
        if edit_profile.is_valid():
            edit_profile.save()
            messages.success(request, 'profile updated successfully :)')
            return redirect('profile')
        # If invalid, render the same form with errors
    else:
        edit_profile = forms.ChangeUserForm( instance = request.user)  # Empty form for GET requests    
    return render(request, 'update_profile.html', {'form': edit_profile})
