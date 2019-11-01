/*
 * @lc app=leetcode id=83 lang=java
 *
 * [83] Remove Duplicates from Sorted List
 */
/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
class Solution {

    public ListNode deleteDuplicates(ListNode head) {
        if (head == null) {
            return head;
        }
        int item = head.val;
        ListNode p = head;
        while (p.next != null) {
            if (p.next.val == item) {
                p.next = p.next.next;
            } else {
                item = p.next.val;
                p = p.next;
            }
        }
        return head;
    }
}

