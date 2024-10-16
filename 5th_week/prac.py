import heapq


def dijkstra(graph, start):
    INF = 1e9
    N = len(graph)
    dist = [INF] * N

    q = []
    # 튜플일 경우 0번째 요소 기준으로 최소 힙 구조.
    # 첫 번째 방문 누적 비용은 0이다.
    heapq.heappush(q, (0, start)) #heapq 동작방식은 쌍 값일 때, (a, b) a값 기준으로 동작하므로 첫번째에 기준값을 넣는다
    dist[start] = 0

    while q:
        # 누적 비용이 가장 작은 녀석을 꺼낸다.
        acc, cur = heapq.heappop(q)

        # 이미 답이 될 가망이 없다.
        if dist[cur] < acc:
            continue

        # 인접 노드를 차례대로 살펴보며 거리를 업데이트한다.
        for adj, d in graph[cur]:
            cost = acc + d
            if cost < dist[adj]:
                dist[adj] = cost
                heapq.heappush(q, (cost, adj))

    return dist


def delay_time(arr, n, k):
    graph = {}

    for u, v, w in arr:
        if u not in graph:
            graph[u] = []
        graph[u].append((v, w))

    Q = [(0, k)]
    dist = {}

    while Q:
        time, node = heapq.heappop(Q)
        if node not in dist:
            dist[node] = time
            if node in graph:
                for v, w in graph[node]:
                    alt = time + w
                    heapq.heappush(Q, (alt, v))

    if len(dist) == n:
        return max(dist.values())

    return -1


def fibo(n):
    if n in [1, 2]:
        return 1
    return fibo(n-1) + fibo(n-2)


memo = {1: 1, 2: 1}


def fibo_dp(n):
    if n in memo:
        return memo[n]
    memo[n] = fibo_dp(n - 1) + fibo_dp(n - 2)
    return memo[n]


def cal_seat(N, seats):
    # 피보나치 수열 초기화
    memo = {
        1: 1,  # Fibo(1) = 1
        2: 2   # Fibo(2) = 2
    }

    # 피보나치 수열 계산 함수
    def fibo(n, memo):
        if n in memo:
            return memo[n]

        # 이전 두 항의 값을 더하여 현재 항의 값을 계산
        nth_fibo = fibo(n - 1, memo) + fibo(n - 2, memo)
        memo[n] = nth_fibo
        return nth_fibo

    # 가능한 모든 경우의 수 초기화
    ways = 1
    current = 0

    # VIP 좌석마다 경우의 수 계산
    for seat in seats:
        fixed = seat - 1
        # 현재 VIP 좌석까지의 좌석 개수만큼 피보나치 수열을 계산하여 경우의 수에 곱함
        count = fibo(fixed - current, memo)
        ways *= count
        # 다음 VIP 좌석부터 계산하기 위해 현재 위치를 변경
        current = fixed + 1

    # 마지막 좌석부터 끝까지의 경우의 수 계산
    count = fibo(N - current, memo)
    ways *= count

    return ways