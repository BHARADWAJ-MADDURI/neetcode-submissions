class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        uniq = {}

        for n in nums:
            if n in uniq:
                return True
            uniq[n] = 1
        
        return False