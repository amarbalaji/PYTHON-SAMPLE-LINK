"""a = ["DATA","python","python","science","DATA","Machine Learning"]
append_values = []
for items in range(0, len(a)):
    index_a = 0
    a_value_pop = a.pop(index_a)
    if(a_value_pop) in a :
        append_values.append(a_value_pop)
    else:
        pass
    index_a += 1

print(append_values)"""
"""print(chr(65))
print(chr(90))"""
"""n= 65
for i in range(0,6):
    for j in range(0,i+1):
        print(chr(n))
"""
"""
STAR PATTERN IN PYTHON
"""
"""n = int(input("Enter a number: "))
for i in range(n):
    for j in range(n):
        print("*", end="  ")
    print("")


""""""
RIGHT ANGLE TRIANGE PATTERN"""

"""n = int(input("Enter a number: "))
for i in range(n):
    for j in range(i+1):
        print("*", end=" ")
    print("")"""

"""
DECREASING TRIANGLE PATTERN
"""
"""n = 5
for i in range(n):
    for j in range(i,n):
        print("*", end=" ")
    print("")"""
"""n = 5
for i in range(n):
    for j in range(i,n):
        print(" ",end=" ")
    for j in range(i+1):
        print("*",end=" ")
    print("")"""

"""n = 5
for i in range(n):
    for i in range(i+1):
        print(" ", end=" ")
    for i in range(i,n):
        print("*", end=" ")
    print("")"""

"""n = 5
for i in range(n):
    for j in range(i,n):
        print(" ", end=" ")
    for j in range(i+1):
        print("*", end=" ")
    for j in range(i):
        print("*", end=" ")
    print("")
"""

"""n = 5
for i in range(n):
    for j in range(i+1):
        print(" ", end=" ")
    for j in range(i,n):
        print("*", end=" ")
    for j in range(i,n-1):
        print("*", end=" ")
    print("")"""

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


"""by amar"""