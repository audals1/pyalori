from structures import  BinaryMinHeap

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


def selectionsort(lst):
    iters = len(lst) - 1
    for iter in range(iters):
        minimun = iter
        #기준 대비 1등인 애 뺀 나머지 "중에서만" 비교하면 되므로 for문 범위가 아래와 같음
        for cur in range(iter + 1, len(lst)):
            if lst[cur] < lst[minimun]:
                minimun = cur

        if minimun != iter:
            lst[minimun], lst[iter] = lst[iter], lst[minimun]

    return lst

def insertionsort(lst):
    # 0번째 요소는 이미 정렬되어있으니, 1번째 ~ lst(len)-1 번째를 정렬하면 된다.
    for cur in range(1, len(lst)):
        # 비교지점이 cur-1 ~ 0(=cur-cur)까지 내려간다.
        for delta in range(1, cur + 1):
            cmp = cur - delta
            if lst[cmp] > lst[cmp + 1]:
                lst[cmp], lst[cmp + 1] = lst[cmp + 1], lst[cmp]
            else:
                break
    return lst

#퀵 정렬은 배열에서 피벗을 잡고 피벗 기준 작은 집합과 큰 집합으로 일단 나눈다
#나눠진 두 집합 범위 대상으로 퀵정렬을 재귀호출 해서 정렬하고 두 결과를 합치면 정렬 끝
#퀵 정렬에서는 i와 j의 역할을 이해하는게 중요
#j는 피벗 값과 배열의 값을 비교하기 위해 이동하는 인덱스값
#i는 피벗보다 작은 값들이 모여있는 경계다 i는 결국 나중에 피벗값이 재배치될 예정인 인덱스를 구하기 위한 값이다
#한 사이클 돌고나면 피벗은 i + 1자리로 그래야 0~i까지 값(작은값들)이 피벗보다 왼쪽에 있게된다
#이후 피벗은 안움직이고 이 피벗을 기준으로 좌우 배열을 대상으로 재귀호출한다
#이전 과정이 되풀이 되면서 정렬이 끝난다
#풀이시에는 항상 마지막 요소를 피벗으로 잡는다
def quicksort(lst, start, end):
    def partition(part, ps, pe): # 뉴 피벗 구하는 짓
        pivot = part[pe] #배열의 마지막을 피벗으로 설정
        i = ps - 1 #첫 비교때 피벗보다 작은 값이 나오면 i를 +1해줬을때 0이 나와야함
        for j in range(ps, pe): #피벗값과 배열요소를 반복비교하기 위한 반복문
            if part[j] <= pivot: #배열 요소가 피벗값보다 작다면
                i += 1 #피벗경계 범위를 한칸 늘려준다
                part[i], part[j] = part[j], part[i] # 값을 스위칭한다
        #위 반복이 끝나고 나면 i는 피벗보다 작은 집합의 범위이므로 i+1 자리에 피벗을 위치시킨다
        part[i + 1], part[pe] = part[pe], part[i + 1] #경계와 끝값(현피벗)을 스위칭한다
        return i + 1

    if start >= end:
        return None

    p = partition(lst, start, end)
    quicksort(lst, start, p - 1)
    quicksort(lst, p + 1, end)
    return lst

def merge(arr1, arr2):
    result = []
    i = j = 0
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            result.append(arr1[i])
            i += 1
        else:
            result.append(arr2[j])
            j += 1

    while i < len(arr1):
        result.append(arr1[i])
        i += 1

    while j < len(arr2):
        result.append(arr2[j])
        j += 1

    return result


def mergesort(lst):
    if len(lst) <= 1:
        return lst

    mid = len(lst) // 2
    #[1,2,3,4,5]
    #mid = 2
    #L = [1,2]
    #R = [3,4,5]
    L = lst[:mid]
    R = lst[mid:]
    return merge(mergesort(L), mergesort(R))


def heapsort(lst):
    minheap = BinaryMinHeap()
    for elem in lst:
        minheap.insert(elem)

    return [minheap.extract() for _ in range(len(lst))]