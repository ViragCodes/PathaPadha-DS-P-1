x1, y1 = input("Enter first coordinates  :").split()  
x2, y2 = input("Enter second coordinates :").split()

x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)   # converts str to int

distance = ((x2-x1)**2 + (y2-y1)**2)**(1/2)

print("\nDistance =", distance)

'''OUTPUT ->
Enter first coordinates  :3 4
Enter second coordinates :0 0

Distance = 5.0
'''