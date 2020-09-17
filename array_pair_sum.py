"""
Array pair sum:
----------------

Given an integer array, output all the unique pairs that sum up to a specific value k.
So given the input: 
pair_sum([1,3,2,2], 4 )

would return two pairs:
(1,3)
(2,2)
"""

# begin pair sum


def pair_sum(arr, pairSum):
    seen = []
    pairBlocs = []
    if len(arr) < 2:
        print("Invalid array")
        return False

    for val in arr:
        val = int(val)
        target = pairSum - val

        if target in seen:
            pairBlocs.append((min(val, target), max(val, target)))
            seen.remove(target)
        else:
            seen.append(val)

    print("\nPair sum : ")

    if len(pairBlocs) > 0:
        print("\n".join(map(str, pairBlocs)))
        return True
    else:
        print("\nNo pair found")
        return False


# end pair sum function


inpArr = input("\nInsert comma separated values for array: \n").split(",")
inPairSum = int(input("\nInsert pair sum: \n"))
pair_sum(inpArr, inPairSum)
