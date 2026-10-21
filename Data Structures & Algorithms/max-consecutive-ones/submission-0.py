class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        
        max_count, curr_count = 0, 0

        for num in nums:
            if num == 1:
                curr_count += 1
                if curr_count > max_count:
                    max_count = curr_count
            
            if num != 1:
                curr_count = 0
        return max_count
