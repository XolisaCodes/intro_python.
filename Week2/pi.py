pi = 0
accuracy = 100000

for i in range(0, accuracy):
    pi += ((4.0 * (-1)**i) / (2*i + 1))
pi = round(pi, 3)
radius = float(input("Enter your radius: "))
area = radius * radius * pi
area = round(area, 3)
print("Approximation of pi: ", pi, "Enter the Radius: ", radius, "Area: ",area,)
