class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for num in nums:
            if num not in freq:
                freq[num] = 1
            else:
                freq[num] += 1
        sorted_freq= sorted(freq.items(), key=lambda item: item[1], reverse=True)
        ans = []
        for num, count in sorted_freq[:k]:
            ans.append(num)

        return ans

            
            
       


        