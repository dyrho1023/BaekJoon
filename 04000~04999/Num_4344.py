"""
문제
대학생 새내기들의 90%는 자신이 반에서 평균은 넘는다고 생각한다.
당신은 그들에게 슬픈 진실을 알려줘야 한다.

입력
첫째 줄에는 테스트 케이스의 개수 C가 주어진다.

둘째 줄부터 각 테스트 케이스마다 학생의 수 N(1 ≤ N ≤ 1000, N은 정수)이 첫 수로 주어지고,
이어서 N명의 점수가 주어진다. 점수는 0보다 크거나 같고, 100보다 작거나 같은 정수이다.

출력
각 케이스마다 한 줄씩 평균을 넘는 학생들의 비율을 반올림하여 소수점 셋째 자리까지 출력한다.
"""

import sys
import statistics

inputFast = sys.stdin.readline

in0 = int(inputFast())
in1 = []

for i in range(in0):
    temp = list(map(int, inputFast().split()))
    in1.append(temp)

for i in range(in0):
    count = 0
    student = in1[i][0]
    del in1[i][0]
    studentAvg = statistics.mean(in1[i])

    for j in range(student):
        if (in1[i][j] - studentAvg) > 0:
            count += 1
        else:
            pass

    print("{:.3f}%".format((count/student)*100))
