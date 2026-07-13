import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        pq = []
        
        for stone in stones:
            heapq.heappush(pq,-stone)

        while len(pq) > 1:

            y = -heapq.heappop(pq)

            x = -heapq.heappop(pq)

            if x != y:
                diff = y - x
                heapq.heappush(pq,-diff)

        if not pq:
            return 0
        
        return -pq[0]



        