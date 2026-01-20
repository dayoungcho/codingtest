# codingtest
코테공부
- mysql 초기설정: https://adjh54.tistory.com/456


# 코딩테스트를 위한 주요 알고리즘
## 1. 정렬 알고리즘
   - Selection Sort
        <br>가장 작은 데이터를 선택해 맨 앞에 있는 데이터와 바꾸고, 그 다음 작은 데이터를 선택해 앞에서 두 번째 데이터와 바꾸고, .... 이 과정을 반복
        <br> 시간 복잡도는 $O(N^2)$으로, 시간 복잡도 측면에서 매우 비효율적임.

```python
num_list = [5,2,3,1,4,2,3,5,1,7]
n = len(num_list)

for i in range(n):
   min_index = i
   for j in range(i+1,n):
      if num_list[j] < num_list[i]:
         min_index = j
   num_list[i], num_list[min_index] = num_list[min_index], num_list[i]
print(num_list)  # [1,1,2,2,3,3,4,5,5,7]
```


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
### 백트래킹
### 유클리드 호제법(Euclidean algorithm)
- 최대공약수(GCD), 최소공배수 구하는 알고리즘
- 최대공약수와 최소공배수의 법칙: **a * b = (a와 b의 최대공약수) * (a와 b의 최소공배수)**
- a를 b로 나눈 나머지를 구해 이것을 새로운 b로 사용하고, 이전의 b를 a로 사용하는 과정을 나머지가 0이 될떄까지 반복
- 나머지가 0이 되기 전 마지막 나머지가 두 수의 최대공약수임
#### ex) 백준 2609. 최대공약수와 최소공배수 <br>
두 개의 자연수를 입력받아 최대 공약수와 최소 공배수를 출력하는 프로그램을 작성하시오.
```python
a, b = map(int, input().split())
mul = a*b
while True:
  a, b = b, a%b
  if b==0:
    break
print(a)
print(int(mul/a))
```

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
