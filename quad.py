import math
import cmath
def quadratic_equation_solver(a, b, c):
    if a == 0:
        print("Error: 'a' cannot be zero. This is not a quadratic equation.")
        return

    discriminant = b**2 - 4*a*c
    
    print(f"Discriminant (D) = {discriminant}")
    
    if discriminant > 0:
        # Two real and distinct roots
        root1 = (-b + cmath.sqrt(discriminant)) / (2 * a)
        root2 = (-b - cmath.sqrt(discriminant)) / (2 * a)
        print(f"Solution 1: {root1:.4f}")
        print(f"Solution 2: {root2:.4f}")
        print("The equation has two real and distinct roots.")
        
    elif discriminant == 0:
        # One real root (repeated)
        root = -b / (2 * a)
        print(f"Solution: {root:.4f}")
        print("The equation has one real root (repeated).")
        
    else:
        # No real roots (complex roots)
         root1 = (-b + cmath.sqrt(discriminant)) / (2 * a)
         root2 = (-b - cmath.sqrt(discriminant)) / (2 * a)
         print(f"Solution 1: {root1:.4f}")
         print(f"Solution 2: {root2:.4f}")
         print("The equation has no real roots (Complex roots).")
if __name__ == "__main__":
    print("=== Quadratic Equation Solver (with Complex Roots) ===\n")
    
    try:
        a = float(input("Enter coefficient a: "))
        b = float(input("Enter coefficient b: "))
        c = float(input("Enter coefficient c: "))
        
        quadratic_equation_solver(a, b, c)
        
    except ValueError:
        print("Error: Please enter valid numbers!")