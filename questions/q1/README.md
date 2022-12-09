# q1

A financial analyst is responsible for a portfolio of profitable stocks represented in an array. Each item in the array represents the yearly profit of a corresponding stock. The analyst gathers all distinct pairs of stocks that reached the target profit. Distinct pairs are pairs that differ in at least one element. Given the array of profits, find the number of distinct pairs of stocks where the sum of each pair's profits is exactly equal to the target profit.

### Example

$\text{stocksProfit} = [5, 7, 9, 13, 11, 6, 6, 3, 3]$

$\text{target} = 12 \text{profit's target}$

- There are 4 pain of stocks that have the sum of their profits equals to the target 12. Note that because there are two in stances of in stocksProfit there are two pairs matching (9,3): docksRofits indices 2 and 7, and indices 2 and 8, but only one can be included.
- There are 3 distinct pairs of stocks: (5, 7), (3, 9), and (6, 6) and the return value is 3.

### Function Description

Complete the function stockPairs in the editor below.
storkPairs has the following parameter(s):

- int stoksProfit[n]: an array of integers representing the stocks profits
- target: an integer representing the yearly target profit

Returns:

- int the total number of pairs determined

### Constraints

- $1 \le n \le 5 \times 10^5$
- $0 \le \text{stockProfit[i]} \le 10^9$
- $0 \le \text{target} \le 5 \times 10^9$
