import machinetranslation.translator as tr
import unittest

class TestTranslation(unittest.TestCase):
    def test_null_fr2en(self):
        self.assertEqual(tr.french_to_english(None), None)
    def test_null_en2fr(self):
        self.assertEqual(tr.english_to_french(None), None)
    def test_en2fr(self):
        self.assertEqual(tr.english_to_french("Hello"), "Bonjour")
    def test_fr2en(self):
        self.assertEqual(tr.french_to_english("Bonjour"), "Hello")

# Run the tests
if __name__ == '__main__':
    unittest.main()