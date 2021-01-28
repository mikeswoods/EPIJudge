from test_framework import generic_test

import string

index = {d: i for i, d in enumerate(string.ascii_uppercase, start=1)}
base = len(index)

def ss_decode_col_id(col: str) -> int:
  return sum(index[ch] * (base ** power) for power, ch in enumerate(reversed(col), start=0))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('spreadsheet_encoding.py',
                                       'spreadsheet_encoding.tsv',
                                       ss_decode_col_id))
