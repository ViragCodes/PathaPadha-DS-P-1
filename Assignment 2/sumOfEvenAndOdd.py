soe = 0; #sum of even
soo = 0; #sum of odd

for i in range(20,31):
    if i%2 == 0:
        soe += i
    else:
        soo += i
print("Sum of even numbers =", soe)
print("Sum of odd numbers  =", soo)