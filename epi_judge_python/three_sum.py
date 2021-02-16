from typing import List

from test_framework import generic_test


from bisect import bisect_left


def binsearch(A, x):
  x_i = bisect_left(A, x)
  if x_i < len(A) and A[x_i] == x:
    return x_i
  return None


def has_three_sum(A: List[int], t: int) -> bool:
  n = len(A)
  A.sort()
  for x in A:
    for y in A:
      z = t - (x + y)
      z_i = binsearch(A, z)
      if z_i is not None:
        return True
  return False


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('three_sum.py', 'three_sum.tsv',
                                       has_three_sum))
