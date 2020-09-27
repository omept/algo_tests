"""
Check that array A is the reversed version of array B
"""


def isMirrow(arrA, arrB):
    mainLen = len(arrA)
    if len(arrB) != len(arrA):
        return False

    i = 0
    while i < mainLen:
        if arrA[i] != arrB[mainLen - 1 - i]:
            return False
        i = i + 1

    return True


print(isMirrow([1, 3, 6, 6], [5, 3, 1]))
print(isMirrow([], []))
print(isMirrow([34, 55, 90], [90, 55, 34]))
