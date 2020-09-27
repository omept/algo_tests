def reverseArray(arr):
    # Write your code here
    arrLen = len(arr) - 1
    # print(arrLen)
    revList = []
    while arrLen >= 0:
        revList.append(arr[arrLen])
        arrLen = arrLen - 1

    return revList


print(reverseArray(["this", "3", "hello"]))
