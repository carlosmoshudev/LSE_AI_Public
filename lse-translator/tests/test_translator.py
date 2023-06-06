import unittest
import src.translator as Translator

class TestTranslator(unittest.TestCase):
    def setUp(self):
        self.translator = Translator('../../config.json')

    def test_translate_toe_string(self):
        input_text = "Hola, estoy haciendo un test de mi función translate, para ver que me respondes un texto."

        output = self.translator.translate(input_text)
        self.assertIsInstance(output, str)

    def test_translate_tobe_tokenizable(self):
        input_text = "buenos días, hoy voy a ir a trabajar en coche"
        expected_output = "buenos días hoy yo trabajar coche ir"

        output = self.translator.translate(input_text)
        self.assertEqual(output, expected_output)
    
if __name__ == '__main__':
    unittest.main()
# tests/test_translator.py