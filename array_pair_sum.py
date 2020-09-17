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

seen = []
pairBlocs = []

print("Insert comma separated values for array: \n")
arr = input().split(",")


print("Insert pair sum: \n")
pairSum = int(input("Insert pair sum: \n"))


if len(arr) < 2:
    print("Invalid array")
    exit()

for val in arr:
    val = int(val)
    target = pairSum - val

    if target in seen:
        pairBlocs.append((min(val, target), max(val, target)))
        seen.remove(target)
    else:
        seen.append(val)

if len(pairBlocs) > 0:
    print("\n".join(map(pair, pairBlocs)))
    exit()
else:
    print("No pair found")
    exit()