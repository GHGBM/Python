 
#Assign an integer to a variable/location
a = 4

#Assign a string to a variable
name = 'Gary'

#Assign a float to a variable
realNumber = 2.56 

#Use the print function and .format() notation to print out the variable you 
#assigned
print('The integer value stored in a is: %d' % a)
print('The float value stored in realNumber is: %f' % realNumber)

#Use each of these operators +, - , * , / , +=, ­= , %
value = a*realNumber+a-realNumber/a
value += a
value = value % a

#Use of logical operators: and, or, not
b=True
c=False

d = b and not c or b
print(d)


#Use of conditional statements: if, elif, else
if b and c:
    print("b and c are true")
elif b or c:
    print("either b or c are true")
else:
    print("Neither of the two cases above resulted in true")


  
#Use of a while loop
i=0
while i < a:
    print(i)
    i += 1
#No esle statement, as there is no if statement

   
#Use of a for loop
for value in range(0, a):
    print(value)



#Create a list and iterate through that list using a for loop
#to print each item out on a new line
elements = ['carbon', 'oxygen', 'radium', 'einsteinium']
for element in elements:
    print(element)
    

#Create a tuple and iterate through it using a for loop to print each item out on a new line
#Tuple allows nesting in certain ways. An argument to a function.
fibs = (1,1,2,3,5,8)
for fib in fibs:
    print(fib)
    
    
#Define a function that returns a string variable
def getName():
    return name
    
#Call the function you defined above and print the result to the shell
print(getName())   