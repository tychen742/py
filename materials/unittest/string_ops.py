import unittest

class TestStringMethods(unittest.TestCase):
    
    def setUp(self):
        pass
    
    def test_strings_a(self):
        self.assertEqual('a'*4, 'aaaa')

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_strip(self):
        s = 'what a life'
        self.assertEqual(s.strip('life'), 'what a ')
    
if __name__ == '__main__':
    unittest.main()
