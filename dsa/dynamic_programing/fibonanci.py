# 1. Fibonacci
# Problem
# The Fibonacci sequence is defined as:
# F(0) = 0
# F(1) = 1
# F(n) = F(n − 1) + F(n − 2) for n > 1
# Given an integer n, return the nth Fibonacci number.
# Example
# Input
# n = 5
# Output
# 5
# Explanation
# F(0)=0
# F(1)=1
# F(2)=1
# F(3)=2
# F(4)=3
# F(5)=5
# Constraints
# 0 ≤ n ≤ 30

def fibonanci(num):
    fibo_hash_map = {}

    for i in range(num + 1):
        if i in [0, 1, 2]:
            fibo_hash_map[i] = 1
        else:
            fibo_hash_map[i] = fibo_hash_map[i - 1] + fibo_hash_map[i - 2]
    
    print(fibo_hash_map[num])
