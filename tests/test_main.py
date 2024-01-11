from app.calculator import Calculator


class Test:
    def setup(self):
        self.calc = Calculator

    def test_multiply(self):
        assert self.calc.multiply(self, 2, 2) == 4

    def test_division(self):
        assert self.calc.division(self, 4, 2) == 2

    def test_subtraction(self):
        assert self.calc.subtraction(self, 5, 3) == 2

    def test_adding(self):
        assert self.calc.adding(self, 5, 2) == 7

    def teardown(self):
        print("Выполнение метода Teardown")