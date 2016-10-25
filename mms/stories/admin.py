from django.contrib import admin

from .models import Prompt, Response

class ResponseInline(admin.StackedInline):
    model = Response
    extra = 3

class PromptAdmin(admin.ModelAdmin):
    inlines = [ResponseInline]
    list_display = ('prompt_text', 'create_date')

admin.site.register(Prompt, PromptAdmin)
