from django.contrib import admin
from .models import Holidays
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.

@admin.register(Holidays)
class HolidaysAdnub(SummernoteModelAdmin):
    list_display = ('title', 'slug', 'status',)
    search_fields = ['title', 'content']
    list_filter = ('status', )
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('content',)
    
