def lis(arr):
    n = len(arr)

    # DP 배열 초기화: 각 원소는 자기 자신만으로 LIS를 구성할 수 있으므로 초기 값은 1
    dp = [1] * n

    # 배열 순회하며 LIS 계산
    for i in range(1, n):
        for j in range(0, i):
            if arr[i] > arr[j]:  # 현재 원소가 앞의 원소보다 크다면
                dp[i] = max(dp[i], dp[j] + 1)  # dp 값을 갱신

    # LIS의 최대 길이 반환
    return max(dp)


# 테스트
arr = [10, 9, 2, 5, 3, 7, 101, 18]
print(lis(arr))

arr2 = [0, 1, 0, 3, 2, 3]
print(lis(arr2))
