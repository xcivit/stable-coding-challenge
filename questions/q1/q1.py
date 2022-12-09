import typing
from collections import defaultdict


def stock_pairs(stocks_profit: typing.List[int], target: int) -> int:  # O(n)
    """
    stock_pairs function takes in 2 parameters:
    stocks_profit: List[int] - the profit of each stock
    target: int - the target profit

    The function returns an int which is the number of pairs of stocks that
    add up to the target profit, the algorithm used is a hashmap and the time
    complexity is O(n) where n is the number of stocks
    """
    count = 0
    expected_values: typing.Dict[int, int] = defaultdict(
        lambda: 0
    )  # key: int number expected, value: int times expected
    _stocks_profit = stocks_profit.copy()  # we are going to modify it
    while _stocks_profit:
        stock_profit = _stocks_profit.pop()  # pop() is O(1) on python lists
        if expected_values[stock_profit] > 0:
            expected_values[stock_profit] -= 1
            count += 1
        elif stock_profit <= target:
            expected_values[target - stock_profit] += 1

    return count
