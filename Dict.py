sum=0
###defining the list of dictionary for students
students=[]
userFlag="Y"
##they are connected through index
##

while(userFlag=="Y"):
    ##creating a dictionary for a new student
    student={}
    name=input("Enter the name of the student")
    student["name"]=name
    feedback=int(input("Enter the feedback of the student one by one"))
    feedbackAvailable=input("Do you want to provide feedback? Enter Y or N")
 #   if(feedbackAvailable=="Y"):
  #      feedback=int(input("Enter the feedback of the student one by one"))
    student["feedback"]=feedback
    userFlag=input("Do you want to continue? Enter Y or N")
    ##adding the student to the list of students
    print(student)
    students.append(student)
    sum=sum+feedback
print(students)
average=sum/len(students)

for student in students:
    if student['name'] == search_name:
    print(f"The feedback of {student['name']} is {student['feedback']}")
