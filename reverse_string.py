"""
Reverse a string and return a list version of the reversed words. Ignore spaces. 

eg "This is a boy"  should retrun ["boy", "a", "is", "This"]

"""


def reverseWords(message):
    strLen = len(message)
    words = []
    revWords = []
    spaces = [" "]
    wdBuilder = ""
    i = 0

    # split the string into a list using space as a break point
    while i < strLen:
        if message[i] in spaces and len(wdBuilder) > 0:
            words.append(wdBuilder)
            wdBuilder = ""
        else:
            if message[i] not in spaces:
                wdBuilder = wdBuilder + message[i]

        i = i + 1

    if len(wdBuilder) > 0:
        words.append(wdBuilder)
        wdBuilder = ""

    # iterate through words and store its reversed
    wordsCount = len(words) - 1
    while wordsCount >= 0:
        revWords.append(words[wordsCount])
        wordsCount = wordsCount - 1

    return revWords


print(reverseWords("      "))
print(reverseWords("   Hello     my very good friend   "))