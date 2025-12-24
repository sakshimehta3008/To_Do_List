tasks=[]

while True:
    print("Enter 1 to ADD tasks.")
    print("Enter 2 to DELETE tasks.")
    print("Enter 3 to VIEW tasks.")
    print("Enter 4 to EXIT")

    choice=int(input("Enter your choice: "))
    if(choice==1):
        task=input("Enter task: ")
        tasks.append(task)
        print("Task added succesfully.")
    
    elif(choice==2):
        tasks.pop()
        print("Last task succesfully deleted")

    elif(choice==3):
        print(tasks)
    
    elif(choice==4):
        print("Hurray! No tasks.")
    
    else:
        print("Enter a valid choice!")