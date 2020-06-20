import unittest
import AddPy_Homework5_ver2
from unittest.mock import patch

class InitAppTest(unittest.TestCase):

    def test_upload_date (self):
        dirs,docs= {}, []
        self.assertFalse(dirs)
        dirs,docs = AddPy_Homework5_ver2.update_date()
        self.assertTrue(docs)
        self.assertTrue(dirs)
        self.assertIsInstance(dirs, dict)

class AppTest(unittest.TestCase):
    def setUp(self):
        print ('Run setUp')
        self.dirs, self.docs = AddPy_Homework5_ver2.update_date()
        with patch ('AddPy_Homework5_ver2.input',return_value='q'):
            with patch ('AddPy_Homework5_ver2.update_date') as mock_ud:
                mock_ud.return_value = self.dirs, self.docs
                AddPy_Homework5_ver2.secretary_program_start()

    def test_remove_doc_from_shelf(self):
        AddPy_Homework5_ver2.remove_doc_from_shelf('10006')
        self.assertNotIn('10006', self.dirs['2'])

    def test_add_doc (self):
        before_len = len(self.docs)
        user_input = ['123', 'pasp', 'username', 'III']
        with patch ('AddPy_Homework5_ver2.input', side_effect=user_input):
            AddPy_Homework5_ver2.add_new_doc()
        self.assertGreater(len(self.docs), before_len)
        self.assertIn('III', self.dirs)

#Выполнение домашнего задания
    def test_add_new_shelf (self):
        before_len=len(self.dirs)
        print (before_len)
        with patch ('AddPy_Homework5_ver2.input', return_value='4'):
            AddPy_Homework5_ver2.add_new_shelf()
        after_len=len(self.dirs)
        print (after_len)
        self.assertGreater(after_len,before_len)

    def test_delete_doc(self):
        print (self.dirs)
        with patch('AddPy_Homework5_ver2.input', return_value='11-2'):
            AddPy_Homework5_ver2.delete_doc()
        print (self.dirs)
        self.assertNotIn('11-2',self.dirs['1'])


    def test_move_doc_to_shelf(self):
        print (self.dirs)
        user_input = ['10006', '3']
        with patch('AddPy_Homework5_ver2.input', side_effect=user_input):
            AddPy_Homework5_ver2.move_doc_to_shelf()
        print (self.dirs)
        self.assertNotIn('10006',self.dirs['2'])

