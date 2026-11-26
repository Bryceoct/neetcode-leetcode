class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        # Sort the array so duplicate values become adjacent.
        nums.sort()

        # Start at index 1 to safely compare each element
        # with its predecessor.
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                return True
        return False
    
      

       