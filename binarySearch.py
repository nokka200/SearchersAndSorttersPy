import math

# source https://en.wikipedia.org/wiki/Binary_search_algorithm

def binarySearch(sortedListA1: list, targetA2: any, debugA3 = False, debugSpplitA4 = "-") -> bool:
    listStart = 0                                       # start of the list
    listEnd = len(sortedListA1) - 1                     # end of the list using 0 based indexing
    listMiddle = math.floor((listStart + listEnd) / 2)  # list middle

    if (debugA3):
        print("before loop")
        print(f"listStart: {listStart}")
        print(f"listEnd: {listEnd}")
        print(f"listMiddle: {listMiddle}")
        print(f"listMiddleValue: {sortedListA1[listMiddle]}")
        print(20 * debugSpplitA4)

    while listStart <= listEnd:
        listMiddle = math.floor((listStart + listEnd) / 2)
        if(debugA3):
            print("loop start")
            print(f"listMiddleIndex: {listMiddle}")
            print(f"listMiddleValue: {sortedListA1[listMiddle]}")
            print(20 * debugSpplitA4)

        if (sortedListA1[listMiddle] < targetA2):
            # if middle value is less than target, change start to next of middle.
            listStart = listMiddle + 1
            if(debugA3):
                print("target less than current middle value")
                print(f"new listStartIndex: {listMiddle}")
                print(20 * debugSpplitA4)
        elif(sortedListA1[listMiddle] > targetA2):
            # if middle value is greater than target, change end to before middle.
            listEnd = listMiddle - 1
            if(debugA3):
                print("target greater than current middle value")
                print(f"new listEndIndex: {listEnd}")
                print(20 * debugSpplitA4)
        else:
            if(debugA3):
                print("target found")
                print(20 * debugSpplitA4)
            return True
    
    return False



targetList = [10, 20, 21, 22, 30, 45, 46, 50]
targetValue = 50


re = binarySearch(targetList, targetValue, True)

print(re)