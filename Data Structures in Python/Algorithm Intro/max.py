'''
	Code By : Sairaj Bhise
	Topic : Data Structure Introductions (Algorithms : Find biggest among 3)
	--------------------------------------------
	Example 2 : Algorithm for finding biggest among three.

	Step 1 : Start 
	Step 2 : Declare variables a,b and c.
	Step 3 : Read the values for a,b and c.
	Step 4 : If a > b
				If a > c
					print a is biggest
				else 
					Print c is biggest
			 Else 
			 	If b > c 
			 		Print b is biggest
			 	else 
					Print c is biggest.
	Step 5 : Stop

'''

a = int(input('Enter the value a ==>'))
b = int(input('Enter the value b ==>'))
c = int(input('Enter the value c ==>'))

if a > b :
	if a > c:
		print('a is biggest')
	else :
		print('c is biggest')
else :
	if b > c :
		print('b is biggest')
	else : 
		print('c is biggest')