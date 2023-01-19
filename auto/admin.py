from django.contrib import admin
from .models import CarAd, Comment
from django_summernote.admin import SummernoteModelAdmin
# Register your models here.


@admin.register(CarAd)
class CarAdAdmin(SummernoteModelAdmin):

    list_display = ('title', 'slug', 'author', 'created_on', 'year', 'nct', 'price')
    list_filter = ('author', 'created_on')
    summernote_fields = ('description',)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'body', 'post', 'created_on', 'approved')
    list_filter = ('approved', 'created_on')
    search_fields = ('name', 'body')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(approved=True)
