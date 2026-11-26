class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        # Solve using Hash Set

        seen = set()
        
        for n in nums:  # Iterate over nums.
            if n in seen:   # If n is in our seen set().
                return True # Duplicate has been found.
            seen.add(n) # If n is not in nums, add it to our set.
        return False # If loop finishes without finding a duplicate.

        # Time Complexity: O(n)
        # Space Complexity: O(n)
