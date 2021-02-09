from test_framework import generic_test


def is_well_formed(s: str) -> bool:
    right_to_left = {
      "]": "[",
      "}": "{",
      ")": "("
    }
    def is_right(c: str) -> bool:
      return c in right_to_left
    def is_match(left_token: str, right_token: str) -> bool:
      return left_token == right_to_left[right_token]

    tokens = list(s)
    stack = []

    for token in tokens:
      if is_right(token):
        # If the stack is empty, the string can't be well-formed:
        if len(stack) == 0:
          return False
        # Try to match the current token with the token on the top of the stack:
        left_token = stack.pop()
        if not is_match(left_token, token):
          return False
      else: # if left
        stack.append(token)
    # If the stack isn't empty, there's unmatched tokens, which means the
    # expression isnt' well-formed
    return len(stack) == 0


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_valid_parenthesization.py',
                                       'is_valid_parenthesization.tsv',
                                       is_well_formed))
