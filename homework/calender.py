#A code to check whether a date exists or not in a calender year
year = int(input('Enter year: '))
months = ('January' , 'February' , 'March' , 'April' , 'May'  , 'June' , 'July' , 'August' , 'September' , 'October' , 'November' , 'December' )
print("Mention month name")
m = input("Enter month: ")
month = m.title()
if month not in months:
	print("The month you entered does not exist in calender")
else:
	date = int(input("Enter the date: "))
	a = ('January' , 'March' , 'May' , 'July' , 'August' , 'October' , 'December')
	b = ('April' , 'June' , 'September' , 'November')
	c = ('February')
	if month in a and date <= 31:
		print("The date you mentioned is present in calender year and it is " ,  date , '/', month , '/' , year)
	elif month in b and date <=30:
		print("The date you mentioned is present in calender year and it is " ,  date , '/', month , '/' , year)
	elif month in c and year%4 == 0 and date <=29:
		print("The date you mentioned is present in this calender year and it is " ,  date , '/', month , '/' , year)
	elif month in c and year%4 != 0 and date <=28:
		print("The date you mentioned is present in this calender year and it is " ,  date , '/', month , '/' , year)
	else:
		print("The date you entered is not in the month you mentioned")