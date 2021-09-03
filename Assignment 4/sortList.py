lst = [1,8,5,4,10,3,7,2,9,6]
size = len(lst)

# selection sort 
for i in range(size, 0, -1):
    for j in range(1, i):
        if lst[j-1] > lst[j]:
           lst[j-1], lst[j] = lst[j], lst[j-1] 
print(lst)

''' OUTPUT->
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
'''