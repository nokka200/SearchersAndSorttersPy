# source https://en.wikipedia.org/wiki/Bubble_sort

def bubbleSort(listToSortA1: list, debugA2 = False, debugSplitA3 = "-")-> list:
    listLen = len(listToSortA1) - 1
    swap = True
    temp1Val = None

    while(swap):
        # set swap to false so we can end loop
        swap = False

        for item in range(listLen):
            if (listToSortA1[item] > listToSortA1[item + 1]):
                # if current value is greater than next swap them
                if(debugA2):
                    print("before swap")
                    print(f"list: {listToSortA1}")
                    print(f"listToSort[{item}]: {listToSortA1[item]}")
                    print(f"listToSort[{item + 1}]: {listToSortA1[item + 1]}")
                    print(20 * debugSplitA3)
                temp1Val = listToSortA1[item]
                listToSortA1[item] = listToSortA1[item + 1]
                listToSortA1[item + 1] = temp1Val
                if(debugA2):
                    print("after swap")
                    print(f"list: {listToSortA1}")
                    print(f"listToSort[{item}]: {listToSortA1[item]}")
                    print(f"listToSort[{item + 1}]: {listToSortA1[item + 1]}")
                swap = True
            if(debugA2):
                print("current values sorted")
                print(20 * debugSplitA3)

        listLen -= 1
        if (debugA2):
            print("listLen changed")
            print(20 * debugSplitA3)

    return listToSortA1


unsortedList = [2, 5, 1, 10, 3, 8, 20, -1, 4252, 400]
re = bubbleSort(unsortedList, True)
print(re)