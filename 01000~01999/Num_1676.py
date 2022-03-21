"""
문제
N!에서 뒤에서부터 처음 0이 아닌 숫자가 나올 때까지 0의 개수를 구하는 프로그램을 작성하시오.

입력
첫째 줄에 N이 주어진다. (0 ≤ N ≤ 500)

출력
첫째 줄에 구한 0의 개수를 출력한다.
"""

import sys

inputFast = sys.stdin.readline
in0 = int(inputFast())
count_2 = 0
count_5 = 0

num = 1

for i in range(1, in0+1):
    num *= i

while(True):
    if num % 2 == 0:
        num = num//2
        count_2 += 1
    else:
        break

while(True):
    if num % 5 == 0:
        num = num//5
        count_5 += 1
    else:
        break

print(min([count_2, count_5]))