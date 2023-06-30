import unittest
from methods import MyMethods

class TestClass(unittest.TestCase):
    
    def setUp(self):
        self.my_obj = MyMethods()
    
    def test_method1(self):
        self.assertTrue(self.my_obj.method1())

    def test_method2(self):
        self.assertFalse(self.my_obj.method2())

    def test_method3(self):
        self.assertEqual(self.my_obj.method3(), 'BLA')

    def test_method3b(self):
        self.assertNotEqual(self.my_obj.method3(), 'Bla')

    def test_method4(self):
        with self.assertRaises(KeyError):
            self.my_obj.method4(3)

    def test_method5(self):
        with self.assertRaises(IndexError):
            self.my_obj.method5(8)

    def test_method1b(self):
        self.assertIs(self.my_obj.method1(), True)

    def test_method1c(self):
        self.assertIsNot(self.my_obj.method1(), False)

    def test_method6(self):
        self.assertIsNone(self.my_obj.method6())

    def test_method3d(self):
        self.assertIsNotNone(self.my_obj.method3())

    def test_method7(self):
        self.assertIn(3, self.my_obj.method7())

    def test_method3e(self):
        self.assertNotIn('C', self.my_obj.method3())

    def test_method8(self):
        self.assertIn('a', self.my_obj.method8().values())

    def test_method8b(self):
        self.assertIsInstance(self.my_obj.method8(), dict)

    def test_method8c(self):
        self.assertNotIsInstance(self.my_obj.method8()[1], int)

    def test_pass(self):
        pass

    def test_fail(self):
        self.fail('Hey this is failed test')

    def test_methodA(self):
        if type(self.my_obj.method9()) is not list:
            self.fail('Julia"s fail massage')
        else:
            pass



    



if __name__ == '__main__':
    unittest.main()
        



    

