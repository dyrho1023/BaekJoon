"""
문제
자연수 n과 정수 k가 주어졌을 때 이항 계수
nCk를 구하는 프로그램을 작성하시오.

입력
첫째 줄에 n과 k가 주어진다. (1 ≤ n ≤ 10, 0 ≤ k ≤ n)

출력

nCk 를 출력한다.
"""
import sys

inputFast = sys.stdin.readline
in1 = list(map(int, inputFast().split()))
parents = 1
children = 1
for i in range(1, in1[1]+1):
    parents *= in1[0]
    in1[0] -= 1
    children *= i
print(int(parents/children))



