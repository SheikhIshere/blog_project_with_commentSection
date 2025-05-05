from django.shortcuts import render, redirect
from . import forms

def add_category(request):
    if request.method == 'POST':
        category_form = forms.CategoryForm(request.POST) # user post request koreche
        if category_form.is_valid(): # user er post request data ekhane chapture korlam
            category_form.save() # jodi tada valid hoy tahole database e save korbo
            return redirect('add_category') # sob thik thakle take add author eei url e 
        
    else:
        category_form = forms.CategoryForm()  
    
    return render(request, 'add_category.html', {'form': category_form})