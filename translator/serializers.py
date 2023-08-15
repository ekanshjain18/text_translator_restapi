from rest_framework import serializers
from .models import TranslatedText

class TranslatedTextSerializer(serializers.ModelSerializer):
    class Meta:
        model = TranslatedText
        fields = '__all__'
