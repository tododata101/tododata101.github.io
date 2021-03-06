# 프로그래머스_스택큐_기능개발
# 먼저 배포되어야 하는 순서대로 작업의 진도가 적힌 정수 배열 progresses와 각 작업의 개발 속도가 적힌 정수 배열 speeds가 주어질 때 각 배포마다 몇 개의 기능이 배포되는지를 return 

# progress = [93, 30, 55]
# speeds = [1, 30, 5]

import math

def solution(prog, speed):
    dic = {}
    for p, s in zip(prog, speed):
        t = math.ceil((100-p)/s)
        if dic:
            m = max(dic.keys())
            if t <= m:
                dic[m] += 1
            else:
                dic[t] = 1
        else:
            dic[t] = 1
    return list(dic.values())
  
