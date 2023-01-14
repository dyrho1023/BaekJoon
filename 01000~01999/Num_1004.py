"""
문제
어린 왕자는 소혹성 B-664에서 자신이 사랑하는 한 송이 장미를 위해 살아간다.
어느 날 장미가 위험에 빠지게 된 것을 알게 된 어린 왕자는, 장미를 구하기 위해 은하수를 따라 긴 여행을 하기 시작했다.
하지만 어린 왕자의 우주선은 그렇게 좋지 않아서 행성계 간의 이동을 최대한 피해서 여행해야 한다.
아래의 그림은 어린 왕자가 펼쳐본 은하수 지도의 일부이다.

빨간 실선은 어린 왕자가 출발점에서 도착점까지 도달하는데 있어서 필요한 행성계 진입/이탈 횟수를 최소화하는 경로이며,
원은 행성계의 경계를 의미한다. 이러한 경로는 여러 개 존재할 수 있지만 적어도 3번의 행성계 진입/이탈이 필요하다는 것을 알 수 있다.

위와 같은 은하수 지도, 출발점, 도착점이 주어졌을 때
어린 왕자에게 필요한 최소의 행성계 진입/이탈 횟수를 구하는 프로그램을 작성해 보자.
행성계의 경계가 맞닿거나 서로 교차하는 경우는 없다.
또한, 출발점이나 도착점이 행성계 경계에 걸쳐진 경우 역시 입력으로 주어지지 않는다.

입력
입력의 첫 줄에는 테스트 케이스의 개수 T가 주어진다.
그 다음 줄부터 각각의 테스트케이스에 대해 첫째 줄에 출발점 (x1, y1)과 도착점 (x2, y2)이 주어진다.
두 번째 줄에는 행성계의 개수 n이 주어지며, 세 번째 줄부터 n줄에 걸쳐 행성계의 중점과 반지름 (cx, cy, r)이 주어진다.

출력
각 테스트 케이스에 대해 어린 왕자가 거쳐야 할 최소의 행성계 진입/이탈 횟수를 출력한다.
"""

import sys

inputFast = sys.stdin.readline

in0 = int(inputFast())
result = []

for _ in range(in0):
    in1 = list(map(int, inputFast().split()))
    in2 = int(inputFast())
    in3 = []
    check = 0
    for i in range(in2):
        in3 = list(map(int, inputFast().split()))

        flagStart = 0
        flagDefinition = 0

        if ((in1[0]-in3[0])**2 + (in1[1]-in3[1])**2) < in3[2]**2:
            check = check + 1
            flagStart = 1

        if ((in1[2]-in3[0])**2 + (in1[3]-in3[1])**2) < in3[2]**2:
            check = check + 1
            flagDefinition = 1

        if (flagStart == 1) & (flagDefinition == 1):
            check = check - 2


    result.append(check)

print(*result, sep ='\n')