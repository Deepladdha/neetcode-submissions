class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_dict = {}
        if not (1 <= len(s) <= 5*10**4) or not (1 <= len(t) <= 5*10**4):
            return False
        if len(s) != len(t):
            return False
        if s.islower()== False or t.islower() == False:
            return False
        for i in s :
            if i in s_dict :
                s_dict[i]+= 1
            else:
                s_dict[i]=1
        for i in t :
            if i not in s :
                return False        
            s_dict[i]-=1
        for i in t:
            if s_dict[i] != 0:
                return False
        return True
            
        

        


        