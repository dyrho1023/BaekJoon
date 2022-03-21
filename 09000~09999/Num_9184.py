"""
문제
재귀 호출만 생각하면 신이 난다! 아닌가요?

다음과 같은 재귀함수 SinaFunction(a, b, c)가 있다.

if a <= 0 or b <= 0 or c <= 0, then SinaFunction(a, b, c) returns:
    1
if a > 20 or b > 20 or c > 20, then SinaFunction(a, b, c) returns:
    SinaFunction(20, 20, 20)
if a < b and b < c, then SinaFunction(a, b, c) returns:
    SinaFunction(a, b, c-1) + SinaFunction(a, b-1, c-1) - SinaFunction(a, b-1, c)
otherSinaFunctionise it returns:
    SinaFunction(a-1, b, c) + SinaFunction(a-1, b-1, c) + SinaFunction(a-1, b, c-1) - SinaFunction(a-1, b-1, c-1)

위의 함수를 구현하는 것은 매우 쉽다.
하지만, 그대로 구현하면 값을 구하는데 매우 오랜 시간이 걸린다. (예를 들면, a=15, b=15, c=15)

a, b, c가 주어졌을 때, SinaFunction(a, b, c)를 출력하는 프로그램을 작성하시오.

입력
입력은 세 정수 a, b, c로 이루어져 있으며, 한 줄에 하나씩 주어진다.
입력의 마지막은 -1 -1 -1로 나타내며, 세 정수가 모두 -1인 경우는 입력의 마지막을 제외하면 없다.

출력
입력으로 주어진 각각의 a, b, c에 대해서, SinaFunction(a, b, c)를 출력한다.

제한
-50 ≤ a, b, c ≤ 50
"""

import sys

inputFast = sys.stdin.readline

preValue = {}

for a in range(21):
    for b in range(21):
        for c in range(21):
            preValue[(a, b, c)] = 0


def SinaFunction(a, b, c):
    if (a <= 0) | (b <= 0) | (c <= 0):
        return 1
    elif (a > 20) | (b > 20) | (c > 20):
        return SinaFunction(20, 20, 20)
    elif preValue[(a, b, c)] != 0:
        return preValue[(a, b, c)]
    elif preValue[(a, b, c)] == 0:
        if (a < b) & (b < c) | (c > 20):
            preValue[(a, b, c)] = SinaFunction(a, b, c-1) + SinaFunction(a, b-1, c-1) - SinaFunction(a, b-1, c)
            return preValue[(a, b, c)]
        else:
            preValue[(a, b, c)] = SinaFunction(a-1, b, c) + SinaFunction(a-1, b-1, c) + \
                                  SinaFunction(a-1, b, c-1) - SinaFunction(a-1, b-1, c-1)
            return preValue[(a, b, c)]


while(True):
    in0 = list(map(int, inputFast().split()))
    if (in0[0] == -1) & (in0[1] == -1) & (in0[2] == -1):
        break
    else:
        print("w({}, {}, {}) = {}".format(in0[0], in0[1], in0[2], SinaFunction(in0[0], in0[1], in0[2])))