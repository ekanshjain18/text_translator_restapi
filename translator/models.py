from django.db import models

class TranslatedText(models.Model):
    source_text = models.TextField()
    source_lang = models.CharField(max_length=10)
    target_lang = models.CharField(max_length=10)
    translated_text = models.TextField()

    def __str__(self):
        return f"{self.source_lang} to {self.target_lang}: {self.source_text}"
