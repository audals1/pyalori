from collections import deque


def isPalindrome(ln):
    arr = []
    head = ln.head

    if not head:
        return True

    node = head
    while node:
        arr.append(node.val)
        node = node.next

    while len(arr) > 1: # 요소가 하나만 남을 때 까지 계속 아래 pop 작업을 한다
        first = arr.pop(0) #pop을 하면 배열의 갯수가 그 만큼 줄어든다
        last = arr.pop() # 배열의 pop에 매개변수 없으면 제일 마지막 요소를 꺼낸다
        if first != last:
            return False

    return True # 위의 if 문에 걸리지 않고 while을 다 돌았다면 팰린드롬이다

#괄호문제는 상식적으로 여는 괄호로 시작 해서 닫는 괄호가 여는 괄호의 반대의 순서로 짝 맞춰 져야 한다
#stack 배열을 만들어서 여는 괄호 문자이면 족족 일단 담는다
#담은 stack을 하나씩 꺼내서 닫는 괄호와 페어링이 되는지 확인한다 이 과정에서 pair가 맞는지 확일할 pair 딕셔너리가 필요하다
def test_problem_stack(s):
    pair = {
        '}': '{',
        ')': '(',
        ']': '[',
    }
    opener = "({["
    stack = []

    for char in s:
        if char in opener: #매개변수 문자열에서 문자를 하나씩 꺼내와서 여는 괄호일 경우
            stack.append(char) #이를 족족 stack에 담는다
        else: # 매개변수 문자가 닫는 괄호일 경우
            if not stack:
                return False
            top = stack.pop() #내가 지금 닫는 괄호인데 스택에 제일 마지막놈(여는괄호 중 가장 마지막에 추가한 놈)을 꺼내와서 top에 저장
            if pair[char] != top: #저장한 top이 딕셔너리 pair에 정해 놓은 규칙과 안 맞다?
                return False #잘못됐다

    return not stack


def test_problem_queue(num):
    deq = deque([i for i in range(1, num + 1)])
    while len(deq) > 1:
        deq.popleft()
        deq.append(deq.popleft())
    return deq.popleft()