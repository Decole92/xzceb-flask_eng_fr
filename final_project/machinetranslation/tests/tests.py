import unittest
from deep_translator import MyMemoryTranslator


class TranslationTests(unittest.TestCase):

    def test_english_to_French(self):
        translator = MyMemoryTranslator(source='en', target='fr')
        english_text = "Hello"
        expected_french_text = "Bonjour"
        french_text = translator.translate(english_text)
        self.assertEqual(french_text, expected_french_text)

    def test_french_to_English(self):
        translator = MyMemoryTranslator()
        french_text = "Bonjour"
        expected_english_text = "Hello"
        english_test = translator.translate(french_text)
        self.assertEqual(english_test, expected_english_text)
