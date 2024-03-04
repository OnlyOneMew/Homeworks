a = float(input("A side of a triangle: "))
b = float(input("B side of a triangle: "))
c = float(input("C side of a triangle: "))

s = (a + b + c) / 2
area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
perimeter = a + b + c

print("Triangle area is: ", area)
print("Triangle perimeter is: ", perimeter)
