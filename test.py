import tail_call_factorial


def test_tail_small():
    assert tail_call_factorial.tail_call_factorial(3) == 6


def test_tail_large():
    assert tail_call_factorial.tail_call_factorial(14) == 87178291200
