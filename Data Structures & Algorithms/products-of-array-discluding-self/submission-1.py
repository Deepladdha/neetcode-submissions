class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = []
        current = 1
        right = []
        

        for num in nums:
            left.append(current)
            current *= num
        current = 1 
        for num in reversed(nums):
            right.append(current)
            current *= num
        right.reverse()
        output = []
        for i in range(len(nums)):
            result = left[i]*right[i]
            output.append(result)           
        return output

        