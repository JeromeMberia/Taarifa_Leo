import unittest
from app.models import Article

class ArticleTest(unittest.TestCase):
   
    def setUp(self):
        
        self.new_article = Article('a','b','c','d','e','f')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_article,Article))

    def test_init(self):
       
        self.assertEqual(self.new_article.author,'a')
        self.assertEqual(self.new_article.title, 'b')
        self.assertEqual(self.new_article.description, 'c')
        self.assertEqual(self.new_article.url, 'd')
        self.assertEqual(self.new_article.image, 'e')
        self.assertEqual(self.new_article.time, 'f')