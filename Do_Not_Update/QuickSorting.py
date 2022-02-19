# originalList = []
#
# in1 = int(input())
#
# for _ in range(in1):
#     in2 = int(input())
#     originalList.append(in2)
originalList = [3, 7, 8, 1, 5, 9, 6, 10, 2, 4, 4, 2, 0]
print()
print(originalList, "\n")


def QuickSorting(start, end, unsortedList=[]):
    if (start < end):
        pivot = start
        left = start + 1
        right = end
        while(left <= right):
            while((unsortedList[pivot] >= unsortedList[left]) & (left < end)):
                left = left + 1

            while((unsortedList[pivot] <= unsortedList[right]) & (right > start)):
                right = right - 1

            if(left < right):
                temp = unsortedList[left]
                unsortedList[left] = unsortedList[right]
                unsortedList[right] = temp

            else:
                print("\npivot 바꾸는 구간 : ", unsortedList[pivot], unsortedList[right])
                temp = unsortedList[pivot]
                unsortedList[pivot] = unsortedList[right]
                unsortedList[right] = temp

        print()
        print(unsortedList, left, right, "\n")

        QuickSorting(start, right - 1, unsortedList)
        QuickSorting(right + 1, end, unsortedList)


in1 = len(originalList)
QuickSorting(0, in1-1, originalList)

print("최종값 :",originalList)