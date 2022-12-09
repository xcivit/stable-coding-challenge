from questions.q3 import select_stock


def test_example():
    """Test the example from the question."""
    assert (
        select_stock(
            250,
            [175, 133, 109, 210, 97],
            [200, 125, 128, 228, 133],
        )
        == 55
    )


def test_max_number_of_stocks():
    """Test with max number of stocks"""
    assert (
        select_stock(
            250,
            [175, 133, 109, 210, 97] * 100,
            [200, 125, 128, 228, 133] * 100,
        )
        == 72
    )


def test_max_number_of_stocks_and_saving():
    """Test with max number of stocks and saving"""
    assert (
        select_stock(
            30000,
            [1750, 1330, 1090, 2100, 970] * 20,
            [2000, 1250, 1280, 2280, 1330] * 20,
        )
        == 8970
    )


def test_same_value():
    """Test with same value."""
    assert (
        select_stock(
            250,
            [1] * 251,
            [2] * 251,
        )
        == 250
    )


def test_two_less_profitable_stocks():
    """Test with two less profitable stocks."""
    assert (
        select_stock(
            250,
            [100, 100, 200],
            [130, 130, 240],
        )
        == 60
    )


def test_one_profitable_stocks():
    """Test with one profitable stocks."""
    assert (
        select_stock(
            250,
            [100, 100, 200],
            [130, 130, 270],
        )
        == 70
    )


def test_no_profitable():
    """Test with no profitable stocks."""
    assert (
        select_stock(
            250,
            [3] * 251,
            [2] * 251,
        )
        == 0
    )


def test_deep_pocket():
    """Test large saving."""
    assert (
        select_stock(
            30000,
            [1] * 251,
            [2] * 251,
        )
        == 251
    )
