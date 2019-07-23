import unittest
import convertisseur


class TestConvertisseur(unittest.TestCase):

    def testjson(self):
        self.assertTrue(convertisseur.ConvertisseurJson('test.json').filename)

if __name__ == '__main__':
    unittest.main()
