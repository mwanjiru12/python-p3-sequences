#!/usr/bin/env python3

def print_fibonacci(length):
    fibonacci_sequnce = []
    if length > 0:
        fibonacci_sequnce.append(0)
    if length >=2:
        fibonacci_sequnce.append(1)
        for i in range(2, length):
            fibonacci_sequnce.append(fibonacci_sequnce[i-1] + fibonacci_sequnce[i-2])

    print(fibonacci_sequnce)        