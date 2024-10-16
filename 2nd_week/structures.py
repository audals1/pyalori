class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, val):
        if not self.head:
            self.head = ListNode(val, None)
            return

        node = self.head #현재 노드 처음엔 헤드를 현재 노드로 설정
        while node.next: #다음 노드가 있을 때는
            node = node.next #현재 노드를 계속 그 다음 노드로 바꿔 준다 그럼 제일 마지막 노드가 현재 노드가 된다

        node.next = ListNode(val, None) # 다음 노드가 없으면 새로운 노드를 생성 한다


class Node:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

class Stack:
    def __init__(self):
        self.top = None

    def push(self, val): #LinkedList와 반대로, 새로 생긴 노드가 이전 노드를 가리키는 식으로 누적 (현 top)ㅁ -> ㅁ -> (최초 top)ㅁ ...
        self.top = Node(val, self.top)


    def pop(self):
        if not self.top:
            return None

        node = self.top #현재 top을 노드에 저장
        self.top = node.next # 현재 top을 현 노드의 next로 변경
        return node.val #현 노드를 넥스트 노드로 바꾸고 나서 이전 값을 리턴해야 완성
    # (현 top)ㅁ -> (현 next)ㅁ -> (최초 top)ㅁ pop실행 ㅁ(pop해서 값 return) -> ㅁ(현 top) -> (최초탑) ㅁ

    def is_empty(self):
        return self.top is None



class Queue:
    def __init__(self):
        self.front = None

    def push(self, value):
        if not self.front:
            self.front = Node(value)
            return

        node = self.front
        while node.next:
            node = node.next
        node.next = Node(value)

    def pop(self):
        if not self.front: #제일 앞에 노드가 비어있으면
            return None #None을 return
#if문에 들어가지 않고 제일 앞 노드에 뭔가가 있다면
        node = self.front #현 제일 앞 노드를 일단 저장
        self.front = self.front.next # 다음 노드를 현 제일 앞 노드로 설정, 이걸 안하면 이전 노드가 계속 제일 앞 노드로 되어있어서 원하는 결과가 안 나옴
        return node.val #저장해놨던 이전의 프론트 노드 값을 return

    def is_empty(self):
        return self.front is None


#해시테이블은 키 값 페어의 자료구조 딕셔너리 같은 것임
#해시함수(나머지연산)을 사용해서 키 값의 범위를 특정 범위로 고정시킴 ex)size = 10이면 0~9까지 범위로 한정된다
#필연적으로 충돌이 발생한다 그럴 경우 체이닝 오픈 어드레싱이라는 방법을 쓴다
#오픈어드레싱은 키 값이 충돌됐을때 값이 빈 인덱스를 다음 다음 다음 해서 찾아나감 key : 1 val : 15가 이미 있어버리면, key : 5 val : None 이면 키 값 5에 도달할때까지 탐색해서 그 자리에 넣음
#체이닝은 충돌된 키값에 연결리스트 형태로 값을 붙여 나간다. ex) key : 1 val : 15 -> 8
#파이썬은 오픈어드레싱을 사용하고 체이닝은 c++ java를 채택하고 있다
#그럼 이 자료구조는 왜 이렇게 하면서까지 쓸까? 시간복잡도 때문이다. 충돌이 안 나면 O(1)이다 충돌 나서 연결리스트로 가도 최대가 O(N)이다


class HashNode:
    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value
        self.next = None


