class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sub_list = {}
        for word in strs:
            count = [0]*26          
            for ch in word:
                ch_index = ord(ch)-ord("a")
                count[ch_index] += 1
            counts = tuple(count)
            if counts not in sub_list:
                sub_list[counts] = [word]
            else:
                sub_list[counts].append(word)
        return list(sub_list.values())

                
            

                
            



        
        