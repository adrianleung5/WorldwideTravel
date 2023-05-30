from django.contrib import admin
from .models import Holidays
from .models import comment
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.

@admin.register(Holidays)
class HolidaysAdnub(SummernoteModelAdmin):
    list_display = ('title', 'slug', 'status',)
    search_fields = ['title', 'content']
    list_filter = ('status', )
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('content',)

@admin.register(Comment)
class AdminForComment(admin.ModelAdmin):
    """This is for the admin to manage Comments"""
    list_filter = ('date_added',)
    list_display = ('name', 'info', 'date_added')
    search_fields = ('name', 'email', 'info')

