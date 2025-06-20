
"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

Example:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
"""
#The Easy Way
def twoSum(nums, target):
        
        # :type nums: List[int]
        # :type target: int
        # :rtype: List[int]
        
        for i in range(len(nums)):
             for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                  print([i, j])
                  return 0

#The Other way

def twoSum2(nums, target):
    num_to_index = {}  # Dictionary to store number and its index

    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_to_index:
            return [num_to_index[complement], i]
        num_to_index[num] = i

    # If no solution is found, though problem states there's always one solution
    return []


arr=[1,2,3,4]
no=7
twoSum(arr,no) # type: ignore






        