"""
문제
자연수 N과 M이 주어졌을 때, 아래 조건을 만족하는 길이가 M인 수열을 모두 구하는 프로그램을 작성하시오.

1부터 N까지 자연수 중에서 M개를 고른 수열
같은 수를 여러 번 골라도 된다.

입력
첫째 줄에 자연수 N과 M이 주어진다. (1 ≤ M ≤ N ≤ 7)

출력
한 줄에 하나씩 문제의 조건을 만족하는 수열을 출력한다.
중복되는 수열을 여러 번 출력하면 안되며, 각 수열은 공백으로 구분해서 출력해야 한다.

수열은 사전 순으로 증가하는 순서로 출력해야 한다.
"""

import sys
import collections

inputFast = sys.stdin.readline

in0 = list(map(int, inputFast().split()))


def dfs(num, array, maxNum, maxLength):
    if num == maxLength:
        for i in range(1, maxNum+1):
            array[num] = i
            print(*array[1:])
    else:
        for i in range(1, maxNum+1):
            array[num] = i
            dfs(num+1, array, maxNum, maxLength)


result = [0 for i in range(in0[1]+1)]

dfs(1, result, in0[0], in0[1])


# print(result)
# print(check)
# print(stackList)