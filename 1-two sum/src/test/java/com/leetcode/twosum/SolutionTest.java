package com.leetcode.twosum;

import static org.junit.Assert.assertArrayEquals;
import org.junit.Test;

public class SolutionTest {
	@Test
	public void twoSumTest() {
		int[] nums = {2, 7, 11, 15};
		int target = 9;
		int[] answer = {0, 1};
		
		Solution solution = new Solution();
		int[] result = solution.twoSum(nums, target);
		
		assertArrayEquals(answer, result);
	}
} 