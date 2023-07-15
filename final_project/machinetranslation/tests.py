import unittest
from translator import english_to_french, french_to_english

class TranslationTests(unittest.TestCase):
    def test_english_to_french_hello(self):
        english_text = 'Hello'
        french_text = english_to_french(english_text)
        self.assertEqual(french_text, 'Bonjour')

    def test_english_to_french_bonjour(self):
        english_text = 'Bonjour'
        french_text = english_to_french(english_text)
        self.assertEqual(french_text, 'Bonjour')  # Bonjour remains the same in French

    def test_french_to_english_bonjour(self):
        french_text = 'Bonjour'
        english_text = french_to_english(french_text)
        self.assertEqual(english_text, 'Hi')

    def test_french_to_english_hello(self):
        french_text = 'Hello'
        english_text = french_to_english(french_text)
        self.assertEqual(english_text, 'Hello')  # Hello remains the same in English

if __name__ == '__main__':
    unittest.main()