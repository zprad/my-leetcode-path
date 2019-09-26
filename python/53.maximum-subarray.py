#
# @lc app=leetcode id=53 lang=python
#
# [53] Maximum Subarray
#
# https://leetcode.com/problems/maximum-subarray/description/
#
# algorithms
# Easy (43.05%)
# Total Accepted:    487.1K
# Total Submissions: 1.1M
# Testcase Example:  '[-2,1,-3,4,-1,2,1,-5,4]'
#
# Given an integer array nums, find the contiguous subarray (containing at
# least one number) which has the largest sum and return its sum.
# 
# Example:
# 
# 
# Input: [-2,1,-3,4,-1,2,1,-5,4],
# Output: 6
# Explanation: [4,-1,2,1] has the largest sum = 6.
# 
# 
# Follow up:
# 
# If you have figured out the O(n) solution, try coding another solution using
# the divide and conquer approach, which is more subtle.
# 
#
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ## 该问题可以转化为：求以i元素为
        l = len(nums)
        if l < 1:
            return 0
        subarray_sum = [nums[0]]
        max_sum = nums[0]
        for i in range(1, l):
            if subarray_sum[i - 1] < 0:
                subarray_sum.append(nums[i])
            else:
                subarray_sum.append(subarray_sum[i - 1] + nums[i])
            if subarray_sum[i] > max_sum:
                max_sum = subarray_sum[i]
        return max_sum

        

