"""
Generates tracking number string with correct chuch_digit given str_num: ex: '02238721'.
Works with Thailand Post.
"""

import numpy as np

def gen_tracking_num(str_num: str, str_prefix: str, str_suffix: str) -> str:
    check_digit = 0
    np_multiplier = np.array([8,6,4,2,3,5,9,7])

    lst_digits = []
    for i in range(len(str_num)):
        lst_digits.append(str_num[i])

    np_digits = np.array(lst_digits).astype(int)
    sum_product = np.dot(np_digits, np_multiplier)
    remainder = sum_product % 11

    if remainder == 0:
        check_digit = 5
    elif remainder == 1:
        check_digit = 0
    else:
        check_digit = 11 - remainder

    return f'{str_prefix}{str_num}{str(check_digit)}{str_suffix}'
