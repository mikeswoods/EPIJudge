import functools
from typing import Optional

from list_node import ListNode
from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook


def list_pivoting(l: ListNode, x: int) -> Optional[ListNode]:
    if not l:
        return l

    lesser = lesser_tail = ListNode(0)
    equal = equal_tail = ListNode(0)
    greater = greater_tail = ListNode(0)

    def detach_head(l):
        if not l:
            return None, None
        next_node = l.next
        head = l
        head.next = None
        return head, next_node

    it = l
    while it:
        it_next = it.next
        # detach:
        it.next = None
        if it.data < x:
            lesser_tail.next = it
            lesser_tail = it
        elif it.data == x:
            equal_tail.next = it
            equal_tail = it
        else:
            greater_tail.next = it
            greater_tail = it
        it = it_next

    # skip the dummy heads:
    lesser = lesser.next
    equal = equal.next
    greater = greater.next

    head = lesser
    tail = lesser_tail

    if head:
        tail.next = equal
    else:
        head = equal
    tail = equal_tail

    if head:
        tail.next = greater
    else:
        head = greater

    return head



def linked_to_list(l):
    v = list()
    while l is not None:
        v.append(l.data)
        l = l.next
    return v


@enable_executor_hook
def list_pivoting_wrapper(executor, l, x):
    original = linked_to_list(l)

    l = executor.run(functools.partial(list_pivoting, l, x))

    pivoted = linked_to_list(l)
    mode = -1
    for i in pivoted:
        if mode == -1:
            if i == x:
                mode = 0
            elif i > x:
                mode = 1
        elif mode == 0:
            if i < x:
                raise TestFailure('List is not pivoted')
            elif i > x:
                mode = 1
        else:
            if i <= x:
                raise TestFailure('List is not pivoted')

    if sorted(original) != sorted(pivoted):
        print("pivoted", pivoted)
        raise TestFailure('Result list contains different values')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('pivot_list.py', 'pivot_list.tsv',
                                       list_pivoting_wrapper))
