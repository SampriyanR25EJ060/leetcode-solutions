Problem Statement
Given two strings s and t, return true if t is an anagram of s, and false otherwise. An anagram is a word or phrase formed by rearranging the letters of a different word or phrase, using all original letters exactly once.

Explanation
We first compare lengths and immediately return False if the two strings differ in size. Next, we build a character frequency map using string s. We then iterate through string t and subtract character counts; if a character is missing or its frequency drops below zero, the strings cannot be anagrams.

Complexity Analysis:

Time Complexity: $\mathcal{O}(n)$ — We perform two separate iterations over strings of length $n$, where dictionary updates occur in $\mathcal{O}(1)$ time.

Space Complexity: $\mathcal{O}(1)$ or $\mathcal{O}(k)$ — The extra space depends on the size of the alphabet $k$. For standard lowercase English letters, space complexity is bounded by $\mathcal{O}(26) = \mathcal{O}(1)$.

Approach Notes
Technique: Hash Map / Frequency Counter.

Edge Cases Considered: Strings of different lengths, empty strings, and repeated characters where frequencies mismatch.

Key Insight: Counting character frequencies in O(n) time is more efficient than sorting both strings, which would take O(nlogn) time.