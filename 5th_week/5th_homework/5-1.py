import heapq

def min_travel_cost(graph, start, end):

    dists = {node: float('infinity') for node in range(1, len(graph) + 1)}

    q = [(0, start)]
    dists[start] = 0

    while q:
        cur_dist, cur_node = heapq.heappop(q)

        if dists[cur_node] < cur_dist:
            continue

        for adj, d in graph[cur_node].items():
            new_dist = cur_dist + d
            if new_dist < dists[adj]:
                dists[adj] = new_dist
                heapq.heappush(q, (new_dist, adj))

    return dists[end]



graph = {
    1: {2: 4, 3: 2},
    2: {3: 5, 4: 1},
    3: {4: 7},
    4: {}
}

A, B = 1, 4
print(min_travel_cost(graph, A, B))
