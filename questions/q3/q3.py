import typing
import sys


def knapsack_algorithm(
    values: typing.List[int],
    weights: typing.List[int],
    number_of_distinct_items: int,
    knapsack_capacity: int,
):
    """
    knapsack_algorithm function takes in 4 parameters:
    values: List[int] - the values of the items
    weights: List[int] - the weights of the items
    number_of_distinct_items: int - the number of distinct items
    capacity: int - the capacity of the knapsack

    The function returns an int which is the maximum value that can
    be put in a knapsack of capacity W, the algorithm used is knapsack
    and the time complexity is O(nW) where n is the number of distinct
    items and W is the capacity of the knapsack

    https://en.wikipedia.org/wiki/Knapsack_problem#0-1_knapsack_problem
    """
    # pylint: disable=invalid-name
    v = values
    w = weights
    n = number_of_distinct_items
    W = knapsack_capacity

    sys.setrecursionlimit(n * W)

    value = [[-1 for _ in range(W + 1)] for _ in range(n + 1)]

    def m(i, j):
        if i == 0 or j == 0:
            value[i][j] = 0
            return

        if value[i - 1][j] == -1:
            m(i - 1, j)

        if w[i - 1] > j:
            value[i][j] = value[i - 1][j]
        else:
            if value[i - 1][j - w[i - 1]] == -1:
                m(i - 1, j - w[i - 1])

            value[i][j] = max(value[i - 1][j], value[i - 1][j - w[i - 1]] + v[i - 1])

    m(n, W)
    # pylint: enable=invalid-name
    return value[n][W]


def select_stock(
    saving: int, current_values: typing.List[int], future_values: typing.List[int]
):
    """
    selectStock function takes in 3 parameters:
    saving: int - the amount of money you have to invest
    current_values: List[int] - the current value of the stock
    future_values: List[int] - the future value of the stock

    The function returns an int which is the maximum profit you can make,
    the algorithm used is knapsack and the time complexity is O(nW) where
    n is the number of profitable stocks and W is the amount of money you can invest

    Example:
    saving = 100
    current_values = [20, 90, 40, 90]
    future_values = [90, 120, 60, 80]

    The maximum profit you can make is 110
    """

    # discard stocks that are not profitable
    profit, _current_values = [], []
    for (current_value, future_value) in zip(current_values, future_values):
        if current_value <= saving and future_value > current_value:
            profit.append(future_value - current_value)
            _current_values.append(current_value)

    # edge cases
    if len(profit) == 0:
        return 0

    if sum(_current_values) <= saving:
        return sum(profit)

    # knapsack algorithm
    return knapsack_algorithm(profit, _current_values, len(profit), saving)
