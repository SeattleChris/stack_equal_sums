# stack_equal_sums

You have three stacks of cylinders where each cylinder has the same diameter, but they may vary in height. You can change the height of a stack by removing and discarding its topmost cylinder any number of times.

Find the maximum possible height of the stacks such that all of the stacks are exactly the same height. This means you must remove zero or more cylinders from the top of zero or more of the three stacks until they are all the same height, then return the height.

## Function Description

Complete the equalStacks function which has the following parameters:

* int h1[n1]: the first array of heights
* int h2[n2]: the second array of heights
* int h3[n3]: the third array of heights

Each array starts with the 'top' and then the following values for each stack.

Returns

* int: the height of the stacks when they are equalized

## Constraints

* 0 <= n1,n2,n3 <= 10^3
* 0 <= height of any cylinder <= 100
