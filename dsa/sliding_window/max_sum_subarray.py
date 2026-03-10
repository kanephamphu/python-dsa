# 1. Maximum Sum Subarray of Size K

# Problem:
# Find the maximum sum of any contiguous subarray of size k.

# Example

# Input: nums = [2,1,5,1,3,2], k=3
# Output: 9
# Explanation: [5,1,3]

def max_sub_array(nums, k):
    """Get the maximum sum of sub array"""
    max_sum = 0

    for index in range(len(nums)- k):
        window_sum = sum(nums[index: index + k])
        max_sum = max(max_sum, window_sum)

    return max_sum

print(max_sub_array([1,3,6,3,6,3,6,9,5,4], 3))
