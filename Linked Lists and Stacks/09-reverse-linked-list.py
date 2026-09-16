# Definition for singly-linked list node.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev = None
        curr = head
        
        while curr:
            next_temp = curr.next  # Save next node
            curr.next = prev       # Reverse current node pointer
            prev = curr            # Move prev forward
            curr = next_temp       # Move curr forward
            
        return prev

# Helper functions for local testing
def to_list(head: ListNode) -> list:
    res = []
    while head:
        res.append(head.val)
        head = head.next
    return res

def create_linked_list(vals: list) -> ListNode:
    dummy = ListNode()
    curr = dummy
    for v in vals:
        curr.next = ListNode(v)
        curr = curr.next
    return dummy.next

# Local Test Cases
if __name__ == "__main__":
    sol = Solution()
    
    # Test Case 1: Standard linked list
    head1 = create_linked_list([1, 2, 3, 4, 5])
    print("Test Case 1 Output:", to_list(sol.reverseList(head1)))  # Expected: [5, 4, 3, 2, 1]
    
    # Test Case 2: Edge case (Single element list)
    head2 = create_linked_list([1])
    print("Test Case 2 Output:", to_list(sol.reverseList(head2)))  # Expected: [1]

    # Test Case 3: Edge case (Empty list)
    head3 = create_linked_list([])
    print("Test Case 3 Output:", to_list(sol.reverseList(head3)))  # Expected: []