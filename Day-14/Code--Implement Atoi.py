# -*- coding: utf-8 -*-
"""
Created on Sun Dec  8 11:01:52 2024

@author: vikas
"""

class Solution:
    
    def myAtoi(s):
        sign = 1
        res = 0
        idx = 0

        # Skip leading Whitespaces
        while idx < len(s) and s[idx].isspace():
            idx += 1

        # Check for sign
        if idx < len(s) and (s[idx] == '-' or s[idx] == '+'):
            if s[idx] == '-':
                sign = -1
            idx += 1

        # Convert digits to integer
        while idx < len(s) and s[idx].isdigit():
            res = res * 10 + (ord(s[idx]) - ord('0'))

            # Check for overflow
            if res > (2**31 - 1):
                return (2**31 - 1) if sign == 1 else -(2**31)

            idx += 1

        return sign * res


# input
s = "-123"
print(Solution.myAtoi(s))
