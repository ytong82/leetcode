package com.leetcode.twosum;

import java.util.HashMap;
import java.util.Map;

public class Solution {
    public int[] twoSum(int[] nums, int target) {
    	int[] result = new int[2];  	
    	
    	Map<Integer, Integer> map = new HashMap<Integer, Integer>();
    	for (int index=0; index<nums.length; index++) {
			int key = target - nums[index];
			if (map.containsKey(key)) {
				result[0] = map.get(key);
				result[1] = index;
				break;
			}
    		map.put(nums[index], index);
    	}
    	return result;
    }
}