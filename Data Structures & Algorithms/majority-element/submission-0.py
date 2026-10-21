class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        
        x = len(nums) // 2

        return nums[x]