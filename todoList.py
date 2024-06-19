List=[]
def display():
    for i in List:
        print(i)
def add():
    item=input("enter the task:")
    List.append(item)
def remove():
    num=int(input("enter the number of the task which is to be removed:"))
    if (num>0 and num<=len(List)):
        item=List.pop(num-1)
    print(f"{item} is removed from the to-do list")

while True:
    print("\nWhat would you like to do?\n1.Display to-do list\n2.Add a task\n3.Remove a task\n4.Quit")
    choice=int(input("enter your choice:"))
    if choice==1:
        display()
    if choice==2:
        add()
    if choice==3:
        remove()
    if choice==4:
        print("GOODBYE")
        break
    if choice not in [1,2,3,4]:
        print("\n INVALID CHOICE \n please try again!")
