#Create a function that determines the cost of a trip to Disney
#Adult tickets cost $100 per day
#Child tickets cost $90 per day

#Determine total cost of adults
#Determine total cost of children
#Add them to get daily cost
#Multiply by number of days for total cost

def DisneyCost(numberofAdults, numberofChildren, days):
    adultCost = 100*numberofAdults
    childCost = 90*numberofChildren
    dailyCost = adultCost + childCost
    finalCost = dailyCost*days
    return finalCost

print (DisneyCost(3, 4, 7))

#Greetings

def greet(player):
    if player == "Shia":
        return "Welcome, Mr. Le Bouf."
    else:
        return "Welcome, " + player

name1 = input("Enter player 1's name: ")
print (greet(name1))
name2 = input("Enter player 2's name: ")
print(greet(name2))


#Defaults
#User is a default that is set, if no input, then automatically "User"
def greetOptional(player = "User"):
    return "Welcome to the game, " + player 

print (greetOptional("Sophia"))
print (greetOptional())