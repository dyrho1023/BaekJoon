"""
문제
세 점이 주어졌을 때, 축에 평행한 직사각형을 만들기 위해서 필요한 네 번째 점을 찾는 프로그램을 작성하시오.

입력
세 점의 좌표가 한 줄에 하나씩 주어진다. 좌표는 1보다 크거나 같고, 1000보다 작거나 같은 정수이다.

출력
직사각형의 네 번째 점의 좌표를 출력한다.
"""

import sys
import math

inputFast = sys.stdin.readline
in0 = []
in1 = []


for i in range(3):
    [temp0, temp1] = list(map(int, inputFast().split()))
    in0.append(temp0)
    in1.append(temp1)

if in0[0] == in0[1]:
    resultX = in0[2]
elif in0[0] == in0[2]:
    resultX = in0[1]
else:
    resultX = in0[0]

if in1[0] == in1[1]:
    resultY = in1[2]
elif in1[0] == in1[2]:
    resultY = in1[1]
else:
    resultY = in1[0]

print(resultX, resultY)

