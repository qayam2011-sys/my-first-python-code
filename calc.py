def calculator(n1,op,n2):
    n1=n1.strip()
    n2=n2.strip()
    op=op.strip()
    try:
     n1=float(n1)
     n2=float(n2) 
    except ValueError:
        print("Error: Invalid input. Please enter valid numbers.")
    if op=='+':
        print(n1+n2)
    elif op=='-':
        print(n1-n2)
    elif op=='*':
        print(n1*n2)
    elif op=='/':
        if n2==0:
            print("Error: Division by zero")
        else:
            print(n1/n2)
    elif op=='%':
        if n2==0:
            print("Error: Division by zero")
        else:
            print(n1%n2)
    elif op=='**':
        print(n1**n2)        
    else:
        print("Invalid operator")
while True:
    n1=input("Enter first number:")
    op=input("Enter operator:")
    n2=input("Enter second number:")
    calculator(n1,op,n2)
    cont=input("Do you want to continue? (yes/no):")
    if cont.lower() != 'yes':
        break

