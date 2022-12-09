# q2

Given an array of integers, its degree is defined as the number of occurrences of the element that occurs most frequently in the array. Given a list of integers, determine two properties:

1. the degree of the array
2. the length of the shortest sub-array that shares that degree

### Example

`arr = [1, 2, 1, 3, 2]`

The array has a degree of 2 based on the occurrences of values 1 and 2. The subarray of degree 2 based on the 1's is [1, 2, 1] and based on 2's is [2, 1, 3, 2]. Their lengths are 3 and 4, so the shortest is length 3. Return the shortest length.

### Function Description

Complete the function degree0fArray in the editor below. The function must return an integer denoting the minimum size of the subarray such that the degree of the subarray is equal to the degree of the array.

degree0fArray has the following parameter(s):

- int arr[n]: an array of integers indexed from 0 to n-1

### Return

- int: the minimum size of the subarrays that have a degree equal to the degree of the array

### Constraints

- $2 \le n \le 10^5$
- $1 \le arr[i] \le 10^6$
