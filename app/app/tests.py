"""
Sample tests
"""

from django.test import SimpleTestCase

from app import calc

class CalcTests(SimpleTestCase):
    
    def test_add_numbers(self):
        
        result = calc.add(2,2)
        
        self.assertEqual(4, result)
        
    def test_subtract_numbers(self):
        
        result = calc.subtract(10, 2)
        
        self.assertEqual(8, result)