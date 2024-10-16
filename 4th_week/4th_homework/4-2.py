def max_meetings(meetings):
    # 회의 시간대를 종료 시간 기준으로 정렬
    sorted_meetings = sorted(meetings, key=lambda x: x[1])

    count = 0  # 선택된 회의 수
    last_end_time = -1  # 마지막으로 선택된 회의의 종료 시간

    for start, end in sorted_meetings:
        # 현재 회의의 시작 시간이 마지막으로 선택된 회의의 종료 시간보다 크거나 같은 경우 선택
        if start >= last_end_time:
            count += 1
            last_end_time = end

    return count


# 예시 실행
meetings = [(0, 6), (1, 4), (3, 5), (3, 8), (5, 7), (8, 9)]
print(max_meetings(meetings))