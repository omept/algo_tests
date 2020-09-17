# start anagram function
def anagram(firstText, secondText):
    s1 = str(firstText).lower().replace(" ", "")
    s2 = str(secondText).lower().replace(" ", "")

    count = {}

    # count the number of character occurances in s1
    for cht in s1:
        if cht in count:
            count[cht]  += 1
        else:
            count[cht] = 1

    # reverse the character occurances while comparing with s2
    for cht2 in s2:
        if cht2 in count:
            count[cht2] -=1
        else:
            count[cht2] = 1

    # all character count must be zero in count dictionary else the anagram equality is false.

    for k in count:
        if count[k] > 0:
            return False

    return True

# end anagram function



print("Program to check if two stings are anagrams. \n")
str1 = input("Enter first string : \n")
str2 = input("Enter second string : \n")

print("Anagram check : ", anagram(str1, str2))
