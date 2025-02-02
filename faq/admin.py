from django.contrib import admin

# Register your models here.

from django.contrib import admin
from .models import FAQ

@admin.register(FAQ)
class FAQAdmin(admin.ModelAdmin):
    list_display = ('question','answer',  'question_hi', 'question_bn')


