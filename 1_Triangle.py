# To find the type of the triangle using its side length

a = float(input("Enter the side: "))
b = float(input("Enter the side: "))
c = float(input("Enter the side: "))

if (a == b) and (b == c) and (c == a):
    print("Equilateral Triangle")
elif (a == b) or (b == c) or (c == a):
    print("Issoceles Triangle")
elif (a*a + b*b == c*c) or (b*b + c*c == a*a) or (c*c + a*a == b*b):
    print("Right Angled Triangle")
else:
    print("Scalen Triangle")
    