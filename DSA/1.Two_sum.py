#!/usr/bin/env python3
"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

"""
# Problem: Two Sum

# My Approach:
# Brute force using nested loops → O(n^2)

# Optimal Approach:
# Hash map to store seen numbers

# Key Insight:
# Instead of searching for pairs, store what you've seen

# Pattern:
# Hashing / Complement lookup

# Mistake:
# Thought in terms of pairs instead of complements
''' My Solution '''
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return []
    
''' Best solution'''
class Solution:
    def twoSum(self, nums, target):
        seen = {}

        for i, num in enumerate(nums):
            complement = target - num

            if complement in seen:
                return [seen[complement], i]

            seen[num] = i
# enumerate(nums):
# loops through the list and gives both index and value

# i   = index (0, 1, 2, ...)
# num = value at that index

# example:
# nums = [10, 20, 30]
# output → (0,10), (1,20), (2,30)

# memory trick:
# enumerate = (index, value) together