class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        n = len(nums)

        freq = {}

        for i in range(n):
            freq[nums[i]] = freq.get(nums[i],0) + 1

        
        for num in nums:
            if freq[num] > n/2:
                return num
        