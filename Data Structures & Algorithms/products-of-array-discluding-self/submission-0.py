class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []
        

        for i in range(len(nums)):
            temp = nums.copy()
            temp[i]=1
            result = math.prod(temp)
            output.append(result)
        return output

        