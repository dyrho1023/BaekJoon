"""
문제
정수 X에 사용할 수 있는 연산은 다음과 같이 세 가지 이다.

1) X가 3으로 나누어 떨어지면, 3으로 나눈다.
2) X가 2로 나누어 떨어지면, 2로 나눈다.
3) 1을 뺀다.

정수 N이 주어졌을 때, 위와 같은 연산 세 개를 적절히 사용해서 1을 만들려고 한다.
연산을 사용하는 횟수의 최솟값을 출력하시오.

입력
첫째 줄에 1보다 크거나 같고, 106보다 작거나 같은 정수 N이 주어진다.

출력
첫째 줄에 연산을 하는 횟수의 최솟값을 출력한다.
"""

import sys
inputFast = sys.stdin.readline
sys.setrecursionlimit(10000)

in0 = int(inputFast())

dpList = [0 for i in range(in0 + 3)]

dpList[1] = 0
dpList[2] = 1
dpList[3] = 1


for num in range(4, in0+1):
    temp0 = 10000
    temp1 = 10000
    temp2 = 10000

    temp0 = dpList[num-1] + 1
    if num % 3 == 0:
        temp1 = dpList[num//3] + 1

    if num % 2 == 0:
        temp2 = dpList[num//2] + 1

    dpList[num] = min(temp0, temp1, temp2)
    # print(num, dpList[num], temp0, temp1, temp2)

print(dpList[in0])




