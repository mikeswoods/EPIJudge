import functools

from list_node import ListNode
from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook


def overlapping_no_cycle_lists(l0: ListNode, l1: ListNode) -> ListNode:
    def length(L):
        i = L
        n = 0
        while i:
            n += 1
            i = i.next
        return n

    l0_n = length(l0)
    l1_n = length(l1)
    diff = abs(l0_n - l1_n)
    if diff is 0:
        return None

    # Find the longer list:
    i, j = (l0, l1) if l0_n > l1_n else (l1, l0)
    for _ in range(diff):
        i = i.next
    while i and j and i is not j:
        i = i.next
        j = j.next
    return i


@enable_executor_hook
def overlapping_no_cycle_lists_wrapper(executor, l0, l1, common):
    if common:
        if l0:
            i = l0
            while i.next:
                i = i.next
            i.next = common
        else:
            l0 = common

        if l1:
            i = l1
            while i.next:
                i = i.next
            i.next = common
        else:
            l1 = common

    result = executor.run(functools.partial(overlapping_no_cycle_lists, l0,
                                            l1))

    if result != common:
        raise TestFailure('Invalid result')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('do_terminated_lists_overlap.py',
                                       'do_terminated_lists_overlap.tsv',
                                       overlapping_no_cycle_lists_wrapper))
