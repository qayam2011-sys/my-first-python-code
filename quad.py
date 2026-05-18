import math    
print("enter the 3 coefficients of the quadratic equation ax^2 + bx + c = 0")
a = float(input("a: "))
b = float(input("b: "))     
c = float(input("c: "))
discriminant = math.pow(b,2) - 4*a*c
solution1=(-b+math.sqrt(discriminant))/2*a
solution2=(-b-math.sqrt(discriminant))/2*a
print(f"Solution 1: {solution1}")
print(f"Solution 2: {solution2}")
print(f"the discriminant is: {discriminant}")
if discriminant > 0:
    print("the equation has two real roots")
elif discriminant == 0:
    print("the equation has one real root")
else:
    print("the equation has no real roots")

    