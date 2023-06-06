import unittest
import src.translator as Translator

class TestTranslator(unittest.TestCase):
    def setUp(self):
        self.translator = Translator()

    def test_translate(self):
        input_text = "buenos días, hoy voy a ir a trabajar en coche"
        expected_output = "buenos días hoy yo trabajar coche ir"

        output = self.translator.translate(input_text)
        self.assertEqual(output, expected_output)
    
if __name__ == '__main__':
    unittest.main()
# tests/test_translator.py