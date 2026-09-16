Problem Statement
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid. An input string is valid if open brackets are closed by the same type of brackets, open brackets are closed in the correct order, and every close bracket has a corresponding open bracket of the same type.

Explanation
We iterate through the string using a stack data structure to manage open brackets. When we encounter an opening bracket, we push it onto the stack; when we encounter a closing bracket, we pop the top element from the stack and verify that it matches the corresponding opening bracket. If a mismatch occurs or the stack is non-empty at the end, the string is invalid.

Complexity Analysis:

Time Complexity: $\mathcal{O}(n)$ — We process each character in the string of length $n$ once, with stack push and pop operations taking $\mathcal{O}(1)$ 
Time.Space Complexity: $\mathcal{O}(n)$ — In the worst-case scenario (e.g., a string consisting only of opening brackets like "((((("), the stack will store up to $n$ elements.

Approach Notes
Technique: Stack / Last-In, First-Out (LIFO).

Edge Cases Considered: String starting with a closing bracket, odd string length, unclosed opening brackets left in stack, and incorrectly nested brackets.

Key Insight: A stack naturally maintains the order of expected closing brackets, ensuring the most recently opened bracket is closed first.