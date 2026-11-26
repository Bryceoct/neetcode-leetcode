class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        # Create and empty set
        # iterate through each number in a set
        # it n is in nums, return true
        # else, add to set
        # if loop finishes without finding duplicate, return false

        seen = set()

        for n in nums:
            if n in seen:
                return True
            else:
                seen.add(n)
        return False

        # Time complexity: O(n)
        # Space Complexity: O(n) 

        

