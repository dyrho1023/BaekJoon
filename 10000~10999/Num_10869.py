"""
문제
두 자연수 A와 B가 주어진다. 이때, A+B, A-B, A*B, A/B(몫), A%B(나머지)를 출력하는 프로그램을 작성하시오.

입력
두 자연수 A와 B가 주어진다. (1 ≤ A, B ≤ 10,000)

출력
첫째 줄에 A+B, 둘째 줄에 A-B, 셋째 줄에 A*B, 넷째 줄에 A/B, 다섯째 줄에 A%B를 출력한다.
"""

in1 = list(map(int, input().split()))

out1 = in1[0] + in1[1]
out2 = in1[0] - in1[1]
out3 = in1[0] * in1[1]
out4 = in1[0] // in1[1]
out5 = in1[0] % in1[1]


print(out1)
print(out2)
print(out3)
print(out4)
print(out5)
