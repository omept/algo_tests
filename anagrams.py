def anagram(firstText, secondText):
    sortedFirstText = sorted(str(firstText).lower().replace(" ", ""))
    sortedSecText = sorted(str(secondText).lower().replace(" ", ""))

    return sortedFirstText == sortedSecText

print("Program to check if two stings are anagrams. \n")
str1 = input("Enter first string : \n")
str2 = input("Enter second string : \n")

print("Anagram check : ", anagram(str1, str2))
