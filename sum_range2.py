try:
    num = int(input("Enter number to sum up to: \n"))
    sol = int(( num * (num +1 ) )/2)
    print("sum of numbers from 0 to ", num, " is ", sol)
except ValueError:
    print("Invalid Number")
except:
    print("Error Occured")
