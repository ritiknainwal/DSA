class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:

        n = len(nums)
        res = []

        freq = {}

        for i in range(1,n+1):
            freq[i] = 0

        for num in nums:
            freq[num] += 1
        
        for num in freq:
            if freq[num] == 0:
                res.append(num)
        
        return res


        