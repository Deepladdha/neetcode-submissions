class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ordered_list = [[] for i in range(len(nums)+1)]
        counts = {}
        for num in nums:
            if num in counts :
                counts[num] += 1
            else:
                counts[num] = 1
        for num,freq in counts.items():
            ordered_list[freq].append(num)
        
        result = []

        for i in range(len(ordered_list)-1,-1,-1):
            for num in ordered_list[i] :
                if len(result) != k:
                    result.append(num)
        return result

        
        

            

        