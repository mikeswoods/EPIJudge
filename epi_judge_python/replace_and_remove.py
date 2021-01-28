import functools
from typing import List

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook


def replace_and_remove(size: int, s: List[str]) -> int:
    i = 0
    seen = 0
    k = len(s)
    while i < k and seen <= size:
        if s[i] == 'b':
            del s[i]
            k -= 1
        elif s[i] == 'a':
            # first 'a':
            s[i] = 'd'
            s.insert(i, 'd')
            k += 1
            i += 2
        else:
            i += 1
        seen += 1
    return i - 1


@enable_executor_hook
def replace_and_remove_wrapper(executor, size, s):
    res_size = executor.run(functools.partial(replace_and_remove, size, s))
    return s[:res_size]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('replace_and_remove.py',
                                       'replace_and_remove.tsv',
                                       replace_and_remove_wrapper))
