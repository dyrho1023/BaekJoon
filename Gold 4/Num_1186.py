"""
문제
2차원 좌표 평면에 변이 축에 평행한 직사각형 N개가 있다. 직사각형은 1부터 N까지 번호가 매겨져 있다.
i번 직사각형의 왼쪽 아래 꼭짓점의 좌표는 (xi,1, yi,1)이고, 오른쪽 위 꼭짓점의 좌표는 (xi,2, yi,2)이다.
N개의 직사각형 중 K개를 칠해 색칠된 영역의 최댓값을 구해보자.

일부 영역은 하나 이상의 직사각형이 있을 수도 있다.
이 경우 그 영역에 있는 직사각형 중 가장 높은 번호를 가진 직사각형만 보이는 것이다. 예제 1을 참고한다.

입력
첫째 줄에 두 정수 N, K가 주어진다. 둘째 줄부터 N개의 줄에 직사각형을 나타내는 네 정수 xi,1, yi,1, xi,2, yi,2가 주어진다.

출력
첫째 줄에 색칠한 면적을 최대로 하려면, 어떤 직사각형을 칠해야 하는지 출력한다.
빈 칸으로 구분하며, 여러 가지일 경우에는 사전순으로 앞서는 것을 출력한다.

제한
1 ≤ K ≤ N ≤ 50
-10,000 ≤ xi,1, yi,1, xi,2, yi,2 ≤ 10,000
xi,1 < xi,2
yi,1 < yi,2
"""

import sys
import itertools

inputFast = sys.stdin.readline

indexList = []
rectangleOrigin = [0]

K, N = map(int, inputFast().split())

area = [0 for _ in range(K+1)]
realArea = [0 for _ in range(K+1)]
result = [0 for _ in range(N)]

for _ in range(K):
    temp = list(map(int, inputFast().split()))
    rectangleOrigin.append(temp)

realArea[K] = (rectangleOrigin[K][2] - rectangleOrigin[K][0]) * (rectangleOrigin[K][3] - rectangleOrigin[K][1])

for j, k in itertools.product(range(rectangleOrigin[K][0], rectangleOrigin[K][2]+1), range(rectangleOrigin[K][1], rectangleOrigin[K][3]+1)):
    if [j, k] not in indexList:
        indexList.append([j, k])

for i in range(K-1, 0, -1):
    sumTemp = 0
    rectangle = rectangleOrigin[i]
    for j, k in itertools.product(range(rectangle[0], rectangle[2]), range(rectangle[1], rectangle[3])):
        if (([j, k] in indexList) & ([j+1, k+1] in indexList)):
            pass
        else:
            indexList.append([j, k])
            sumTemp = sumTemp + 1
    realArea[i] = sumTemp

    # 테두리 더하기
    for j, k in itertools.product(range(rectangle[2], rectangle[2]+1), range(rectangle[1], rectangle[3])):
        if ([j, k] not in indexList):
            indexList.append([j, k])
    for j, k in itertools.product(range(rectangle[0], rectangle[2]+1), range(rectangle[3], rectangle[3]+1)):
        if ([j, k] not in indexList):
            indexList.append([j, k])

area = sorted(realArea, reverse=True)

for i in range(N):
    result[i] = realArea.index(area[i])
    realArea[result[i]] = 0

result.sort()

print(*result[::1])


#
# for i in range(K, 0, -1):
#     rectangle1 = rectangle[i]
#     for j in range(i-1, 0, -1):
#         rectangle2 = rectangle[j]
#         if (rectangle1[x1] >= rectangle2[c]):
#             rowLength = 0
#         elif (rectangle1[x2] <= rectangle2[a]):
#             rowLength = 0
#         elif (rectangle1[x1] >= rectangle2[a]) & (rectangle1[x2] <= rectangle2[c]):
#             rowLength = rectangle1[x2] - rectangle1[x1]
#         elif (rectangle1[x1] >= rectangle2[a]) & (rectangle1[x2] >= rectangle2[c]):
#             rowLength = rectangle2[c] - rectangle1[x1]
#         elif (rectangle1[x1] <= rectangle2[a]) & (rectangle1[x2] <= rectangle2[c]):
#             rowLength = rectangle1[x2] - rectangle2[a]
#         elif (rectangle1[x1] <= rectangle2[a]) & (rectangle1[x2] >= rectangle2[c]):
#             rowLength = rectangle2[c] - rectangle2[a]
#         else:
#             pass
#
#         if (rectangle1[y1] >= rectangle2[d]):
#             colLength = 0
#         elif (rectangle1[y2] <= rectangle2[b]):
#             colLength = 0
#         elif (rectangle1[y1] >= rectangle2[b]) & (rectangle1[y2] <= rectangle2[d]):
#             colLength = rectangle1[y2] - rectangle1[y1]
#         elif (rectangle1[y1] >= rectangle2[b]) & (rectangle1[y2] >= rectangle2[d]):
#             colLength = rectangle2[d] - rectangle1[y1]
#         elif (rectangle1[y1] <= rectangle2[b]) & (rectangle1[y2] <= rectangle2[d]):
#             colLength = rectangle1[y2] - rectangle2[b]
#         elif (rectangle1[y1] <= rectangle2[b]) & (rectangle1[y2] >= rectangle2[d]):
#             colLength = rectangle2[d] - rectangle2[b]
#         else:
#             pass
#
#         area[j] += rowLength * colLength
#
#         print(i, j, rowLength * colLength, area)
#
# print("+++++++++++++")
#
# for i in range(K-1, 0, -1):
#     area[i] = area[i] - area[i+1]
#     realArea[i] = realArea[i] - area[i]
#     print(area)
#     print(realArea)

