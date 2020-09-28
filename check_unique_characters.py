# Check if the characters of a sting are unique. ignore spaces.


def checkUnique(str):
    ss = str.replace(" ", "")
    return len(set(ss)) == len(ss)


print(checkUnique("qwertyuioplkjhgfdsazx  "))