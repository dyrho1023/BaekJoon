"""
문제
자연수 n과 정수 k가 주어졌을 때 이항 계수 nCk를
10,007로 나눈 나머지를 구하는 프로그램을 작성하시오.

입력
첫째 줄에 n과 k가 주어진다. (1 ≤ n ≤ 1000, 0 ≤ k ≤ n)

출력
nCk 를 출력한다.
"""

import sys

inputFast = sys.stdin.readline

in1 = list(map(int, inputFast().split()))

parentSmall = in1[0]-in1[1]
parentLarge = in1[0]
childSmall = 1
childLarge = in1[1]

count5PS = 0
count5PL = 0
count5CL = 0
count5CS = 0

count2PS = 0
count2PL = 0
count2CL = 0
count2CS = 0

for i in range(1, 15):
    if 5**i <= parentSmall:
        temp = parentSmall//(5**i)
        count5PS += temp

for i in range(1, 15):
    if 5**i <= parentLarge:
        temp = parentLarge//(5**i)
        count5PL += temp

for i in range(1, 15):
    if 5**i <= childLarge:
        temp = childLarge//(5**i)
        count5CL += temp


for i in range(1, 31):
    if 2**i <= parentSmall:
        temp = parentSmall//(2**i)
        count2PS += temp

for i in range(1, 31):
    if 2**i <= parentLarge:
        temp = parentLarge//(2**i)
        count2PL += temp

for i in range(1, 31):
    if 2**i <= childLarge:
        temp = childLarge//(2**i)
        count2CL += temp


# print(count2PL - count2PS, count2CL)
# print(count5PL - count5PS, count5CL)
# print(count5PL - count5PS - count5CL)
#
#
count2 = count2PL - count2PS - count2CL
count5 = count5PL - count5PS - count5CL
print(min(count2, count5))
