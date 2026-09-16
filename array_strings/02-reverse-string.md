Problem Statement:

Write a function that reverses a string given as an array of characters s. You must do this by modifying the input array in-place with extra memory.

Explanation
We place two pointers at opposite ends of the character list: left at index 0 and right at index len(s) - 1. We swap the characters at these pointers in each step and increment left while decrementing right. The process terminates when the two pointers meet or cross each other.

Complexity Analysis:

Time Complexity: We perform $n / 2$ character swaps, resulting in linear processing time relative to string length.
Space Complexity: Swapping is done directly within the input list without allocating auxiliary space.

Approach Notes
Technique: Two-Pointer Approach.

Edge Cases Considered: Single-character lists, empty inputs, and strings with an even or odd number of characters.

Key Insight: Reversing in-place eliminates the need to create a new list or string, adhering strictly to constant memory requirements.