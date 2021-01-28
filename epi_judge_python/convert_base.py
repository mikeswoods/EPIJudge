from test_framework import generic_test


def convert_base(num_as_string: str, b1: int, b2: int) -> str:
  digits_int_to_char = "0123456789ABCDEF"
  digits_char_to_int = {c: i for i, c in enumerate(digits_int_to_char)}

  def convert_base_to_10(n: str, b_2: int) -> int:
    return sum(digits_char_to_int[digit] * (b_2 ** power) for power, digit in enumerate(reversed(n), start=0))

  def convert_10_to_base(n: int, base: int) -> str:
    (q, r) = divmod(n, base)
    if q == 0:
      return digits_int_to_char[r]
    return convert_10_to_base(q, base) + digits_int_to_char[r]

  negative = False
  if len(num_as_string[0]) > 0 and num_as_string[0] == '-':
    num_as_string = num_as_string[1:]
    negative = True

  c = convert_10_to_base(convert_base_to_10(num_as_string, b1), b2)
  if negative:
    c = '-' + c
  return c


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('convert_base.py', 'convert_base.tsv',
                                       convert_base))
