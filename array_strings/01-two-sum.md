Problem Statement
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target. You may assume that each input would have exactly one solution, and you may not use the same element twice. You can return the answer in any order.

ExplanationWe iterate through the array while storing each element's value and index in a hash map (seen). For every number, we calculate its required complement (target - num) and check if it already exists in the dictionary. If present, we immediately return the pair of indices; otherwise, we add the current number to the hash map.Complexity AnalysisTime 

Complexity: — We traverse the array of length $n$ once, where hash map lookups and insertions operate in  average time.Space 
Complexity:  — In the worst-case scenario, we store up to $n$ elements in the hash map.

Approach NotesTechnique: One-Pass Hash Map.Edge Cases Considered: Negative integers, zero values, and duplicate elements that combine to equal the target (e.g., [3, 3] with target 6).Key Insight: Searching in a hash map takes  time compared to an  array search, avoiding a brute-force nested loop approach.