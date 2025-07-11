#Activity one

a,b,c=int(input("Enter a:")),int(input("Enter b:")),int(input("Enter c:"))
print(f"a:{a},b:{b},c:{c}")
a,b,c=b,c,a
print(f"a:{a},b:{b},c:{c}")

#Activity two
#Given a set of 3 student's examination marks (in the range from 0 to 100), 
#make a count of the number of students that have passed the exam. 
#A pass is awarded if the students mark is greater than or equal to 35.


def exam_pass(x,y,z):
    a=0
    if x>=35:
        a=a+1
    if y>=35:
        a=a+1
    if z>=35:
        a=a+1
    return a

St1=int(input("Enter marks of student1:"))
St2=int(input("Enter marks of student2:"))
St3=int(input("Enter marks of student3:"))
if 0<=St1<=100 and 0<=St2<=100 and 0<=St3<=100:
    result=exam_pass(St1,St2,St3)
    print("No. of students passed:",result)

#Activity three
#Design an algorithm that reads a list of 5 numbers (both +ve and -ve) and 
#makes a count of the number of negative and non-negative numbers in the list.
#Note-0 must be considered as a +ve number in this algorithm.


lst=list(map(int,input("Enter you list:").split()))
negative=0
positive=0
for i in list:
    if i<0:
        negative=negative+1
    if i>=0:
        positive=positive+1

print("Number of positive numbers:",positive)
print("Number of negative numbers:",negative)


#Activity four
#Design an algorithm that reads a number from the user and tells if it is even or odd or a zero.

num=int(input("Enter a number to check:"))
if num==0:
    print("num is zero")
elif num%2==0:
    print(f"num:{num} is even")
elif num%2!=0:
    print(f"num:{num} is odd")

#Activity five
#Given a set of 3 numbers, 
#design an algorithm that adds these numbers and returns the resultant sum

