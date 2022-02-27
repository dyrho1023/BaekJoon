"""
문제
두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.

입력
첫째 줄에 테스트 케이스의 개수 T가 주어진다.

각 테스트 케이스는 한 줄로 이루어져 있으며, 각 줄에 A와 B가 주어진다. (0 < A, B < 10)

출력
각 테스트 케이스마다 "Case #x: "를 출력한 다음, A+B를 출력한다. 테스트 케이스 번호는 1부터 시작한다.
"""

import sys

inputFast = sys.stdin.readline

in0 = int(inputFast())
in1 = []

for i in range(in0):
    temp = list(map(int, inputFast().split()))
    in1.append(temp)

for i in range(in0):
    print("Case #{}:".format(i+1), sum(in1[i]))
