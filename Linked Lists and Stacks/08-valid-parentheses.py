class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {')': '(', '}': '{', ']': '['}
        
        for char in s:
            if char in mapping:
                top_element = stack.pop() if stack else '#'
                if mapping[char] != top_element:
                    return False
            else:
                stack.append(char)
                
        return not stack

# Local Test Cases
if __name__ == "__main__":
    sol = Solution()
    
    # Test Case 1: Standard input with matching nested brackets
    print("Test Case 1 Output:", sol.isValid("()[]{}"))  # Expected: True
    
    # Test Case 2: Edge case (Mismatched bracket types)
    print("Test Case 2 Output:", sol.isValid("(]"))      # Expected: False