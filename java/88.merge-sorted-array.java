/*
 * @lc app=leetcode id=88 lang=java
 *
 * [88] Merge Sorted Array
 */

// @lc code=start
class Solution {
    public void merge(int[] nums1, int m, int[] nums2, int n) {
        int index = m + n - 1;
        int i = m - 1;
        int j = n - 1;
        
        while (j >= 0) {
            if (i < 0) {
                nums1[index] = nums2[j];
                j = j - 1;
            } else {
                if (nums1[i] > nums2[j]) {
                    nums1[index] = nums1[i];
                    i = i - 1;
                } else {
                    nums1[index] = nums2[j];
                    j = j - 1;
                }
            }
            
            index -= 1;
        }
    }
}
// @lc code=end

