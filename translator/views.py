from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import TranslatedText
from .serializers import TranslatedTextSerializer
from googletrans import Translator
from django.db import IntegrityError

# get method can be used to find a particular record or list all the translation records.
class TranslationView(APIView):
    def get(self, request):
        source_text = request.query_params.get('text', None)
        source_lang = request.query_params.get('source', None)
        target_lang = request.query_params.get('target', None)

        if source_text is None and source_lang is None and target_lang is None:
            translations = TranslatedText.objects.all()
            serializer = TranslatedTextSerializer(translations, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)

        cached_translation = TranslatedText.objects.filter(source_text=source_text, source_lang=source_lang, target_lang=target_lang).first()
        if cached_translation:
            serializer = TranslatedTextSerializer(cached_translation)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({'Not found'}, status=status.HTTP_404_NOT_FOUND)
            
# post method is used for creating new translation or if found already in database then fetch from the database.
    def post(self, request):
        source_text = request.data.get('text')
        source_lang = request.data.get('source', 'en')
        target_lang = request.data.get('target', 'es')

        cached_translation = TranslatedText.objects.filter(source_text=source_text, source_lang=source_lang, target_lang=target_lang).first()
        if cached_translation:
            serializer = TranslatedTextSerializer(cached_translation)
            return Response(serializer.data, status=status.HTTP_200_OK)

        translator = Translator()
        translation = translator.translate(source_text, src=source_lang, dest=target_lang)
        translation_text = translation.text

        try:
            new_translation = TranslatedText.objects.create(source_text=source_text, source_lang=source_lang,target_lang=target_lang, translated_text=translation_text)
            serializer = TranslatedTextSerializer(new_translation)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except IntegrityError:
            return Response({'error': 'Translation already exists in the database'}, status=status.HTTP_409_CONFLICT)
