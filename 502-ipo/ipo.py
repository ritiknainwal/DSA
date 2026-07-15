class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:

        n = len(profits)
        proj = []

        for i in range(n):
            proj.append((capital[i],profits[i]))
        
        proj.sort()

        pq = []
        ind = 0

        while k:
            while ind < n:
                if proj[ind][0] > w:
                    break
                
                heapq.heappush(pq,-proj[ind][1])
                ind += 1

            
            if not pq:
                return w
            
            w = w + (-heapq.heappop(pq))

            k -= 1
        
        return w
        

        