import heapq
from typing import List


# Min on first, Max on second
class Pair:

    def __init__(self, first, second):
        self.first = first
        self.second = second

    def __lt__(self, other):

        if self.first != other.first:
            return self.first < other.first

        return self.second > other.second


class Solution:

    def topKFrequent(self, words: List[str], k: int) -> List[str]:

        n = len(words)

        freq = {}

        for i in range(n):
            freq[words[i]] = freq.get(words[i], 0) + 1


        pq = []

        for word, frequency in freq.items():

            curr = Pair(frequency, word)

            heapq.heappush(pq, curr)

            if len(pq) > k:
                heapq.heappop(pq)


        res = []

        while pq:

            res.append(pq[0].second)

            heapq.heappop(pq)


        res.reverse()

        return res