from day1.fib import is_prime


def test_2_is_prime():
    assert is_prime(2) is True


def test_4_is_not_prime():
    assert is_prime(4) is False