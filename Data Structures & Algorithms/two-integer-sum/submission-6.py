class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        res = {}

        for i, num in enumerate(nums):
            complementary = target - num

            if complementary in res:
                return [res[complementary], i]
            res[num] = i
        return []
