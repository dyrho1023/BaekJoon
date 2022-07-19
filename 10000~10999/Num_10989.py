"""
문제
N개의 수가 주어졌을 때, 이를 오름차순으로 정렬하는 프로그램을 작성하시오.

입력
첫째 줄에 수의 개수 N(1 ≤ N ≤ 10,000,000)이 주어진다. 둘째 줄부터 N개의 줄에는 수가 주어진다.
이 수는 10,000보다 작거나 같은 자연수이다.

출력
첫째 줄부터 N개의 줄에 오름차순으로 정렬한 결과를 한 줄에 하나씩 출력한다.
"""

import sys

inputFast = sys.stdin.readline
in1 = int(inputFast())

countArray = [0 for i in range(10001)]
# resultArray = [0 for i in range(in1)]
# inputNumList = [0 for i in range(in1)]

for i in range(in1):
    temp = int(inputFast())
    # inputNumList[i] = temp
    countArray[temp] = countArray[temp] + 1

# for i in range(10000):
#     countArray[i+1] = countArray[i]+countArray[i+1]

# for i in inputNumList:
#     resultArray[countArray[i]-1] = i
#     countArray[i] = countArray[i] - 1


for i in range(10001):
    if countArray[i] != 0:
        for j in range(countArray[i]):
            print(i)


