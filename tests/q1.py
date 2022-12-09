from time import time

from questions.q1.q1 import stock_pairs


def test_example():
    """Test the example from the question."""
    assert stock_pairs([5, 7, 9, 13, 11, 6, 6, 3, 3], 12) == 3


def test_example_reversed():
    """Test the example from the question reversed."""
    assert stock_pairs(list(reversed([5, 7, 9, 13, 11, 6, 6, 3, 3])), 12) == 3


def test_one():
    """Test with one element."""
    assert stock_pairs([1], 2) == 0


def test_no_match():
    """Test with no matchs."""
    assert stock_pairs(list(range(10)), 20) == 0


def test_all_match():
    """Test with all matches."""
    assert stock_pairs(list(range(10)), 9) == 5


def test_same_value_all_pairs():
    """Test with same value."""
    assert stock_pairs([1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 2) == 5


def test_same_value_one_left():
    """Test with same value one orphan"""
    assert stock_pairs([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 2) == 5


def test_elements_greater_than_target():
    """Test with elements greater than target."""
    assert stock_pairs([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 0) == 0


def test_large_input_size_with_matchings():
    """Test with large input size with matchings."""
    print()
    for exp in [1e1, 1e2, 1e3, 1e4, 1e5]:
        max_len = int(5 * exp)
        t_start = time()
        assert stock_pairs(list(range(max_len)), max_len - 1) == max_len // 2
        t_end = time()
        print(exp, t_end - t_start)


def test_large_input_size_without_matchings():
    """Test with large input size without matchings."""
    print()
    for exp in [1e1, 1e2, 1e3, 1e4, 1e5]:
        max_len = int(5 * exp)
        t_start = time()
        assert stock_pairs(list(range(max_len)), max_len**2) == 0
        t_end = time()
        print(exp, t_end - t_start)
