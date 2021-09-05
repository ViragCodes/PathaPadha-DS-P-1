def sum(lst):
    rv = 0
    for i in lst:
        rv += i
    print(rv)

l = [30, 40, 10, 60, 20, 50]

sum(l)   # calling the function and passing l as argument

''' OUTPUT ->
210
'''