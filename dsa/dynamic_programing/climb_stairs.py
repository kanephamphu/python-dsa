# 2. Climbing Stairs
# Problem
# You are climbing a staircase. It takes n steps to reach the top.
# Each time you can climb either:
# 1 step
# 2 steps
# Return the number of distinct ways to reach the top.
# Example
# Input
# n = 3
# Output
# 3
# Explanation
# Ways to climb:
# 1 + 1 + 1
# 1 + 2
# 2 + 1
# Constraints
# 1 ≤ n ≤ 45

def climb_stairs(n):
    hash_map = {}

    for i in range(n+1):
        if i == 0:
            hash_map[i] = 0
            
            continue

        if i == 1:
            hash_map[i] = 1

            continue

        if i == 2:
            hash_map[i] = 2

            continue

        hash_map[i] = hash_map[i-1] + hash_map[i-2]

    return (hash_map[n])


print(climb_stairs(45))
