#
# @lc app=leetcode id=69 lang=python3
#
# [69] Sqrt(x)
#
class Solution:
    def mySqrt(self, x: int) -> int:
        import math
        def sqrt_iter(guess, expectation):
            if good_enough(guess, expectation):
                return guess
            else:
                return sqrt_iter(improve(guess, expectation), expectation)
        def good_enough(guess, x):
            return abs(guess * guess - x) < 0.001
        def improve(guess, x):
            return (guess + x / guess) / 2
        result = sqrt_iter(1.0, x)
        return math.floor(result)
                

