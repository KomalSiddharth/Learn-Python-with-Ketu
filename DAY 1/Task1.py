# QUESTION NO 1
# create a variable for travelling, flight_cost, insurance ,passport, baggage
# create a variable to calculate the cost of them
# print off the total cost with strings and variables
# NOTE-> that there are 5 people travelling
filght_cost=5000
insurance=200
passort=110
baggage=20
total=(filght_cost + insurance + passort + baggage)*5
print("the total cost would be:",total)

# QUESTION NO 2
# create 4 variable for ticket_price, 1 variable is for no of adults & one for children
# create for adult price and one for children price
# create a variable to calculate cost
# print off the total with strings and integers
no_of_adults=5
no_of_children=2
adult_price=1000
children_price=500
total=(no_of_children*children_price)+(no_of_adults*adult_price)
print("The total price for tickets would be: ",total)

# QUESTION NO 3
# A resort offers the normal price of 500 per night,a family wants to stay for one week
# A resort is offereing a special promo of 30% off
# print the last minute trip price with string and variables
base_price=500
no_of_days=7
total=(500*7)*0.3
print("The trip price will be: ",total)

# QUESTION NO 4
# Create 3 variables to collect info fro users
# theses variables are first name,country and city
# print off their information -> ex. John lives in seattle,USA
name=input("Enter your name: ")
country=input("Country: ")
city=input("city: ")
print(name, "lives in" , city , country)

# QUESTION NO 5
# create 2 variables to gather information of users
# rental price for 1 day and no of days
# create a total variable to add these 2 variables 
# print out their total cost
rental_price=500
no_of_days=3
total_price=( rental_price * no_of_days )
print("The total price would be: ",total_price)

# QUESTION NO 6
# A user can enter the weight of 3 packages
# create a variable to add these 3 variables together
# offer a 20% discount on shipping weight
# print off total cost for shipment
weight1=input("Enter your 1st weight: ")
weight2=input("Enter your 2nd weight: ")
weight3=input("Enter your 3rd weight: ")
weight1=int(weight1)
weight2=int(weight2)
weight3=int(weight3)
total= (weight1 + weight2 +weight3)*0.8
print("The total shipping price would be: ",total)

# QUESTION NO 7
# create a user ID
# collect their name,age
# their user id number is 786147
# convert everything to string
# print off their information
user_ID=786147
name=input("Enter your name")
age=input("Enter your age: ")
# age=int(age)
id=str(user_ID)
print("welcome, "+name +".Your are"+age+". Your id is:"+id)

# QUESTION NO 8
# short the code of question 6
weight1=int(input("Enter weight1: "))
weight2=int(input("Enter weight2: "))
weight3=int(input("Enter weight3: "))
total=weight1+weight2+weight3
print(total)

# QUESTION NO 9
# Collect the income from the user
# collect expenses for food,rent,other income from the user
# get the total amount left after expenses
# print off the remaning total
income=int(input("Enter your income: "))
food=int(input("Enter your food expense: "))
rent=int(input("Enter your rent expenese: "))
other=int(input("Enter your other expenses: "))
total=income-(food+rent+other)
print("The total left expense is: ")

# QUESTION NO 10
# Collect a users monthly pay
# Collect the users extra hours worked
# Their bonnus is 20% of their monthly salary * extra pay hour
# print off their overtime bonus payoff
monthly_pay=int(input("enter your monthly pay: "))
extra_hours=int(input("enter the extra hours: "))
bonus=(monthly_pay * extra_hours) *0.8
print("The extra overtime bonus payoff is: ",bonus)

# QUESTION NO 11
# create a discount program
# ask the user which type of trip they are taking
# ask the user for an expected trip cost
# if the trip is a bussiness trip and the price is 1200 or over return true
# print if a customer gets a discount or not
type=input("enter the type of trip: ").lower()
cost=int(input("enter your expected cost: "))
if type=="Bussiness" or cost>=1200:
    print("True")
else:
    print("False")

# PROBLEM NO 12
# allow a user to enter a special discount code
# if the discount if equal to winter23 the give 20% discount
# otherwise return the code is invalid
code=input("enter your discount code: ")
if code=="winter23":
    print("Avail your 20% discount")
else:
    print("The code is invalid")

# QUESTION NO 13
# create a program that recommends a type of trip
# gather the trip cost from the user
# if the cost is less than 360,tell them to visit jaipur
# if the cost is over/equal to 350 and less than 1000 tell them go to road trip
# if the cost is over 1000, tell them to catch a flight to go to beach
# NOTE no matter the answer print have fun! at the end of your program
cost=int(input("Enter your estimated cost: "))
if cost<360:
    print("visit jaipur")
