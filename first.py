#print("This is my first program")

stud1=int(input('Enter the feedback stud1 : '))
stud2=int(input('Enter the feedback stud2 : '))
stud3=int(input('Enter the feedback stud3 : '))
stud4=int(input('Enter the feedback stud4 : '))
stud5=int(input('Enter the feedback stud5 4: '))

average = int((stud1+stud2+stud3+stud4+stud5)/5)
print(average)

if average>2:
    print('Average is good')
    print('Good')


else:
    print('Average is not good')