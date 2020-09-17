import sys

n = 20
data = []
for numbr in range(20):
    a = len(data)
    b = sys.getsizeof(data)
    resp =  "Length: {0:3d} Size in bytes {1:4d}"
    print(resp.format(a,b))
    data.append(numbr)
