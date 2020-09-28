"""
Return the common elements in two arrays. the two arrays can have different lengths. 
"""


def commonElements(arr1, arr2):
    arr1Size = len(arr1)
    arr2Size = len(arr2)
    maxSize = max(arr1Size, arr2Size)

    if arr1Size > arr2Size:
        maxArr = arr1
        compareTo = arr2
    else:
        maxArr = arr2
        compareTo = arr1

    if arr1Size == 0 or arr2Size == 0:
        return []

    i = 0
    commonElements = set()
    while i < maxSize:
        if maxArr[i] in compareTo:
            commonElements.add(maxArr[i])

        i = i + 1

    return list(commonElements)


print(commonElements([4, 5, 6, 5, 34, 2, 4], [2, 4]))
