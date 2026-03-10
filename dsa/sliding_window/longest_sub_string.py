# Problem 1: Longest Substring Without Repeating Characters
# Given a string s, find the length of the longest substring without repeating characters.
# A substring is a contiguous sequence of characters in a string.
# Return the maximum length of such a substring.
# Example:
# Input:
# s = "abcabcbb"
# Output:
# 3

def get_longest_sub_string(original_str):
    """Get the maximum sum of sub array"""
    char_set = set()
    left = 0
    right = 0
    current_max_length_left = 0
    current_max_length_right = 0
    max_length = 0

    for index in range(len(original_str)):
        while original_str[index] in char_set:
            char_set.remove(original_str[left])
            left +=1

        char_set.add(original_str[index])
        right += 1

        if max_length <= len(original_str[left:right]):
            current_max_length_left = left
            current_max_length_right = right

        max_length = max(max_length, len(original_str[left:right]))

    return max_length, original_str[current_max_length_left:current_max_length_right]


# Problem 2: Longest Substring with K Distinct Characters
# Given a string s and an integer k, find the length of the longest substring that contains at most k distinct characters.
# A substring is a contiguous sequence of characters in a string.
# Return the maximum length of such a substring.
# Example
# Input:
# s = "eceba"
# k = 2
# Output:
# 3

# Explanation: The longest substring with at most 2 distinct characters is "ece".


def get_longest_sub_string_with_k_distinct(original_str, k):
    left = 0
    right = 0
    current_max_length_left = 0
    current_max_length_right = 0
    max_length = 0

    for index in range(len(original_str)):
        while len(set(original_str[left: index])) > k:
            left += 1

        right += 1

        if max_length <= len(original_str[left: right]):
            current_max_length_left = left
            current_max_length_right = right

        max_length = max(max_length, len(original_str[left: right]))


    return max_length, original_str[current_max_length_left: current_max_length_right]


# print(get_longest_sub_string("abcgeweeww"))
print(get_longest_sub_string_with_k_distinct("abcgeweewwabc", 3))
