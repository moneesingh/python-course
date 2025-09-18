print("Welcome to Pizza delivery program")
print("Pizza size options and their costs are: S($15), M($20), L($25)?")
size = input("What pizza size do you want? S, M, L?").lower() 
print("Pepperoni topping for S is $3, M or L is $2")
pepperoni = input("Do you want pepperoni on pizza? Y or N?").lower()
print("Extra cheese is $1 extra")
extra_cheese = input("Do you want extra cheese? Y or N?")

#cost calculator
if (size == "s"):
    cost = 15
elif (size == "m"):
    cost = 20
elif (size == "l"):
    cost = 25
else:
    print("Wrong pizza size picked, valid option are S, M, L")
print(f"Pizza cost for {size} is {cost}") 

if (pepperoni == "y"):
    if (size == "s"):
        cost += 3
    else:
        cost += 2

if (extra_cheese == "y"):
   cost += 1

print(f"Pizza cost for size:{size}, pepperoni:{pepperoni}, extra_cheese:{extra_cheese} is {cost}")    

