class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freq = {}
        if len(s) == len(t):
            for character in s:
                if character not in freq:
                    freq[character] = 1
                else:
                    freq[character] +=1
            for character in t:
                if character not in freq:
                    return False
                else:
                    freq[character] -=1
            for num in freq.values():
                if num != 0:
                    return False
                
            return True
        else:
            return False 
                

