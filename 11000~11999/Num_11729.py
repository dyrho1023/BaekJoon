"""
문제
세 개의 장대가 있고 첫 번째 장대에는 반경이 서로 다른 n개의 원판이 쌓여 있다.
각 원판은 반경이 큰 순서대로 쌓여있다. 이제 수도승들이 다음 규칙에 따라 첫 번째 장대에서 세 번째 장대로 옮기려 한다.

한 번에 한 개의 원판만을 다른 탑으로 옮길 수 있다.
쌓아 놓은 원판은 항상 위의 것이 아래의 것보다 작아야 한다.
이 작업을 수행하는데 필요한 이동 순서를 출력하는 프로그램을 작성하라. 단, 이동 횟수는 최소가 되어야 한다.

입력
첫째 줄에 첫 번째 장대에 쌓인 원판의 개수 N (1 ≤ N ≤ 20)이 주어진다.

출력
첫째 줄에 옮긴 횟수 K를 출력한다.

두 번째 줄부터 수행 과정을 출력한다.
두 번째 줄부터 K개의 줄에 걸쳐 두 정수 A B를 빈칸을 사이에 두고 출력하는데,
이는 A번째 탑의 가장 위에 있는 원판을 B번째 탑의 가장 위로 옮긴다는 뜻이다.

"""

import sys
import collections

inputFast = sys.stdin.readline

in0 = int(inputFast())
ring1 = collections.deque([i for i in range(in0, 0, -1)])
ring1.appendleft(100)
ring2 = collections.deque([100])
ring3 = collections.deque([100])
hanoi = [0]


num = 1
while(True):
    if num == 1:
        hanoi.append(1)
    elif num == in0+1:
        break
    else:
        temp = hanoi[num-1] + 2**(num-1)
        hanoi.append(temp)
    num += 1

print(hanoi[-1])

if in0 % 2 == 0:
    temp0 = ring1.pop()
    ring2.append(temp0)
    print(1, 2)
    temp0 = ring1.pop()
    ring3.append(temp0)
    print(1, 3)

    while(True):
        if ring1[-1] == 1:
            temp = ring1.pop()
            ring2.append(temp)
            print(1, 2)
            if ring1[-1] > ring3[-1]:
                temp = ring3.pop()
                ring1.append(temp)
                print(3, 1)
            elif ring1[-1] < ring3[-1]:
                temp = ring1.pop()
                ring3.append(temp)
                print(1, 3)

        elif ring2[-1] == 1:
            temp = ring2.pop()
            ring3.append(temp)
            print(2, 3)
            if ring1[-1] > ring2[-1]:
                temp = ring2.pop()
                ring1.append(temp)
                print(2, 1)
            elif ring1[-1] < ring2[-1]:
                temp = ring1.pop()
                ring2.append(temp)
                print(1, 2)

        elif ring3[-1] == 1:
            temp = ring3.pop()
            ring1.append(temp)
            print(3, 1)
            if ring2[-1] > ring3[-1]:
                temp = ring3.pop()
                ring2.append(temp)
                print(3, 2)
            elif ring2[-1] < ring3[-1]:
                temp = ring2.pop()
                ring3.append(temp)
                print(2, 3)

        if len(ring3) == in0+1:
            break

elif in0 == 1:
    print(1, 3)

elif in0 % 2 == 1:
    temp0 = ring1.pop()
    ring3.append(temp0)
    print(1, 3)
    temp0 = ring1.pop()
    ring2.append(temp0)
    print(1, 2)

    while(True):
        if ring1[-1] == 1:
            temp = ring1.pop()
            ring3.append(temp)
            print(1, 3)
            if ring1[-1] > ring2[-1]:
                temp = ring2.pop()
                ring1.append(temp)
                print(2, 1)
            elif ring1[-1] < ring2[-1]:
                temp = ring1.pop()
                ring2.append(temp)
                print(1, 2)

        elif ring2[-1] == 1:
            temp = ring2.pop()
            ring1.append(temp)
            print(2, 1)
            if ring2[-1] > ring3[-1]:
                temp = ring3.pop()
                ring2.append(temp)
                print(3, 2)
            elif ring2[-1] < ring3[-1]:
                temp = ring2.pop()
                ring3.append(temp)
                print(2, 3)

        elif ring3[-1] == 1:
            temp = ring3.pop()
            ring2.append(temp)
            print(3, 2)
            if ring1[-1] > ring3[-1]:
                temp = ring3.pop()
                ring1.append(temp)
                print(3, 1)
            elif ring1[-1] < ring3[-1]:
                temp = ring1.pop()
                ring3.append(temp)
                print(1, 3)

        if len(ring3) == in0+1:
            break







