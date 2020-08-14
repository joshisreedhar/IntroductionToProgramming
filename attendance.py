#1. record user attendance
studentNames=["alekya","amith","harsha","sreya","vyasa","sindhu","anirudh","pradhyumna","munna","manasa","spandana","sankarshana","sumana"]
n=0
totalstudentspresent=0
studentAttendance={}
for x in studentNames:
  n=n+1
  r=input(x+" ")
  if (r=="p"):
    studentAttendance[x]="p"
    totalstudentspresent=totalstudentspresent+1
  else:
    studentAttendance[x]="a"
print("total",n)
print("present",totalstudentspresent) 
print("absent",n-totalstudentspresent) 
    








#2. no of students in class








#3. no of presnt & absent students

