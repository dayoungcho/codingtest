# codingtest
코테공부
- mysql 초기설정: https://adjh54.tistory.com/456


# 코딩테스트를 위한 주요 알고리즘
## 1. 정렬 알고리즘
   - Merge Sort
   - Bubble Sort
   - Quick Sort
   - Heap Sort
   - Insertion Sort
## 2. 자료구조
   - Binary Tree
   - B-Tree
   - Stack
   - Queue
   - Priority Queue
   - LinkedList
   - LinkedHashMap
   - HashTable
## 3. 검색 알고리즘
   - Linear Search
   - Binary Search
## 4. 그래프 탐색 알고리즘
   - Depth-First Search(DFS)
   - Breadth-First Search(BFS)
## 5. 문제 해결 전략
   - 백트래킹
### 완전탐색(Brute-force Search)
- 그냥 가능한 경우를 일일이 다 탐색하는 알고리즘.
#### ex) 백준 2231. 분해합 <br>

어떤 자연수 N이 있을 때, 그 자연수 N의 분해합은 N과 N을 이루는 각 자리수의 합을 의미한다. 어떤 자연수 M의 분해합이 N인 경우, M을 N의 생성자라 한다. 예를 들어, 245의 분해합은 256(=245+2+4+5)이 된다. 따라서 245는 256의 생성자가 된다. 물론, 어떤 자연수의 경우에는 생성자가 없을 수도 있다. 반대로, 생성자가 여러 개인 자연수도 있을 수 있다. <br>
자연수 N이 주어졌을 때, N의 가장 작은 생성자를 구해내는 프로그램을 작성하시오.
<br>
첫째 줄에 답을 출력한다. 생성자가 없는 경우에는 0을 출력한다.
```python
n = input()
for i in range(int(n)):  # 처음부터 끝까지 iterate해서 생성자가 존재하면 break
  j = str(i)
  a = i
  for k in j:
    a += int(k)
  if a==int(n):
    print(i)
    break
  if i==int(n)-1:  # 끝까지 iterate했을 때 생성자가 존재하지 않으면 0 출력
    print(0)
```

### 투 포인터
### 분할 정복
### 다이나믹 프로그래밍
### 그리디 알고리즘
  
## 6. 캐시 교체 알고리즘
   - LRU
   - LFU
## 7. 최단 경로 알고리즘
   - 다익스트라 알고리즘
   - 벨만-포드 알고리즘


# 기타 알아야겠다 싶은 것들
### EOF(End Of File) 처리
  ```python
  while True:
     try:
        # 하고 싶은 작업
     except EOFError:
        break
  ```
- 
