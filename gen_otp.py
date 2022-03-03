"""
Generates numeric OTP with length len
"""

import random

def gen_otp(len: int) -> str:
    return ''.join([str(random.randint(0, 9)) for i in range(len)])
