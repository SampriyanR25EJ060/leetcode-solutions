Problem Statement
Write a function to find the longest common prefix string amongst an array of strings. If there is no common prefix, return an empty string

Explanation
We initialize our candidate prefix as the entire first string in the list. We then iterate through the remaining strings and shorten the candidate prefix character-by-character from the end until the target string starts with it. If the candidate prefix becomes empty during this process, we immediately return

Complexity Analysis:

Time Complexity: $\mathcal{O}(S)$ — Where $S$ is the sum of all characters across all strings in the array.
Space Complexity: $\mathcal{O}(1)$ — Slicing and comparing modifies the string candidate without allocating extra proportional space.

Approach Notes
Technique: Horizontal Scanning.

Edge Cases Considered: Empty array input, strings with no overlapping characters, array containing a single string, and variable string lengths.

Key Insight: Shrinking the candidate prefix sequentially stops early if any word shares no characters with the prefix, minimizing unnecessary string operations.