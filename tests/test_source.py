import unittest
from app.models import Source


class SourceTest(unittest.TestCase):
   
    def setUp(self):
        
        self.new_source = Source('abc-news','ABC News', 'blabla blabla', 'en')

    def test_source_instance(self):
        
        self.assertTrue(isinstance(self.new_source,Source))

    def test_init(self):
       
        self.assertEqual(self.new_source.id, 'abc-news')
        self.assertEqual(self.new_source.name, 'ABC News')
        self.assertEqual(self.new_source.description, 'blabla blabla')
        self.assertEqual(self.new_source.language, 'en')