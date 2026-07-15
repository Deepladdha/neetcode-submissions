class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen_num = {}
        for i, num in enumerate(nums):
            compliment = target - num
            if  compliment in seen_num:
                return [seen_num[compliment], i]
            seen_num[num] = i
        