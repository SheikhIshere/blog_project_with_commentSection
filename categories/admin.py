from django.contrib import admin
from . import models  # Make sure to import your Category model

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug' : ('name',)}  # Auto-create slug from name
    list_display = [ 'name', 'slug' ]  # Show these fields in list view

admin.site.register(models.Category, CategoryAdmin)