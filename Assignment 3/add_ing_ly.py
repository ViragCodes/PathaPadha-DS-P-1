stg = input()
size = len(stg)

if size >= 3:
    if stg[-3:] == "ing":
        print(stg + "ly")
    else:
        print(stg + "ing")
else:
    print(stg)

'''Test Case ->
loving
lovingly

walk
walking
'''
