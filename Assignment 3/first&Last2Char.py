stg = input()
size = len(stg)
if (size >= 2) :
    first2char = stg[0 : 2]
    last2char  = stg[-2:]
    ans = first2char + last2char
    print(ans)
else :
    print("empty string")

'''Test Case ->
HA
HAHA
'''