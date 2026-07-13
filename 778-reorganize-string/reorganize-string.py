import heapq

class Pair:
    def __init__(self,first,second):
        self.first = first
        self.second = second

    def __lt__(self,other):

        if self.first != other.first:
            return self.first > other.first
            
        return self.second < other.second


class Solution:
    def reorganizeString(self, s: str) -> str:

        freq = {}

        for ch in s:
            freq[ch] = freq.get(ch,0) + 1

        pq = []

        for ch,frequency in freq.items():
            p = Pair(frequency,ch)
            heapq.heappush(pq,p)

        res = []

        while pq:

            p = heapq.heappop(pq)

            if len(res) == 0 or res[-1] != p.second:

                res.append(p.second)

                p.first -= 1

                if p.first > 0:

                    heapq.heappush(pq,p)

            
            else:

                if not pq:
                    return ""

                
                p2 = heapq.heappop(pq)
                res.append(p2.second)

                p2.first -= 1

                if p2.first > 0:
                    heapq.heappush(pq,p2)

                heapq.heappush(pq,p)
                
        return "".join(res)

