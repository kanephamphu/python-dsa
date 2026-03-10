
def max_sub_array(nums, k):
    """Get the maximum sum of sub array"""
    max_sum = 0

    for index in range(len(nums)- k):
        window_sum = 0

        for j in nums[index: index + k]:
            window_sum += j

        max_sum = max(max_sum, window_sum)

    return max_sum

print(max_sub_array([1,3,6,3,6,3,6,9,5,4], 3))
