a = ["DATA","python","python","science","DATA","Machine Learning"]
append_values = []
for items in range(0, len(a)):
    index_a = 0
    a_value_pop = a.pop(index_a)
    if(a_value_pop) in a :
        append_values.append(a_value_pop)
    else:
        pass
    index_a += 1

print(append_values)