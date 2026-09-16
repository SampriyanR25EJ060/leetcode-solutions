class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        insert_pos = 0
        
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[insert_pos], nums[i] = nums[i], nums[insert_pos]
                insert_pos += 1

# Local Test Cases
if __name__ == "__main__":
    sol = Solution()
    
    # Test Case 1: Standard input with mixed numbers and zeroes
    nums1 = [0, 1, 0, 3, 12]
    sol.moveZeroes(nums1)
    print("Test Case 1 Output:", nums1)  # Expected: [1, 3, 12, 0, 0]
    
    # Test Case 2: Edge case (Array consisting entirely of zeroes)
    nums2 = [0, 0, 0]
    sol.moveZeroes(nums2)
    print("Test Case 2 Output:", nums2)  # Expected: [0, 0, 0]