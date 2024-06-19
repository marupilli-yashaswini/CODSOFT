def add(n1,n2):
    return n1+n2
def subtract(n1,n2):
    return n1-n2
def multiply(n1,n2):
    return n1*n2
def division(n1,n2):
    return n1/n2

print("welcome to calculator!!")
while True:
    print("\nselect operation:\n1.ADD\n2.SUBTRACT\n3.MULTIPLY\n4.DIVIDE\n5.EXIT\n");
    choice=int(input("enter your choice:"))
    if choice in (1,2,3,4):
        n1=float(input("enter your num1:"))
        n2=float(input("enter your num2:"))
        if choice==1:
            print("RESULT:",add(n1,n2))
        elif choice==2:
            print("RESULT:",subtract(n1,n2))
        elif choice==3:
            print("RESULT:",multiply(n1,n2))
        elif choice==4:
            print("RESULT:",division(n1,n2))
    elif choice==5:
        print("GOODBYE")
        break
    else:
        print("INVALID!!")
