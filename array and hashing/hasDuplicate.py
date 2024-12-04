from typing import List


class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        map = {}
        for num in nums:
            if num in map:
                return True
            map[num] = True
        return False

# Add test cases
if __name__ == "__main__":
    solution = Solution()
    
    # Test cases
    test_cases = [
        [1, 2, 3, 1],         # Should return True
        [1, 2, 3, 4],         # Should return False
        [1, 1, 1, 3, 3, 4, 3] # Should return True
    ]
    
    for nums in test_cases:
        result = solution.hasDuplicate(nums)
        print(f"Input: {nums}")
        print(f"Has duplicates: {result}\n")

         