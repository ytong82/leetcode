package com.leetcode.twosum;

public class Solution {
    public int[] twoSum(int[] nums, int target) {
    	int[] result = new int[2];  	
    	for (int i=0; i<nums.length; i++) {
    		for (int j=i+1; j<nums.length; j++) {
    			if (nums[j] == target - nums[i]) {
    				result[0] = i;
    				result[1] = j;
    				System.out.println(i + " " + j);
    				break;
    			}
    		}
    	}
    	return result;
    }
}