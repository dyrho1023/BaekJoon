originalList = []

in1 = int(input())

originalList = list(map(int, input().split()))

originalList.sort()

timeSum = 0
for i in range(in1):
    timeSum = timeSum + originalList[i]*(in1 - i)

print(timeSum)



#
#
# def QuickSorting(start, end, unsortedList=[]):
#     if (start < end):
#         pivot = start
#         left = start + 1
#         right = end
#         while(left <= right):
#             while((unsortedList[pivot] >= unsortedList[left]) & (left < end)):
#                 left = left + 1
#
#             while((unsortedList[pivot] <= unsortedList[right]) & (right > start)):
#                 right = right - 1
#
#             if(left < right):
#                 temp = unsortedList[left]
#                 unsortedList[left] = unsortedList[right]
#                 unsortedList[right] = temp
#
#             else:
#                 temp = unsortedList[pivot]
#                 unsortedList[pivot] = unsortedList[right]
#                 unsortedList[right] = temp
#
#         QuickSorting(start, right - 1, unsortedList)
#         QuickSorting(right + 1, end, unsortedList)
#
#
# QuickSorting(0, in1-1, originalList)
