Problem Statement
Given the head of a singly linked list, reverse the list, and return the reversed list's head.

Explanation
We traverse the linked list while using two pointers, prev (initialized to None) and curr (initialized to head). At each step, we temporarily store curr.next, reverse curr.next to point back to prev, and shift both prev and curr one node forward. Once curr becomes None, prev serves as the new head of the reversed list.

Complexity Analysis:
Time Complexity: $\mathcal{O}(n)$ — We iterate through the linked list of length $n$ once.Space Complexity: $\mathcal{O}(1)$ — Reversal is performed in-place by updating node pointers without allocating additional memory nodes.

Approach Notes:

Technique: Iterative Pointer Reversal (Three-Pointer Method).Edge Cases Considered: Empty list (head = None), single-node list, and two-node list.

Key Insight: Temporarily storing curr.next before overwriting the reference prevents losing access to the rest of the list during pointer re-assignment.