# source https://en.wikipedia.org/wiki/Merge_sort
import math

def mergeSort(listToSortA1: list, debugA2 = True, debugSplitA3 = "-") -> list:
    if (len(listToSortA1) <= 1):
        # if lenght is less or equal to 1 return list.
        if (debugA2):
            print("list lenght <= 1 returning sorted list")
            print(20 * debugSplitA3)
        return listToSortA1

    # list variables
    leftHalf = []
    rightHalf = []
    listLen = len(listToSortA1)
    listMiddle = listLen / 2
    if(debugA2):
        print("before for loop")
        print(f"listlen: {listLen}")
        print(f"listMiddle: {listMiddle}")
        print(20 * debugSplitA3)

    for item in range(listLen):
        if(debugA2):
            print("inside loop")
            print(20 * debugSplitA3)

        if (item < listMiddle):
            leftHalf.append(listToSortA1[item])
            if(debugA2):
                print("item < listmiddle")
                print(f"appending: {listToSortA1[item]} to leftHalf")
                print(f"leftHalf: {leftHalf}")
                print(20 * debugSplitA3)

        else:
            rightHalf.append(listToSortA1[item])
            if(debugA2):
                print("item > listmiddle")
                print(f"appending: {listToSortA1[item]} to rightHalf")
                print(f"rightHalf: {rightHalf}")
                print(20 * debugSplitA3)

    leftHalf = mergeSort(leftHalf)
    rightHalf = mergeSort(rightHalf)

    return merge(leftHalf, rightHalf)

def merge(leftListA1: list, rightListA2: list, debugA3 = True, debugSplitA4 = "*"):
    sortedList = []
    if(debugA3):
        print("calling merge")
        print(20 * debugSplitA4)

    while( len(leftListA1) != 0 and len(rightListA2) != 0 ):
        if(debugA3):
            print("inside while")
            print(20 * debugSplitA4)
        if(leftListA1[0] <= rightListA2[0]):
            sortedList.append(leftListA1.pop(0))
            if (debugA3):
                print("leftListA1[0] <= rightListA2[0]")
                print(f"appending to sorted list: {sortedList}")
        else:
            sortedList.append(rightListA2.pop(0))
            if (debugA3):
                print("else")
                print(f"appending to sorted list: {sortedList}")

    while( len(leftListA1) != 0 ):
        sortedList.append(leftListA1.pop(0))
    while( len(rightListA2) != 0 ):
        sortedList.append(rightListA2.pop(0))

    return sortedList

unsortedList = [2, 1, 10, 5, -1, -100, 1002424, 87]
re = mergeSort(unsortedList)

print(re)