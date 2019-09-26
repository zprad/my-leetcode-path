#
# @lc app=leetcode id=1 lang=python
#
# [1] Two Sum
#
# https://leetcode.com/problems/two-sum/description/
#
# algorithms
# Easy (42.66%)
# Total Accepted:    1.6M
# Total Submissions: 3.7M
# Testcase Example:  '[2,7,11,15]\n9'
#
# Given an array of integers, return indices of the two numbers such that they
# add up to a specific target.
# 
# You may assume that each input would have exactly one solution, and you may
# not use the same element twice.
# 
# Example:
# 
# 
# Given nums = [2, 7, 11, 15], target = 9,
# 
# Because nums[0] + nums[1] = 2 + 7 = 9,
# return [0, 1].
# 
# 
# 
# 
#
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # 通过一个字典（查询时间为O(1)），来空间换取时间
        # 空间：O(n), 时间：O(n)
        map_dict = {}
        length = len(nums)
        for i in range(length):
            ele = target - nums[i]
            if ele in map_dict:
                return [i, map_dict[ele]]
            else:
                map_dict[nums[i]] = i
        return []
        

