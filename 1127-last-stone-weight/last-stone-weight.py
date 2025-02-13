class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        for i in range(len(stones)):
            stones[i] = -stones[i]

        heapq.heapify(stones)
        while len(stones)>1:
            a=-heapq.heappop(stones)

            b=-heapq.heappop(stones)
\
            if a>b:

                heapq.heappush(stones,b-a)

        return -heapq.heappop(stones) if stones else 0