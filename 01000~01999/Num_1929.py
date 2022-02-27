"""
문제
M이상 N이하의 소수를 모두 출력하는 프로그램을 작성하시오.

입력
첫째 줄에 자연수 M과 N이 빈 칸을 사이에 두고 주어진다. (1 ≤ M ≤ N ≤ 1,000,000)
M이상 N이하의 소수가 하나 이상 있는 입력만 주어진다.

출력
한 줄에 하나씩, 증가하는 순서대로 소수를 출력한다..

"""

import sys

inputFast = sys.stdin.readline

[in0, in1] = list(map(int, input().split()))

PrimeList = [1] * (in1+1)
PrimeList[0] = 0
PrimeList[1] = 0

for i in range(2, int(in1**0.5)+1):
    if PrimeList[i] == 1:
        for j in range(2, in1//i+1):
            PrimeList[i*j] = 0

for i in range(in0, in1+1):
    if PrimeList[i] == 1:
        print(i)
#
# k = 0
# while(True):
#     j = numList[k]
#
#     for i in numList[k+1:]:
#         if i % j == 0:
#             numList.remove(i)
#     k += 1
#
#     if numList[k] > in1**0.5:
#         break
#
# for i in numList:
#     if in0 <= i:
#         print(i)
# print(time.time() - start)


