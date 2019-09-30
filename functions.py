#Function that prints name in all uppercase
def shout(name):
    name = name.upper()
    return "Hello " + name + "!"

print(shout("Sophia"))
print(shout("Isha"))
print(shout("Sadia"))

#Function that prints name in all lowercase
def whisper(name):
    name = name.lower()
    return "Hello " + name + "."

print(whisper("Sophia"))
print(whisper("Isha"))
print(whisper("Sadia"))

def pi_reminder():
    return 3.14159265

print(pi_reminder())

def add (x, y):
    total = x + y
    return total

print(add(2, 3))

age = 17 

def have_a_birthday():
    #global age <-Changes global variable
    age = 25
    age += 1 
    print ("Happy birthday! You are now " + str(age))
    return age 
    
#Returns calculated age, and then returns global age. Function can temporarily redefine a variable