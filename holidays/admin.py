from django.contrib import admin
from .models import Holidays
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.

@admin.register(Holidays)
class HolidaysAdnub(SummernoteModelAdmin):
    summernote_fields = ('content')