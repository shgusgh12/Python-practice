from collections import defaultdict
import heapq

times = [[2,1,2], [2,3,5], [4,3,3]]
n = 4,
k = 2,

def networkDelayTime(times, n, k):
    graph = defaultdict(list)
    for time in times:
        graph[time[0]].append(time[2], time[1])
    
    # 방문한 노드 기록
    costs = {}
    pq = []
    # 빈 리스트와 넣을 값을 받는다 (가중치, 시작점)
    heapq.heappush(pq, (0,k))

    while pq:
        cur_cost, cur_node = heapq.heappop(pq)
        if cur_node not in costs:
            costs[cur_node] = cur_cost
            for cost, next_node in graph[cur_node]:
                next_cost = cur_cost + cost
                heapq.heappush(pq, (next_cost, next_node))
    
    for node in range(1, n+1):
        if node not in costs:
            return -1
    return max(costs.values())

