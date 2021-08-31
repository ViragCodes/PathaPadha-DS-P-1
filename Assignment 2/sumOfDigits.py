n = int(input("Enter value : "))

temp = n
sum  = 0

while temp > 0:
    sum += temp%10
    temp //= 10

print("Sum of Digits =", sum)