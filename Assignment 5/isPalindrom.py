def removeSpaceAndCase(stg):
    s1 = stg.lower()          # normalizing upper and lower case
    s2 = s1.replace(" ", "")  # removing spaces
    return s2

def check(stg):
    if stg == stg[::-1]:
        return True
    return False

string = input()
val = check(removeSpaceAndCase(string)) 

if val == True:
    print("Palindrom!")
else:
    print("Not a Palindrom!")

''' TEST CASES ->
_!101!_
Palindrom!

Virag Jain
Not a Palindrom!

Was it a Car or a Cat I saw
Palindrom!
'''


