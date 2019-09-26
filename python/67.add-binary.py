#
# @lc app=leetcode id=67 lang=python3
#
# [67] Add Binary
#
# https://leetcode.com/problems/add-binary/description/
#
# algorithms
# Easy (38.65%)
# Total Accepted:    292.4K
# Total Submissions: 756.6K
# Testcase Example:  '"11"\n"1"'
#
# Given two binary strings, return their sum (also a binary string).
# 
# The input strings are both non-empty and contains only characters 1 or 0.
# 
# Example 1:
# 
# 
# Input: a = "11", b = "1"
# Output: "100"
# 
# Example 2:
# 
# 
# Input: a = "1010", b = "1011"
# Output: "10101"
# 
#
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        i, j = len(a) - 1, len(b) - 1
        result = ''
        carry = 0
        while (i >= 0 or j >= 0):
            if i < 0:
                x = 0
                y = b[j]
            elif j < 0:
                x = a[i]
                y = 0
            else:
                x = a[i]
                y = b[j]
            sum = int(x) + int(y) + carry
            if sum > 1:
                result = str(sum - 2) + result
                carry = 1
            else:
                result = str(sum) + result
                carry = 0
            i -= 1
            j -= 1
        if carry == 1:
            result = '1' + result
        return result
            
        

