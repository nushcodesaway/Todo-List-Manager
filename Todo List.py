todo=[]
print("1. Add task \n2. Delete Task \n3. Mark task complete")
l=input("Input Y:")
while l=="Y":
    ch= int(input("Enter choice:"))
    if ch==1:
        Task= input("Input task:")
        todo.append(Task)
    if ch==2:
        Task= input("Input task:")
        todo.remove(Task)
    if ch==3:
        Task= input("Input task:")
        index= todo.index(Task)
        todo[index]= Task+ " XXXX"
    l=input("Do you wanna continue?")
    if l=="N":
        print(todo)