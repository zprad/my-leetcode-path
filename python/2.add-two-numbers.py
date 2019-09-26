#
# @lc app=leetcode id=2 lang=python
#
# [2] Add Two Numbers
#
# https://leetcode.com/problems/add-two-numbers/description/
#
# algorithms
# Medium (30.78%)
# Total Accepted:    810.6K
# Total Submissions: 2.6M
# Testcase Example:  '[2,4,3]\n[5,6,4]'
#
# You are given two non-empty linked lists representing two non-negative
# integers. The digits are stored in reverse order and each of their nodes
# contain a single digit. Add the two numbers and return it as a linked list.
# 
# You may assume the two numbers do not contain any leading zero, except the
# number 0 itself.
# 
# Example:
# 
# 
# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8
# Explanation: 342 + 465 = 807.
# 
# 
#
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        result = ListNode(0)
        pointer = result
        pre = 0
        while l1 != None and l2 != None:
            num = l1.val + l2.val + pre
            pre = num // 10
            current = num % 10
            pointer.next = ListNode(current)
            pointer = pointer.next
            l1 = l1.next
            l2 = l2.next
        if l1 != None:
            pointer.next = self.addTwoNumbers(l1, ListNode(pre))
        elif l2 != None:
            pointer.next = self.addTwoNumbers(l2, ListNode(pre))
        elif pre != 0:
            pointer.next = ListNode(pre)
            
        return result.next

        

