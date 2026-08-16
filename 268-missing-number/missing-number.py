class Solution:
    def missingNumber(self, nums: List[int]) -> int:

        n = len(nums)
        freq = {}

        for i in range(n+1):
            freq[i] = 0
        
        for num in nums:
            freq[num] += 1
        
        for num in freq:
            if freq[num] == 0:
                return num 
        



        