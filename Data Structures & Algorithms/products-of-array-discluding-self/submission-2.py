class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        current = 1
        output = []
        

        for num in nums:
            output.append(current)
            current *= num
        current = 1 
        for i in range(len(nums) - 1, -1, -1):
            output[i] *= current 
            current *= nums[i]

        return output