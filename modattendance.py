print("Welcome to Attendance Registry")
print("Total students = 4")
rollno = {1 : 'raj' , 2 : 'neha' , 3 : 'binod' , 4 : 'riya'}
print(rollno)
x = { 1 : 0 , 2 : 0, 3 :0, 4 : 0}
print("Enter the Roll numbers of those who are present then enter 0 ")
i = int(input())
if i ==1:
	x[1] = x[1] + 1
while i < 5:
	i = int(input())
	if i == 2:
		x[2] = x[2] + 1
	elif i == 3:
		x[3] = x[3] + 1
	elif i ==4:
		x[4] = x[4] + 1
if i >4:
	print("Invalid Roll number")
input =  input("Type name to know the no.of days present or press any key to exit: ")
if input == "raj":
	print(x[1])
elif input == "neha":
	print(x[2])
elif input == "binod":
	print(x[3])
elif input == "riya":
	print(x[4])
else:
	print('name doesnot exist')
	