n = int(input("Enter number : "))
m = int(n**(1/2)) #checking only half of the factors to save Time

mark = True

for i in range(2, m + 1):
    if (n % i == 0):
        mark = False
        break

if mark == True:
    print("Prime")
else:
    print("Not prime")