from typing import List

from test_framework import generic_test


from bisect import bisect_left


def has_two_sum(A: List[int], t: int) -> bool:
  # A is sorted
  for x in A:
    y = t - x
    y_i = bisect_left(A, y)
    if y_i < len(A) and A[y_i] == y:
      return True
  return False


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('two_sum.py', 'two_sum.tsv',
                                       has_two_sum))
