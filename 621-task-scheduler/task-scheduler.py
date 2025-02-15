class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        if n==0:
            return len(tasks)
        
        count= Counter(tasks)

        heap= [-count for count in count.values()]
        heapq.heapify(heap)

        time=0
        queue=deque()

        while queue or heap:
            time+=1
            if heap:
                count= heapq.heappop(heap)+1
                if count!=0:
                    queue.append([time+n,count])
            
            if queue and time==queue[0][0]:
                heapq.heappush(heap,queue.popleft()[1])
        
        return time
