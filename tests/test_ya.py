import unittest
import AddPy_Homework5_ver2_task2
from unittest.mock import patch

class YaTest(unittest.TestCase):

    def test_response_code(self):
        translate_word='hello'
        with patch ('AddPy_Homework5_ver2_task2.input',return_value=translate_word):
            self.dirs=AddPy_Homework5_ver2_task2.translation_function()
        self.assertIn('привет',self.dirs['text'])
        self.assertEqual(200, self.dirs['code'])
