"""
Given an array, print the most frequent occurring element
"""


def max_frequency(arr):
    maxCount = 0
    maxWord = None
    words = {}

    for val in arr:
        if val in words:
            words[val] += 1
        else:
            words[val] = 1

        if words[val] > maxCount:
            maxCount = words[val]
            maxWord = val

    return maxWord


print(max_frequency([1, 4, 5, 3, 4, 5, 6, 4]))
