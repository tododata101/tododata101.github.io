---
title: "Programmers_Python_stack+queue_주식가격"
date: 2021-06-11
categories: Algorithms
---
> [문제링크](https://programmers.co.kr/learn/courses/30/lessons/42584)

{% include adsense.html %}

### 프로그래머스_스택큐_주식가격
- 초 단위로 기록된 주식가격이 담긴 배열 prices가 매개변수로 주어질 때, <br>
  가격이 떨어지지 않은 기간은 몇 초인지를 return 

### 풀이방식
- 가격이 떨어지지 않는 맨 뒤요소는 제외(0)
- 뒤의 요소들과 비교하여 가격이 떨어질때까지 카운트 +1
- 가격이 떨어지면 break
- 각 카운트를 큐에 담음


```python
# prices = [1, 2, 3, 2, 3]
def solution(pr):
    que = []
    # 맨 뒤는 제외
    for i in range(len(pr)-1):
        e = pr[i]
        cnt = 0
        # 해당 가격의 뒤와 비교
        j = i+1
        # 가격이 떨어질 때 cnt를 셈
        while j < len(pr):
            if pr[j] < e:
                cnt += 1
                break
            else:
                cnt += 1
                j += 1
        que.append(cnt)
    # 맨 뒤는 가격이 떨어지는 상황이 없으니 0
    que.append(0)
    return que
 ```
