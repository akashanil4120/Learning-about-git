# write a program that asks the user for their name and age, then prints a message with that information using functions 

name = input("Please enter your name ")
age = int(input("Please enter your age "))

def name_age (x,z):
    print("Your name is "+ x,"and you are ",+ z, "years old !" )

name_age(name,age)


# a fuction can also return a value using the return statement

name = input("Please enter your name ")
age = int(input("Please enter your age "))

def name_age (x,z):
    return "Your name is "+ x,"and you are ",+ z, "years old !"

mesage = name_age(name,age)
print(mesage)