if cost>=350 and cost<1000:
    print("go for a road trip")
if cost>1000:
    print("catch a flight to go to a beach")
print("Have fun!")

# QUESTION NO 14
# create a program that gathers bag weight in KG and also either domestic/international from the user
# if the weight is less than or equal to 18 KG then the price is 35
# otherwise the price is 45
# then check if the destination is domestic or international
# if it's domestic add 300 to the price
# add 750 to the price
# print off the estimated cost
# NOTE what is the price variable?
weight=int(input("Enter the weight in kg: "))
type=input("enter the type: ").tolower()
if weight<=18:
    price=35
else:
   price=45
if type=="domestic":
    print(price+300)
elif type=="international":
    print(price+750)
else:
    print("Spelling error!")
print("The estimated cost is: ",price)

# QUESTION NO 15
# ask a user if they want to watch a movie
# if the user says yes ask their genre they wanna watch
# if they say comedy tell them to watch hangover trilogy
# otherwise tell them to watch top gun
# if they don't want to watch amovie tell them to watch a TV series
ask=input("Do u wanna watch a movie").lower()
if ask=="yes":
  genre=input("Which genre?").lower()
  if genre=="comedy":
     print("Hangover trilogy")
  else:
     print("Top gun")
else:
    print("Watch a TV series")

# PROBLEM NO 16
# ask the user if they want a hotel or resort
# if they want a resort,ask them a max price they want to spend per night
# if their max price is greater than or equal to 350,tell them to book siz senses resort
# otherwise  they can go to four seasons
# if they want a hotel,tell them to go to the nearest hilton
type=input("hotel or resort? : ").lower()
if type=="resort":
    ask_cost=int(input("enter the maximum cost: "))
    if ask_cost>=350:
        print("Book six senses resort")
    else:
        print("Book for seasons resort")
elif type=="hotel":
    print("visit nearest station")

# PROBLEM NO 17
# Ask the user for 3 different prices for 3 different products
# if the 3rd product is most expensive ,give them half of their total
# if the 1st product is most expensive, give them 60% off
# print their total
product1=int(input("Enter price of product 1: "))
product2=int(input("Enter price of product 2: "))
product3=int(input("Enter price of product 3: "))
total=product1 + product2 + product3
if product3>product2 and product2>product3:
    total=total * 0.33
if product1>product2 and product2>product3:
    total=total*0.5
print("Total: ",total)

# PROBLEM NO 18
# ask the user for a cost and current time in hour form
# if the time is from/between 7-9 then get a 20% discount tell them their new total
# also if the time is between 10-6 there is no discount tell them their total
# any other time tell them we are closed
cost=int(input("enter the cost: "))
time=int(input("Enter the time: "))
if time>=7 and time<=9:
    cost=cost*0.8
    print("new total: ",cost)
if time>=6 and time<=10:
    print("No discount, Thus total cost is: ",cost)
else:
    print("we are closed")

# PROBLEM NO 19
# similar to our slides,create paascode character
# if the paascode contains an invalid characters print the invalid symbol
passcode=input("enter the passcode: ")
invalid="!@#$%^&*()"
for letter in passcode:
    if letter in invalid:
        print("This is not allowed: ",letter)

# PROBLEM NO 20
# create a program that counts vowels in a word
# the program takes an input for a single word
# loops through the word and checks the vowels
# at the end print off the numbers of vowels in the word
word=input("enter the word: ")
vowel="aeiou"
for letter in word:
    if letter in vowel:
        print("the vowels in word are: ",letter)

# PROBLEM NO 21
# create a program that checks for a valid phone number
# if the program contains anything besides a number
# print off "invaild phone number" and break the loop
phone=int(input("enter your contact number: "))
valid="1234567890"
for num in phone:
    if num in valid:
        print(num)
    else:
        print("Invalid phone number!")
        break

# PROBLEM NO 22
# create a program that takes a number of guests
# for each guest ask their name and age
# if guests is 18 or older welcome the user
# otherwise tell the user that they must be 18 to drink
num=int(input("Enter the number of guests: "))
for i in range(num):
    name=input("Enter your name: ")
    age=int(input("Enter your age: "))
    if age>=18:
        print("Welcome",name)
    else:
        print("You must be 18 to drink")

# PROBLEM NO 23
# A user has 5 chances to login into a account
# Their username is "admin" and their password is"12345"
# printoff how many tries it took them to login in
# if they enter wrong 5 times,print off "you are not admin"
for i in range(5):
    name=input("enter your username: ")
    password=input("enter your password: ")
    if name=="admin" and password=="12345":
     print("Welcome admin!")
     break
    if name!="admin" and password!="12345":
        print("you are not an admin")


