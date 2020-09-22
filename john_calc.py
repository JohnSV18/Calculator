# This is the welcome message explaining the calculator and the deal we are giving for the coins.
print("Welcome to Zund and Buster's\n")
print(" This will tell you how many gaming coins everyone can get for everyones cards!\n")
print("For every $1 you get 5 coins, WHAT A STEAL!\n")

#In this part of the code I am creating 2 variables , dollar is created to hold the amount of money a user is going to put in
dollars = int(input("How many bean$(Bill$ only!) would you like to insert? "))
#The variable cards is holding the amount of cards that are going to be refilled
#Both of these variables are wrapped with int because when you get input from the user it comes out as a string
#and you can't calculate a string.
cards = int(input("How many gaming cards would you like to refill? "))


#This is an if statement that tells me if the result of 'dollars / cards' has a remainder or not.
#Since we are giving coins, nobody could get '0.5' of coins so the if statment helps round the total 
# number of coins up! the variable 'total_coins' holds the result of the calculation which is the amount 
# of money put it divided by the amount of cards to be refilled and then multiplied by 5 because for every one
#dollar you get 5 gaming coins 

if dollars % cards == 0:
    total_coins =int(dollars / cards * 5)

#in the case that there is a remainder the calculation would come out with a decimal so to avoid that and round up we add 1
# and then wrap it around an int 
#because it will then round down

else:
    total_coins = int(dollars / cards * 5 + 1)



   

#this is printing out a message on how many coins you have but since the variable 'total_coins' is an int type, 
#I'm wrapping it with str so that I can add it into the message

print("Great!! You guys get " + str(total_coins) + " coins on each card!")

