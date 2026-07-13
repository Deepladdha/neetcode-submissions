class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        group = {int(x) for x in nums}
        if len(group)!= len(nums):
            return True
        return False


        