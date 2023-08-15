from django.contrib import admin
from .models import TranslatedText

@admin.register(TranslatedText)
class TranslatedTextAdmin(admin.ModelAdmin):
    list_display = ('source_text', 'source_lang', 'target_lang')
    search_fields = ('source_text', 'translated_text')
    list_filter = ('source_lang', 'target_lang')
