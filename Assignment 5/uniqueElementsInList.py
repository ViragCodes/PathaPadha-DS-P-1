def newList(lst):
    return [i for i in lst if lst.count(i) == 1]  # returns a list of elements occuring only once

l = [30, 40, 10, 60, 20, 50, 60, 10, 30]

new = newList(l) # calling the fuction
print(new)

''' OUTPUT ->
[40, 20, 50]
'''