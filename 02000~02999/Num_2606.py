"""
문제
신종 바이러스인 웜 바이러스는 네트워크를 통해 전파된다.
한 컴퓨터가 웜 바이러스에 걸리면 그 컴퓨터와 네트워크 상에서 연결되어 있는 모든 컴퓨터는 웜 바이러스에 걸리게 된다.

예를 들어 7대의 컴퓨터가 <그림 1>과 같이 네트워크 상에서 연결되어 있다고 하자.
1번 컴퓨터가 웜 바이러스에 걸리면 웜 바이러스는 2번과 5번 컴퓨터를 거쳐 3번과 6번 컴퓨터까지 전파되어
2, 3, 5, 6 네 대의 컴퓨터는 웜 바이러스에 걸리게 된다.
하지만 4번과 7번 컴퓨터는 1번 컴퓨터와 네트워크상에서 연결되어 있지 않기 때문에 영향을 받지 않는다.

어느 날 1번 컴퓨터가 웜 바이러스에 걸렸다.
컴퓨터의 수와 네트워크 상에서 서로 연결되어 있는 정보가 주어질 때,
1번 컴퓨터를 통해 웜 바이러스에 걸리게 되는 컴퓨터의 수를 출력하는 프로그램을 작성하시오.

입력
첫째 줄에는 컴퓨터의 수가 주어진다.
컴퓨터의 수는 100 이하이고 각 컴퓨터에는 1번 부터 차례대로 번호가 매겨진다.
둘째 줄에는 네트워크 상에서 직접 연결되어 있는 컴퓨터 쌍의 수가 주어진다.
이어서 그 수만큼 한 줄에 한 쌍씩 네트워크 상에서 직접 연결되어 있는 컴퓨터의 번호 쌍이 주어진다.

출력
1번 컴퓨터가 웜 바이러스에 걸렸을 때, 1번 컴퓨터를 통해 웜 바이러스에 걸리게 되는 컴퓨터의 수를 첫째 줄에 출력한다.
"""

import sys
from collections import deque

inputFast = sys.stdin.readline

in0 = int(inputFast())
in1 = int(inputFast())

temp = []
checkListOriginal = deque()
PCListOriginal = [0 for i in range(in0+1)]
countOne = 0
result = 0


def swap(a, b):
    tt = a
    a = b
    b = tt
    return a, b


for i in range(in1):
    temp = list(map(int, inputFast().split()))
    if temp[1] == 1:
        temp = swap(temp[0], temp[1])
        countOne = countOne + 1
    if temp[0] == 1:
        countOne = countOne + 1
    checkListOriginal.append(temp)

# print(checkListOriginal, '\n')


def findPC(checkList, PCList, target):
    for i in range(in1):
        PCList[target[0]] = 1
        PCList[target[1]] = 1
        targetNext = checkList.popleft()
        # print(target, targetNext)
        if target[1] == targetNext[0]:
            checkList.append([0, 0])
            # print(checkList)
            # print(PCList)
            findPC(checkList, PCList, targetNext)
        elif target[1] == targetNext[1]:
            checkList.append([0, 0])
            findPC(checkList, PCList, swap(targetNext[0], targetNext[1]))

        else:
            checkList.append(targetNext)
            # print(checkList)
            # print(PCList)

    return sum(PCList)


for j in range(countOne):
    for i in range(in1):
        targetTemp = checkListOriginal.popleft()
        if targetTemp[0] == 1:
            checkListOriginal.append([0, 0])
            result = findPC(checkListOriginal, PCListOriginal, targetTemp)
            break
        else:
            checkListOriginal.append(targetTemp)

# result = sum(PCList) - 1
if result == 0:
    print(0)
else:
    print(result-1)