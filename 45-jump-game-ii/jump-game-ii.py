class Solution:
    def jump(self, nums: list[int]) -> int:

        n = len(nums)
        count = 0 
        farthest = 0 
        curr = 0 

        for i in range(n-1):

            farthest = max(farthest,i+nums[i])

            if i == curr:
                count += 1
                curr = farthest 
        
        return count 


        