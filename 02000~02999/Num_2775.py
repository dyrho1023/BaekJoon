# def SumationZero(lastNum):
#     result = 0
#     for m in range(lastNum + 1):
#         result = result + m
#     return result
#
#
# def SumationFloor(sequence, lastNum):
#     result = 0
#     if sequence > 1:
#         for m in range(1, lastNum + 1):
#             result = result + SumationFloor(sequence - 1, m)
#     else:
#             result = SumationZero(lastNum)
#     return result
#
#
# k = []
# n = []
#
# in1 = int(input())
#
# for i in range(in1):
#     in2 = int(input())
#     in3 = int(input())
#     k.append(in2)
#     n.append(in3)
#
# for i in range(in1):
#     if k[i] == 1:
#         person = SumationZero(n[i])
#         print(person)
#     else:
#         person = SumationFloor(k[i], n[i])
#         print(person)

k = []
n = []

in1 = int(input())

for i in range(in1):
    in2 = int(input())
    in3 = int(input())
    k.append(in2)
    n.append(in3)

for i in range(in1):
    valueList = [[0 for col in range(n[i])] for row in range(k[i]+1)]
    for j in range(n[i]):
        valueList[0][j] = j + 1

    if k[i] >= 1:
        for l in range(1, k[i]+1):
            valueList[l][0] = 1
            for m in range(n[i]):
                tempSum = 0
                for o in range(m+1):
                    tempSum = tempSum + valueList[l-1][o]
                valueList[l][m] = tempSum
    else:
        pass
    print(valueList[k[i]][n[i]-1])
    #print(valueList)


