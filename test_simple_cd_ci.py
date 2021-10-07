import calculator_pipeline


class TestSimpleCdCi:
    def test_addition(self):
        assert 4 == calculator_pipeline.add(2, 2)

    def test_subtraction(self):
        assert 2 == calculator_pipeline.subtract(4, 2)

    def test_multiplication(self):
        assert 4 == calculator_pipeline.multiply(2, 2)

    def test_division(self):
        assert 3 == calculator_pipeline.divide(6, 2)

    # def setUp(self, a):
    #     a.monkeypatch.setattr(calculator_pipeline.select, 'select', value=0)
    #     a = calculator_pipeline.number_1(6)
    #     b = calculator_pipeline.number_2(3)

