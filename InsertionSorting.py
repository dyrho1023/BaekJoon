# originalList = []
#
# in1 = int(input())
#
# for _ in range(in1):
#     in2 = int(input())
#     originalList.append(in2)
originalList = [3, 7, 8, 1, 0, 9, 6, 10, 2, 4, 4, 2, 5]
print()
print(originalList, "\n")

in1 = len(originalList)

for j in range(in1-1):
    i = j
    while((originalList[i] > originalList[i+1]) & (0 <= i)):
        print(i)
        temp = originalList[i]
        originalList[i] = originalList[i+1]
        originalList[i+1] = temp
        i = i - 1

print("최종값 :", originalList)