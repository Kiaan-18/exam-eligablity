med=input("Do you have any medical conditions ? Y/N")
if med=="Y":
    print("You are allowed for exams")
else:
     per=int(input("Enter your attendence percentage:"))
     if per>=75:
          print("You are allowed")
     else:
        print("Not allowed")