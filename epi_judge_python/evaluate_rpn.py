from test_framework import generic_test


def evaluate(expression: str) -> int:
    def is_number(token):
      try:
        int(token)
        return True
      except:
        return False

    tokens = expression.split(',')
    numbers = []

    for token in tokens:
      if is_number(token):
        num = int(token)
        numbers.append(num)
      else:
        if len(numbers) < 2:
          raise Exception("malformed expression")
        right = numbers.pop()
        left = numbers.pop()
        if token == "+":
          numbers.append(left + right)
        elif token == "-":
          numbers.append(left - right)
        elif token == "*":
          numbers.append(left * right)
        elif token == "/":
          numbers.append(left // right)
        else:
          raise Exception(f"operator not supported: {token}")

    assert len(numbers) == 1

    return numbers[0]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('evaluate_rpn.py', 'evaluate_rpn.tsv',
                                       evaluate))