class HashTable:
    def __init__(self):
        self.size = 10
        self.table = [None] * self.size

    def _hash_function(self, key): # 임의로 들어온 데이터를 고정 크기 값으로 매핑하는데 쓰는 함수가 해시함수다
        return key % self.size # 가장 대표적인 해시함수가 나머지연산임. 무슨 값이든 3으로 나머지 연산 하면 값이 아무리 커도 0,1,2까지만 나온다

    # 뭐든 해시테이블 연산에서는 일단 해시함수로 인덱스를 구하는거부터 시작해서 구한 인덱스에 해당하는 테이블의 값을 목적에 따라 비교
    # 아래 방식은 체이닝 방식이다 연결리스트를 이용한 방법
    def put(self, key, value):
        index = self._hash_function(key)
        if self.table[index] is None: # 해시테이블이 비어있다?
            self.table[index] = HashNode(key, value) # 새로 생성해서 그 인덱스에 키랑 값을 넣어라
        else: # 해당 인덱스에 값이 있다?
            node = self.table[index] # 해당 노드를 일단 변수에 저장해 놓고, 작업 스타트
            while node.next is not None: # 가리키는 다음 노드에 값이 있으면
                node = node.next # 현 노드를 다음 노드로 계속 바꿔줌
            node.next = HashNode(key, value) # 더 없다면 새 노드를 마지막 자리에 새로 생성

    def get(self, key):
        index = self._hash_function(key) # 해시함수로 인덱스를 구함
        node = self.table[index] # 그 노드를 일단 변수에 저장
        while node is not None: # 그 노드가 비어있지 않는 한 반복
            if node.key == key: # 그 노드의 키값과 받은 키 값이 같으면?
                return node.value # 그 노드의 값을 반환해라
            node = node.next # 키 값이 다르면 다음 노드를 현재 노드로 바꿔서 계속 검사
        return -1 # while문 다 돌았는데 없다면 해당 키 값이 테이블에 없다는 것임


    def remove(self, key):
        index = self._hash_function(key)
        node = self.table[index]
        prev_node = None # 연결리스트가 단방향 구조라서 이전 노드를 꾸준히 관리해줘야 삭제가 가능하다 처음에는 이전노드는 없다
        while node is not None:
            if node.key == key:
                if prev_node is None: # 이전 노드가 없는 노드를 지워야 하는 상황이라면?
                    self.table[index] = node.next # A -> B 에서 A를 지워야 한다면 A자리에 B를 할당해주면 A는 사라지는것과 같다
                else:
                    prev_node.next = node.next  # 현 노드를 지운다는건 A(prev) -> B(node) -> (node.next)C 이 상태에서 A가 C를 가리키게 한다는것이다
                return
            # 키 값을 못 찾았다? 노드들을 한칸씩 밀어줘야한다
            prev_node = node
            node = node.next



    class BinaryMaxHeap:
        def __init__(self):
            # 계산 편의를 위해 0이 아닌 1번째 인덱스부터 사용한다.
            self.items = [None]

        def insert(self, k):
            self.items.append(k)
            self._percolate_up()

        def _percolate_up(self):
            # percolate: 스며들다.
            cur = len(self.items) - 1 # [1,2,3] 길이는 3 마지막 인덱스는 2이므로 len - 1이 현재 인덱스 값임 append는 제일 뒤에 추가하는 것이므로 현 인덱스는 마지막 인덱스임
            # left 라면 2*cur, right 라면 2*cur + 1 이므로 parent 는 항상 cur // 2
            parent = cur // 2

            while parent > 0: # 루트가 될 때까지 반복
                if self.items[cur] > self.items[parent]:
                    self.items[cur], self.items[parent] = self.items[parent], self.items[cur] # 값 스위칭 코드

                cur = parent # 값들 갱신, 현재값은 부모값으로
                parent = cur // 2 # 부모값은 현재값의 나누기 2한 몫으로 갱신 이진트리는 자식이 최대 2개뿐이므로 나누기 2를 한 몫이 부모의 인덱스가 나옴

        def extract(self):
            if len(self.items) - 1 < 1:
                return None

            root = self.items[1]
            self.items[1] = self.items[-1]
            self.items.pop()
            self._percolate_down(1)

            return root

        def _percolate_down(self, cur):
            biggest = cur
            left = 2 * cur
            right = 2 * cur + 1

            if left <= len(self.items) - 1 and self.items[left] > self.items[biggest]:
                biggest = left

            if right <= len(self.items) - 1 and self.items[right] > self.items[biggest]:
                biggest = right

            if biggest != cur:
                self.items[cur], self.items[biggest] = self.items[biggest], self.items[cur]
                self._percolate_down(biggest)