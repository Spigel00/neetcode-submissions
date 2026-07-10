class Solution:

    def encode(self, strs: List[str]) -> str:
        encode = []
        for char in strs:
            count = len(char)
            new_char = str(count)+'#'+char
            encode.append(new_char)
        return "".join(encode)


    def decode(self, s: str) -> List[str]:
        decode = []
        i = 0
        while i<len(s):
            j = i
            while s[j]!= '#':
                j +=1 
            length = int(s[i:j])
            start = j+1
            end = start + length
            decode.append(s[start:end])
            i = end
        return decode 
                



