import heapq

def dijstra(graph, start):
    global check
    INF = float('inf')
    distances = [INF] * (V+1)
    distances[start] = 0
    q = []
    heapq.heappush(q, [distances[start], start])
    while q:
        current_distance, current_node = heapq.heappop(q)
        if current_node == V:
            if current_distance < check:
                check = current_distance
            continue
        for i in graph[current_node]:
            if distances[current_node] + i[0] >= distances[i[1]]:
                continue
            distances[i[1]] = distances[current_node] + i[0]
            heapq.heappush(q, [distances[i[1]], i[1]])
    return distances


T = int(input())

for test_case in range(1, T+1):
    V, E = map(int, input().split())
    Graph = [[] for _ in range(V + 1)]
    check = 999999999999999999999
    for _ in range(E):
        f, t, cost = map(int, input().split())
        Graph[f].append((cost, t))


    result = dijstra(Graph, 0)
    # print(result)
    print(f'#{test_case} {check}')

