def dfs_recursive(graph, node, visited):
    # 방문처리
    visited.append(node)

    # 인접 노드 방문
    for adj in graph[node]:
        if adj not in visited:
            dfs_recursive(graph, adj, visited)

    return visited


def dfs_stack(graph, start):
    visited = []
    # 방문할 순서를 담아두는 용도
    stack = [start]

    # 방문할 노드가 남아있는 한 아래 로직을 반복한다.
    while stack:
        # 제일 최근에 삽입된 노드를 꺼내고 방문처리한다.
        top = stack.pop()
        visited.append(top)
        # 인접 노드를 방문한다.
        for adj in graph[top]:
            if adj not in visited:
                stack.append(adj)

    return visited


def island_dfs_stack(grid):
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    rows, cols = len(grid), len(grid[0])
    cnt = 0

    for row in range(rows):
        for col in range(cols):
            if grid[row][col] != '1':
                continue

            cnt += 1
            stack = [(row, col)] #방문해야 될 목록

            while stack:
                x, y = stack.pop()
                grid[x][y] = '0'
                for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]
                    if nx < 0 or nx >= rows or ny < 0 or ny >= cols or grid[nx][ny] != '1':
                        continue
                    stack.append((nx, ny))
    return cnt


assert island_dfs_stack(grid=[
    ["1", "1", "1", "1", "0"],
    ["1", "1", "0", "1", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "0", "0", "0"]
]) == 1
assert island_dfs_stack(grid=[
    ["1", "1", "0", "0", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "1", "0", "0"],
    ["0", "0", "0", "1", "1"]
]) == 3


def island_dfs_recursive(grid):
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    rows = len(grid)
    cols = len(grid[0])
    cnt = 0

    def dfs_recursive(r, c):
        if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] != '1':
            return

        # 방문처리
        grid[r][c] = '0'
        for i in range(4):
            dfs_recursive(r + dx[i], c + dy[i])
        return

    for r in range(rows):
        for c in range(cols):
            node = grid[r][c]
            if node != '1':
                continue

            cnt += 1
            dfs_recursive(r, c)

    return cnt


assert island_dfs_recursive(grid=[
    ["1", "1", "1", "1", "0"],
    ["1", "1", "0", "1", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "0", "0", "0"]
]) == 1
assert island_dfs_recursive(grid=[
    ["1", "1", "0", "0", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "1", "0", "0"],
    ["0", "0", "0", "1", "1"]
]) == 3


from collections import deque

def bfs_queue(graph, start):
    visited = [start]
    q = deque([start])

    while q:
        node = q.popleft()
        for adj in graph[node]:
            if adj not in visited:
                q.append(adj)
                visited.append(adj)

    return visited


def island_bfs(grid):
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    rows, cols = len(grid), len(grid[0])
    cnt = 0

    for row in range(rows):
        for col in range(cols):
            if grid[row][col] != '1':
                continue

            cnt += 1
            q = deque([(row, col)])

            while q:
                x, y = q.popleft()
                for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]
                    if nx < 0 or nx >= rows or ny < 0 or ny >= cols or grid[nx][ny] != '1':
                        continue
                    grid[nx][ny] = '0'
                    q.append((nx, ny))
    return cnt


def nqueen(n):
    """
    visited 의 인덱스는 행, 값은 열을 나타낸다.
    (1, 3)에 놓은 경우, visited[1] = 3 으로 표현하겠다는 것.

    예시) n=4 이고 visited = [1, 3, 0, 2] 인 경우,
    체스판을 그려보면 아래와 같다. (1이 퀸)
    0 1 0 0
    0 0 0 1
    1 0 0 0
    0 0 1 0
    """
    visited = [-1] * n
    cnt = 0
    answers = []

    def is_ok_on(nth_row):
        """
        n번째(nth) 행에 퀸을 놓았을 때, 올바른 수인지 검사한다.
        nth 행의 퀸 위치와, 0번째 행부터 n-1번째 행까지 놓여진 퀸의 위치를 비교한다.
        nth 행에 놓여진 퀸이 규칙을 깼다면 False 를 반환한다.
        """
        # 0번째 행 ~ nth_row-1번째 행의 퀸 위치를 차례대로 꺼내온다.
        for row in range(nth_row):
            # 방금 놓여진 nth 퀸은 (nth_row, visited[nth_row]) 에 놓여져있다.
            # 각 행에 차례대로 단 한 번만 두기 때문에 행이 겹치는 것은 검사하지 않아도 된다.
            # 1) 열 번호가 겹치지는 않는지? visited[nth_row] == visited[row]:
            # 2) 또는 대각선으로 존재하지는 않는지? nth_row - row == abs(visited[nth_row] - visited[row]) 살펴본다.
            if visited[nth_row] == visited[row] or nth_row - row == abs(visited[nth_row] - visited[row]):
                return False
        return True

    def dfs(row):
        """
        row 는 퀸을 놓을 행번호를 의미한다.
        dfs(0) 은 0번째 행에서 퀸의 위치를 고르는 것이고,
        dfs(1) 은 1번째 행에서 퀸의 위치를 고르는 것이고,
        ...
        dfs(n-1) 은 n-1번째 행에서 퀸의 위치를 고르는 것이다.
        따라서 row 는 n-1까지 가능하며, n이 되었다는 것은 n개의 퀸을 모두 올바른 위치에 두었다는 의미이다.
        """

        # 0 ~ n-1 행에 퀸을 모두 하나씩 두었을 때 경우의 수를 1 증가시키고 재귀탐색을 종료한다.
        if row >= n:
            # nonlocal 은 지역변수가 아님을 의미한다.
            nonlocal cnt
            cnt += 1
            print("*" * 80)
            print(f"{cnt}번째 답 - visited: {visited}")
            grid = [['.'] * n for _ in range(n)]
            for idx, value in enumerate(visited):
                grid[idx][value] = 'Q'
            result = []
            for row in grid:
                print(row)
                result.append(''.join(row))
            answers.append(result)
            ################
            return

        # visited[row] 의 값을 결정한다.
        # n*n 의 체스판이므로 가능한 열의 범위는 0 ~ n-1 이다.
        for col in range(n):
            # (row, col) 위치에 퀸을 두었다고 가정하고, 규칙을 깨지 않는다면 row+1 행에 다시 퀸을 둔다.
            visited[row] = col
            if is_ok_on(row):
                dfs(row + 1)

    # 0번째 행에 퀸을 둔다.
    dfs(0)
    return answers

#시작과 끝을 정한다 - 절반값과 타겟을 비교한다 - 작으면 왼쪽 크면 오른쪽 - 1~3반복한다
#재귀를 쓰면 좋다 1~3 과정을 함수로 만들어 놓고 재귀한다
def binary_search(nums, target):
    def bs(start, end):
        if start > end:
            return -1

        mid = (start + end) // 2

        if nums[mid] < target:
            return bs(mid + 1, end)
        elif nums[mid] > target:
            return bs(start, mid - 1)
        else:
            return mid

    return bs(0, len(nums) - 1)