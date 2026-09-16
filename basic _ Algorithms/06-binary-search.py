class Solution:
    def search(self, nums: list[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
                
        return -1

# Local Test Cases
if __name__ == "__main__":
    sol = Solution()
    
    # Test Case 1: Target exists in array
    print("Test Case 1 Output:", sol.search([-1, 0, 3, 5, 9, 12], 9))  # Expected: 4
    
    # Test Case 2: Edge case (Target not found in array)
    print("Test Case 2 Output:", sol.search([-1, 0, 3, 5, 9, 12], 2))  # Expected: -1