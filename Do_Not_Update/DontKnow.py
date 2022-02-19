
in1 = int(input())

def SumCheck(argIn1, argIn2):
    result = 0
    for i in range(argIn1, argIn2 + 1):
        result = result + i

    return result

def LocationCheck():
    for i in range (10):
        pass
# SumCheck(in1, in2)
# 1 ~ 1000 :   500500
# 1 ~ 2000 :  2001000
# 1 ~ 3000 :  4501500
# 1 ~ 4000 :  8002000
# 1 ~ 5000 : 12502500


if in1 == 1:
    pass
elif in1 <= 500500:
    for i in range(1, 1001):
        sumResultMin = SumCheck(1, i-1)
        sumResultMax = SumCheck(1, i)
        if (sumResultMin < in1) & (in1 <= sumResultMax):
            print(i)
            if i % 2 == 1:
                print("홀수")
            else:
                print("짝수")

elif in1 <= 2001000:
    for i in range(1, 2001):
        print(i)
elif in1 <= 4501500:
    for i in range(1, 3001):
        print(i)
elif in1 <= 8002000:
    for i in range(1, 4001):
        print(i)
else:
    for i in range(1, 5001):
        print(i)
