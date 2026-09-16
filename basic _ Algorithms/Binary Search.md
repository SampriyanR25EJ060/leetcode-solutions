Problem Statement:

Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1. You must write an algorithm with $\mathcal{O}(\log n)$ runtime complexity.

Explanation
We initialize two pointers, left and right, at the boundaries of the sorted array. In each iteration, we calculate the middle index mid and compare nums[mid] with the target. If the middle element equals the target, we return its index; otherwise, we eliminate the half of the array where the target cannot reside by shifting either left or right.

Complexity Analysis:

Time Complexity: $\mathcal{O}(\log n)$ — The search space is halved during each iteration step.
Space Complexity: $\mathcal{O}(1)$ — The iterative search operates using only scalar pointer variables.

Approach NotesTechnique: 
Binary Search (Divide and Conquer).Edge Cases Considered: Target smaller than the minimum value, target larger than the maximum value, target absent, and single-element arrays.Key Insight: Halving the search area on every check guarantees logarithmic runtime compared to linear scanning.