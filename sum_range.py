rangeMax = int(input("Enter the max number to sum from zero : \n"))
numSum = 0

for num in range(0, (rangeMax + 1)):
    numSum += num


print("Total sum of numbers from 0 to ", rangeMax, " is ", numSum)
