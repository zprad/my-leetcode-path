#
# @lc app=leetcode id=66 lang=python3
#
# [66] Plus One
#
# https://leetcode.com/problems/plus-one/description/
#
# algorithms
# Easy (41.01%)
# Total Accepted:    376.8K
# Total Submissions: 918.9K
# Testcase Example:  '[1,2,3]'
#
# Given a non-empty array of digits representing a non-negative integer, plus
# one to the integer.
# 
# The digits are stored such that the most significant digit is at the head of
# the list, and each element in the array contain a single digit.
# 
# You may assume the integer does not contain any leading zero, except the
# number 0 itself.
# 
# Example 1:
# 
# 
# Input: [1,2,3]
# Output: [1,2,4]
# Explanation: The array represents the integer 123.
# 
# 
# Example 2:
# 
# 
# Input: [4,3,2,1]
# Output: [4,3,2,2]
# Explanation: The array represents the integer 4321.
# 
#
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        l = len(digits)
        carry = 1
        for i in range(l):
            index = l - i - 1
            if digits[index] + carry > 9:
                digits[index] = 0
                carry = 1
            else:
                digits[index] += carry
                carry = 0
        if carry > 0:
            digits.insert(0, carry)
        return digits
        

