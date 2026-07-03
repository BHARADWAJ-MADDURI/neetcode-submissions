class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        res = {}

        for i, num in enumerate(nums):
            complement = target - nums[i]
            if complement not in res:
                res[num] = i
            else:
                return [res[complement], i]