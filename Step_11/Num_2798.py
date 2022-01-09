"""
문제
...

한국 최고의 블랙잭 고수 김정인은 새로운 블랙잭 규칙을 만들어 상근, 창영이와 게임하려고 한다.
김정인 버전의 블랙잭에서 각 카드에는 양의 정수가 쓰여 있다.
그 다음, 딜러는 N장의 카드를 모두 숫자가 보이도록 바닥에 놓는다.
그런 후에 딜러는 숫자 M을 크게 외친다.

이제 플레이어는 제한된 시간 안에 N장의 카드 중에서 3장의 카드를 골라야 한다. :w
블랙잭 변형 게임이기 때문에, 플레이어가 고른 카드의 합은 M을 넘지 않으면서 M과 최대한 가깝게 만들어야 한다.

N장의 카드에 써져 있는 숫자가 주어졌을 때,
M을 넘지 않으면서 M에 최대한 가까운 카드 3장의 합을 구해 출력하시오.


입력
첫째 줄에 카드의 개수 N(3 ≤ N ≤ 100)과 M(10 ≤ M ≤ 300,000)이 주어진다.
둘째 줄에는 카드에 쓰여 있는 수가 주어지며, 이 값은 100,000을 넘지 않는 양의 정수이다.
합이 M을 넘지 않는 카드 3장을 찾을 수 있는 경우만 입력으로 주어진다.


출력
첫째 줄에 M을 넘지 않으면서 M에 최대한 가까운 카드 3장의 합을 출력한다.
"""

# cardCount, targetNum = [10, 500]
# inList2 = [93, 181, 245, 214, 315, 36, 185, 138, 216, 295]
#
# print(cardCount, targetNum)
# inList2.sort()
#
# print(inList2)

inList1 = list(map(int, input().split()))
inList2 = list(map(int, input().split()))

cardCount = inList1[0]
targetNum = inList1[1]

breaker = False
maxValue = 0
for i in range(cardCount-1, 1, -1):
    for j in range(i-1, 0, -1):
        for k in range(j-1, -1, -1):
            overallSum = inList2[i] + inList2[j] + inList2[k]
            if overallSum > targetNum:
                pass
            else:
                if overallSum > maxValue:
                    maxValue = overallSum
                else:
                    pass

print(maxValue)






