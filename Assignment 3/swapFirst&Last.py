stg = input()
first = stg[0]              #extracts first character
last  = stg[len(stg)-1]     #extracts last  character

ans = last + stg[1:len(stg)-1] + first
print(ans)

'''Test Case ->
HELLO
OELLH
'''