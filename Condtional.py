stud1=int(input('Enter the feedback stud1 : '))
stud2=int(input('Enter the feedback stud2 : '))
stud3=int(input('Enter the feedback stud3 : '))
stud4=int(input('Enter the feedback stud4 : '))
stud5=int(input('Enter the feedback stud5 : '))

average = int((stud1+stud2+stud3+stud4+stud5)/5)
print(average)

if average>3:
    print('Average is good')
elif(average>3):
    print('Not bad')
elif(average>2):
    print('Average')
else:
    print('replace the faculty')