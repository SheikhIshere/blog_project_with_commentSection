from django.contrib import admin
from . import models
from .models import Like

# Register your models here.
admin.site.register(models.Post)
admin.site.register(models.Comment)

@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    list_display = ('user', 'post', 'timestamp')
    search_fields = ('user__username', 'post__title')
