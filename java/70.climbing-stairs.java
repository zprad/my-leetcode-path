/*
 * @lc app=leetcode id=70 lang=java
 *
 * [70] Climbing Stairs
 */
class Solution {
    public int climbStairs(int n) {
        int a = 1;
        int b = 2;
        int i = 2;
        if (n == 1) {
            return a;
        } 
        while (i < n) {
            int temp = a + b;
            a = b;
            b = temp;
            i += 1;
        }
        return b;
    }
}

