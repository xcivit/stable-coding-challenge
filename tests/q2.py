from questions.q2 import degree_of_array


def test_example():
    """Test the example from the question."""
    assert degree_of_array([1, 2, 1, 3, 2]) == 3


def test_small_1():
    """Test with small input size and len 1"""
    assert degree_of_array([1, 2]) == 1


def test_small_2():
    """Test with small input size and len 2"""
    assert degree_of_array([1, 1]) == 2


def test_large_input_degree_1():
    """Test with large input size and degree 1"""
    max_len = int(1e5)
    assert degree_of_array(list(range(max_len))) == 1


def test_large_input_degree_len():
    """Test with large input size and degree len"""
    max_len = int(1e5)
    assert degree_of_array([1] * max_len) == max_len
