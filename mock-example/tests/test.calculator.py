import pytest
from src.calculator import Calculator

# //Primeiro teste

# def test_add():   
#     calculator = Calculator()    
#     result = calculator.add(2, 3)    
#     assert result == 5



def test_add(mocker):
    mocker.patch("src.Calculator.Calculator.add", return_value=5)
    calculator = Calculator()
    assert calculator.add(2, 3) == 5

    
def test_substract(mocker):
    mocker.patch("src.Calculator.Calculator.substract", return_value=5)
    calculator = Calculator()
    assert calculator.substract(10, 5 ) == 5
    

    

