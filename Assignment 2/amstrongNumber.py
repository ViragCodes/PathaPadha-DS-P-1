n = int(input("Enter number : "))

temp = n
sum  = 0

while temp > 0:
    sum += (temp % 10)**3  # adds up cube of each digit
    temp //= 10            # removes one by one from last 

if sum == n:
    print("Amstrong number")
else:
    print("Not Amstrong number")
