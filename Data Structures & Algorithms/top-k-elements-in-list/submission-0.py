class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequent_nums = []
        counts = {}
        for num in nums:
            if num in counts :
                counts[num] += 1
            else:
                counts[num] = 1

        sorted_dict = dict(sorted(counts.items(), key=lambda item: item[1], reverse = True))
        sorted_keys = list(sorted_dict.keys())
        for i in range(k):
            frequent_nums.append(sorted_keys[i])
        return frequent_nums

            

        