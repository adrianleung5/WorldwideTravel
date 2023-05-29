from django.contrib import admin
from .models import Holidays
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.
admin.site.register(Holidays)

@admin.register(Holidays)
class HolidaysAdnub(SummerNoteModelAdmin):
    summernote_fields = ('content')