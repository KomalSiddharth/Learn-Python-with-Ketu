# print methods in python
print("hello everyone!")  #it's just one complete string
print("hello","everyone") #here there's two different string separated by a space(comma create a automatic space)
print("i m roll no 68")  # here integer enclosed with double quotes wppuld be considered string itself
print(68) #here it idicated the integer

# Mathematical operations
print(6+8) #addition operator
print(6-8) #subtraction operator
print(6*8) #multiplication operator
print(6/8) #division operator
print(21%2) #remainder operator
print(22//3) #quotient->rounded down
print( 4**4) #raising to power

# Cheatcode to remember the order of operators
# <------PLEASE EXCUSE MY DEAR AUNT SALLY----------->
# Parentheses > exponential > multiplication > division > Addition > Subtraction 

# how to use multiple operations in one liner
print("Funds to be send are: ", 200*5 + 600/3+ 758-637)
print(30/9) # all decimal values are provided
print(30//9) #whereas here the value is rounded down 

# Now let's learn about the variables
# variable name= value (where variable name must be lowercase,no numbers and no special characters)
Months=10
print("I've been working here for ",Months,"months")

# Now let's learn about the assignment operator
years=2
years=5
print(years) 
#now u might be thinking why 5 not 2 coz python uses top to bottom approach where once a value is intialized and then upadted so it will provide the updated value as an outcome
# Example -> Code to calculate the passengers fare
base_fare=200
num_of_bags=2
base_fare=150 #here the values have been changed
total=base_fare*(num_of_bags*0.75)
print(total)

# Now let's explore the input function
# input function basically let's us take an input from the user
name=input("Enter your name: ")
city=input("Enter your city: ")
print("My name is ",name,"and i m from ",city)

extra=input("price of add-ons: ")
extra=int(extra)
total=100+extra
print(total)

# Now let's explore nesting functions
# nesting means putting code within another code to make the quesries appear shorter
# it reduces the no of lines within the code
# here first the user provides the string as an inpuand then converted into integer to make ir machine readablet 
height=input("enter the height: ")
height=int(height)
# theses directly performs the same steps in one liner
height=int(input("enter the height: "))

# example on nesting-> finding the sum of input length based on the numbers of letter
lenght1=len(input("enter your 1st word: "))
length2=len(input("enter your 2nd word: "))
total=lenght1+length2
print("The total length is" ,total)

# single line commments are presenred by #
# multi line comments are presented bu ''' ........'''
# commments are non executable code and are often ignored while programming

# CONDITIONAL OPERATORS
# if something is true do this else do this instead
available_tickets=int(input("Enter the no of available tickets: "))
sold_tickets=int(input("No of tickets sold: "))
result=available_tickets > sold_tickets
print(result)
# Additional logical operators( and , or)
buy_more=available_tickets<20 or available_tickets>40
print(buy_more)
# conditional statements 
# example 1
genre=input("Music genre")
if genre=="Hindi":
    print("Dil tu jaan tu, dard bhi dawa tu")
else:
    print("Baithi kithen baadalan te dur honi ae")
# example 2
password=input(input("Enter your password: "))
if password!=12345:
    print("Invalid format")
else:
    print("Valid password")

# Special string method
# .lower()-> converts all input to lowercases
# .upper()->converts all input to uppercase
# .capitalize()-> will captilize the first letter of the string 

# Nesting conditions
# example
# if the user enters "beach" then python replies "visit thailand".If the user eneter anything different from "beach"
# pyhton asks the user "warm or cold?".if the user enters "cold" python replies with "A japan ski holiday" anything else,
# python replies with "A mountain holiday to the rockies"
destination=input("enter the destination: ").lower()
if destination=="beach":
    print("visit thailand")
else:
 choose=input("what would u like to have warm or cold? : ").lower()
if choose=="cold":
    print("A japan ski holiday")
else:
    print("A moutain holiday in rockies")

# Creating our own functions
# A Piece of reusable code with unique name and can be called/used in other parts of code
# def function_name(parameter1,parameter2):
#     calling_function(parameter1,parameter2)
# example
def person_info(name,age,nationality):
    print("welcome: ",name)
    print("Your age is: ",age)
    print("You are from: ",nationality)
number=int(input("Amount: "))
for  i in range(number):
    name=input("Enter your name: ")
    age=input("enter your age: ")
    nationality=input("enter your nationality: ")
    person_info(name,age,nationality)


