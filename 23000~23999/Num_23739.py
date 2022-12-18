"""
문제
유체이탈을 할 줄 아는 지환이는 수업에 출석은 했으나 수업을 듣지 않았다.
늘 그랬듯이 시험기간은 찾아오는 법, 지환이는 이제야 공부를 시작했다.

N개의 챕터를 순서대로 공부해야 하는데, i번째 챕터를 공부하는 데 T_i분이 걸린다.
하지만 시간이 많지 않기 때문에 모두 볼 수는 없다. 어쩔 수 없이 벼락치기 공부법을 통해 F 학점만은 피하고자 한다.

벼락치기 공부법이란 30분간 공부한 후 휴식을 취하고 다시 30분 공부를 시작하는 방법이다.
한 챕터를 모두 공부하는 즉시 다음 챕터 공부를 시작한다.

이 공부법에 벼락치기라는 수식어가 붙은 이유는 한 가지 중요한 규칙이 더 있기 때문이다.
바로 30분의 공부시간이 끝나면 공부하던 챕터는 가차 없이 덮고 넘어가 버리는 것이다!

다행히 시험 전까지 벼락치기 공부법으로 N개의 챕터를 순서대로 공부할 수 있었다.
생각보다 쉽다고 생각한 지환이는 그대로 술을 마시러 갔다.

하지만 벼락치기 공부법의 한계일까?
안타깝게도 술을 마시고 나니 절반 이상 공부한 챕터를 제외하고 모두 머리에서 지워지고 말았다.
정신이 아득해진 지환이는 머리에 챕터가 몇 개 남았는지 세기 시작했다.

숙취에 힘들어하는 지환이를 도와 절반 이상 공부한 챕터의 개수를 구해주자.

입력
첫 번째 줄에 N이 주어진다. 0<N<101
두 번째 줄부터 N개의 줄에 정수 T_i가 순서대로 주어진다. 0<N<101

출력
지환이가 절반 이상 공부한 챕터의 개수를 출력한다.

"""

import sys

inputFast = sys.stdin.readline

in0 = int(inputFast())
in1 = []

for i in range(in0):
    temp = int(inputFast())
    in1.append(temp)

leftTime = 30
count = 0

for i in in1:
    nextLeftTime = leftTime - i

    if nextLeftTime < 0:
        if leftTime*2 >= i:
            count = count + 1
        else:
            pass
        leftTime = 30
    elif nextLeftTime == 0:
        count = count + 1
        leftTime = 30
    else:
        count = count + 1
        leftTime = nextLeftTime

print(count)
