"""
문제
양수 A가 N의 진짜 약수가 되려면, N이 A의 배수이고, A가 1과 N이 아니어야 한다.
어떤 수 N의 진짜 약수가 모두 주어질 때, N을 구하는 프로그램을 작성하시오.

입력
첫째 줄에 N의 진짜 약수의 개수가 주어진다.
이 개수는 50보다 작거나 같은 자연수이다.
둘째 줄에는 N의 진짜 약수가 주어진다.
1,000,000보다 작거나 같고, 2보다 크거나 같은 자연수이고, 중복되지 않는다.

출력
첫째 줄에 N을 출력한다. N은 항상 32비트 부호있는 정수로 표현할 수 있다.
"""

import sys

inputFast = sys.stdin.readline

in0 = list(map(int, inputFast().split()))
in1 = list(map(int, inputFast().split()))


def BinaryBoundSearch(targetList, targetValue, start, end):
    upperIndex = UpperBoundarySearch(targetList, targetValue, start, end)
    return upperIndex


def UpperBoundarySearch(targetList, targetValue, start, end):
    while(True):
        mid = (start + end) // 2
        tree = 0
        for i in in1:
            if i > mid:
                tree += (i-mid)
            else:
                tree = tree
        # print(tree, start, mid, end, targetValue)
        if tree >= targetValue:
            start = mid + 1
        elif tree < targetValue:
            end = mid

        if (start >= end):
            return start -1


start = 0
end = 1000000000
targetValue = in0[1]

result = BinaryBoundSearch(in1, targetValue, start, end)

print(result)
