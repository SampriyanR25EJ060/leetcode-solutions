Problem Statement
Given an integer array nums, move all 0s to the end of it while maintaining the relative order of the non-zero elements. You must do this in-place without making a copy of the array.

Explanation
We maintain an insert_pos pointer tracking the index where the next non-zero element should be placed. As we iterate through the array with pointer i, every time we encounter a non-zero element, we swap it with the element at insert_pos and increment insert_pos. This effectively bubbles all non-zero elements to the front and pushes all zeroes to the end.

Complexity Analysis:

Time Complexity: $\mathcal{O}(n)$ — We iterate through the array of length $n$ once.
Space Complexity: $\mathcal{O}(1)$ — Elements are swapped directly in-place without using extra memory.

Approach Notes
Technique: Two-Pointer Swap / Partition Variant.

Edge Cases Considered: Array with all zeroes, array with no zeroes, single-element array, and zeroes already at the end.

Key Insight: Swapping non-zero elements into insert_pos preserves the relative order of non-zero elements while pushing zeroes backward in a single pass.