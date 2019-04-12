#
# @lc app=leetcode id=38 lang=python
#
# [38] Count and Say
#
# https://leetcode.com/problems/count-and-say/description/
#
# algorithms
# Easy (39.81%)
# Total Accepted:    267.2K
# Total Submissions: 670.6K
# Testcase Example:  '1'
#
# The count-and-say sequence is the sequence of integers with the first five
# terms as following:
# 
# 
# 1.     1
# 2.     11
# 3.     21
# 4.     1211
# 5.     111221
# 
# 
# 1 is read off as "one 1" or 11.
# 11 is read off as "two 1s" or 21.
# 21 is read off as "one 2, then one 1" or 1211.
# 
# Given an integer n where 1 ≤ n ≤ 30, generate the n^th term of the
# count-and-say sequence.
# 
# Note: Each term of the sequence of integers will be represented as a
# string.
# 
# 
# 
# Example 1:
# 
# 
# Input: 1
# Output: "1"
# 
# 
# Example 2:
# 
# 
# Input: 4
# Output: "1211"
# 
#
class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n == 1:
            return '1'
        i = 1
        a = '1'
        while i < n:
            j = 1
            temp = ''
            pre = a[0]
            count = 1
            while j < len(a):
                if a[j] == pre:
                    count += 1
                else:
                    temp += str(count) + pre
                    pre = a[j]
                    count = 1
                j += 1
            temp += str(count) + pre
            a = temp
            i += 1
        return a



        

