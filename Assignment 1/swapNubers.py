num1, num2 = input("Enter first number  : "), input("Enter second number : ")

#swapping values with help of another variable
temp = num1
num1 = num2
num2 = temp

print("Values after swapping       : a =", num1, " b =", num2)

#swapping values without using another variable
num1, num2 = num2, num1

print("Values after swapping again : a =", num1, " b =", num2)

'''OUTPUT ->
Enter first number  : 1
Enter second number : 8
Values after swapping       : a = 8  b = 1
Values after swapping again : a = 1  b = 8
'''