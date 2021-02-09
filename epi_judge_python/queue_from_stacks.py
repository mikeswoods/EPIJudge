from test_framework import generic_test
from test_framework.test_failure import TestFailure


def push(s, item):
    s.append(item)


def pop(s):
    return s.pop()


def is_empty(s):
    return len(s) == 0


class Queue:
    def __init__(self):
        self.stack = []

    def enqueue(self, x: int) -> None:
        push(self.stack, x)

    def dequeue(self) -> int:
        s2 = []
        # [1,2,3,4,5] -> [5,4,3,2,1]
        while not is_empty(self.stack):
            push(s2, pop(self.stack))
        last = pop(s2)
        while not is_empty(s2):
            push(self.stack, pop(s2))
        return last


def queue_tester(ops):
    try:
        q = Queue()

        for (op, arg) in ops:
            if op == 'Queue':
                q = Queue()
            elif op == 'enqueue':
                q.enqueue(arg)
            elif op == 'dequeue':
                result = q.dequeue()
                if result != arg:
                    raise TestFailure('Dequeue: expected ' + str(arg) +
                                      ', got ' + str(result))
            else:
                raise RuntimeError('Unsupported queue operation: ' + op)
    except IndexError:
        raise TestFailure('Unexpected IndexError exception')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('queue_from_stacks.py',
                                       'queue_from_stacks.tsv', queue_tester))
