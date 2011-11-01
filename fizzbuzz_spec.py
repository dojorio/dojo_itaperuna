import unittest
from should_dsl import should
from fizzbuzz import fizzbuzz

class TestFizzBuzz(unittest.TestCase):
    
    def test_tres_deve_retornar_fizz(self):
        fizzbuzz(3) |should| equal_to("fizz")
        
    def test_cinco_deve_retornar_buzz(self):
        fizzbuzz(5) |should| equal_to("buzz")
        
    def test_um_deve_retornar_um(self):
        fizzbuzz(1) |should| equal_to(1)
        
    def test_seis_deve_retornar_fizz(self):
        fizzbuzz(6) |should| equal_to("fizz")
       
    def test_quatro_deve_retornar_quatro(self):
        fizzbuzz(4) |should| equal_to(4)
       
    def test_quinze_deve_retornar_fizzbuzz(self):
        fizzbuzz(15) |should| equal_to("fizzbuzz")
     
                 
