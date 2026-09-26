name=input("enter student name:")
with open("students.txt","a")as file:
    file.write(name+"\n")
    print("student added")
