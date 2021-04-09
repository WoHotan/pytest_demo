import pytest
from calculator import Calculator

class TestCalculator:
    
    def setup_class(self):
        print("Start test calculator....\n")
        self.calc = Calculator()
    
    def teardown_class(self):
        print("\nFinished the calculator test.")

    @pytest.mark.parametrize("a, b, expect", [(1, 1, 2), (0.1, 0.1, 0.2),
                                              (0.1, 1, 1.1), (-1, 1, 0),
                                              (-1, -2, -3), (1000000, 1000000, 2000000),
                                              (999, 1, 1000), ("1", "1", "11")])
    def test_add(self, a, b, expect):
        assert expect == self.calc.add(a, b)


    @pytest.mark.parametrize("a, b, expect", [(1, 1, 1),
                                              (1.1, 10, 0.11),
                                              (-1, -1, 1),
                                              (-1, 1, -1),
                                              (10000, 999, 10.01001001001001)])
    def test_div(self, a, b, expect):
        assert (expect - self.calc.div(a, b)) <= 0.000000001
    
    def test_zero_divition(self):
        with pytest.raises(ZeroDivisionError):
            self.calc.div(1, 0)
    

    