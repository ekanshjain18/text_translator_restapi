from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from .models import TranslatedText

class TranslatedTextAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()
# testing creation of translation
    def test_create_translation(self):
        data = {
            'text': 'Nice to meet you',
            'source': 'en',
            'target': 'fr'
        }
        response = self.client.post('enter server link', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(TranslatedText.objects.count(), 1)

    # Retrieving particular translation
    def test_retrieve_translation(self):
        translation = TranslatedText.objects.create(
            source_text='Hello',
            source_lang='en',
            target_lang='es',
            translated_text='Hola'
        )
        response = self.client.get(f'enter server link?text={translation.source_text}&source={translation.source_lang}&target={translation.target_lang}')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['translated_text'], translation.translated_text)
   
    #Retrieving  all translation
    def test_retrieve_all_translations(self):
        TranslatedText.objects.create(
            source_text='Hello',
            source_lang='en',
            target_lang='fr',
            translated_text='Bonjour'
        )
        TranslatedText.objects.create(
            source_text='Goodbye',
            source_lang='en',
            target_lang='fr',
            translated_text='Au revoir'
        )
        response = self.client.get('enter server link')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)
        
