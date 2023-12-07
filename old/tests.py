import unittest
from transpiler import  transpile, Runproject, Compilee, Compileprojectwithoutput,Compileproject
from templates import create_project,CreateDll
from CSVM import *
import argparse
from errors import *

class TestTranspiler(unittest.TestCase):
    """
    A unit test class for testing the transpile function.
    """
    def test_transpile(self):
        # Test the transpile function to see if all is working!
        self.assertEqual(transpile('struct'), 'static void')
        self.assertEqual(transpile('revoid'), 'public static void')
        self.assertEqual(transpile('reint'), 'public static int' )
        self.assertEqual(transpile('rebool'), 'public static bool' )

        
    def test_transpile_valid_code(self):
        # Test transpiling valid code
        source_code = 'struct'
        expected_output = 'static void'
        self.assertEqual(transpile(source_code), expected_output)

    def test_transpile_invalid_code(self):
        # Test transpiling invalid code
        source_code = 'invalid syntax'
        with self.assertRaises(OSError):
            transpile(source_code)
    def test_error_functions(self):
        with self.assertRaises(EnvironmentError):
            print_error("test error")
    
if __name__ == '__main__':
    unittest.main()
