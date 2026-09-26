search_name=input("enter student name")
found=False
with open("students.txt","r") as file:
    for line in file:
        name=line.strip()
        if name==search_name:
            found=True
            break
    if found:
        print("student found")
    else:
        print("student not found")