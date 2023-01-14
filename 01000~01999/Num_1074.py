"""
문제
한수는 크기가 2^N × 2^N인 2차원 배열을 Z모양으로 탐색하려고 한다.
예를 들어, 2×2배열을 왼쪽 위칸, 오른쪽 위칸, 왼쪽 아래칸, 오른쪽 아래칸 순서대로 방문하면 Z모양이다.


N > 1인 경우, 배열을 크기가 2^(N-1) × 2^(N-1)로 4등분 한 후에 재귀적으로 순서대로 방문한다.
다음 예는 2^2 × 2^2 크기의 배열을 방문한 순서이다.

N이 주어졌을 때, r행 c열을 몇 번째로 방문하는지 출력하는 프로그램을 작성하시오.
다음은 N=3일 때의 예이다.


입력
첫째 줄에 정수 N, r, c가 주어진다.

출력
r행 c열을 몇 번째로 방문했는지 출력한다.
"""

import sys

inputFast = sys.stdin.readline

(N, r, c) = list(map(int, inputFast().split()))
standard = 0

for i in range(N, 1, -1):
    if 2**(i-1)-1 < r:
        y_flag = 1
        r = r-2**(i-1)
    else:
        y_flag = 0

    if 2**(i-1)-1 < c:
        x_flag = 1
        c = c-2**(i-1)
    else:
        x_flag = 0

    if (x_flag == 1) & (y_flag == 1):
        standard = standard + (4**(i-1))*3
    elif (x_flag == 0) & (y_flag == 1):
        standard = standard + (4**(i-1))*2
    elif (x_flag == 1) & (y_flag == 0):
        standard = standard + (4**(i-1))*1
    else:
        pass
        #standard = standard + 4**(i-1) - 1

    if (r < 2) & (c < 2):
        break

    # print(i, r, c, x_flag, y_flag, standard)


standard = standard + r*2 + c

print(standard)
