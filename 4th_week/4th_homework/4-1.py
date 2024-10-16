def bubblesort(lst):
    # 최댓값을 구하는 알고리즘을 len(lst) - 1 만큼 반복한다.
    iters = len(lst) - 1
    for iter in range(iters):
        # 이미 구한 최댓값은 범위에서 제외한다.
        wall = iters - iter # 두개씩 비교할 때 (길이 - 2) 까지만 비교해야함
        #wall = len(lst) - 2로 대체 가능
        #{3,1,2} 2다음이 없으므로 두번째 for문은 1까지만 범위를 잡아야 함 그래야 cur + 1이 범위에 있음
        for cur in range(wall):
            if lst[cur] > lst[cur + 1]:
                lst[cur], lst[cur + 1] = lst[cur + 1], lst[cur]
    return lst

def merge_and_sort(arr1, arr2):
    lst = arr1 + arr2
    sorted_arr = bubblesort(lst)
    return sorted_arr

print(merge_and_sort([1,3,5],[2,4,6]))
print(merge_and_sort([10,5,15],[4,11,2]))