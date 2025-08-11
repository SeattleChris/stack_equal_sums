#!/bin/python3

import os

#
# Complete the 'equalStacks' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY h1
#  2. INTEGER_ARRAY h2
#  3. INTEGER_ARRAY h3
#

def equalStacks(h1, h2, h3):
    """Will reverse the lists and use pop to remove from 'top' of stack"""
    stacks = [list(reversed(h)) for h in (h1, h2, h3)]
    num = -1 * len(stacks)
    heights = [sum(h) for h in stacks]
    target = min(heights) + 1
    while any(val != target for val in heights[num:]) and target > 0:
        target -= 1
        if len(heights) > len(stacks):
            target = min(target, *heights[num:])
        for stack, total in zip(stacks, heights[num:]):
            while total > target and stack:
                total -= stack.pop()
            heights.append(total)
    return target

def noreversal_equalStacks(h1, h2, h3):
    """This version works for all tests """
    stacks = (h1, h2, h3)
    heights = sums = [sum(h) for h in stacks]
    indexes = []
    target = min(heights) + 1
    while any(val != target for val in sums) and target > 0:
        target -= 1
        if indexes:
            stacks = [ea[i + 1:] for (ea, i) in zip(stacks, indexes)]
            heights = sums[:]
            target = min(target, *heights)
        indexes, sums = [], []
        for stack, total in zip(stacks, heights):
            idx = -1
            end = len(stack) - 1
            while total > target and idx < end:
                idx += 1
                total -= stack[idx]
            indexes.append(idx)
            sums.append(total)
    return target


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    first_multiple_input = input().rstrip().split()
    n1 = int(first_multiple_input[0])
    n2 = int(first_multiple_input[1])
    n3 = int(first_multiple_input[2])
    h1 = list(map(int, input().rstrip().split()))
    h2 = list(map(int, input().rstrip().split()))
    h3 = list(map(int, input().rstrip().split()))
    result = equalStacks(h1, h2, h3)
    fptr.write(str(result) + '\n')
    fptr.close()
