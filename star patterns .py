"""
STAR PATTERN IN PYTHON
"""
n = int(input("Enter a number: "))
for i in range(n):
    for j in range(n):
        print("*", end="  ")
    print("")


""""""
RIGHT ANGLE TRIANGE PATTERN
"""

n = int(input("Enter a number: "))
for i in range(n):
    for j in range(i+1):
        print("*", end=" ")
    print("")

DECREASING TRIANGLE PATTERN
"""
n = 5
for i in range(n):
    for j in range(i,n):
        print("*", end=" ")
    print("")
n = 5
for i in range(n):
    for j in range(i,n):
        print(" ",end=" ")
    for j in range(i+1):
        print("*",end=" ")
    print("")

n = 5
for i in range(n):
    for i in range(i+1):
        print(" ", end=" ")
    for i in range(i,n):
        print("*", end=" ")
    print("")

n = 5
for i in range(n):
    for j in range(i,n):
        print(" ", end=" ")
    for j in range(i+1):
        print("*", end=" ")
    for j in range(i):
        print("*", end=" ")
    print("")


n = 5
for i in range(n):
    for j in range(i+1):
        print(" ", end=" ")
    for j in range(i,n):
        print("*", end=" ")
    for j in range(i,n-1):
        print("*", end=" ")
    print("")

n = 5
for i in range(n-1):
    for j in range(i,n):
        print(" ", end=" ")
    for j in range(i+1):
        print("*", end=" ")
    for j in range(i):
        print("*", end=" ")
    print("")

for i in range(n):
    for j in range(i+1):
        print(" ", end=" ")
    for j in range(i,n):
        print("*", end=" ")
    for j in range(i,n-1):
        print("*", end=" ")
    print("")
