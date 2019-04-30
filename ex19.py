# define function with it 2 arguments
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print(f"You have {cheese_count} cheese!")
    print(f"You have {boxes_of_crackers} boxes of crackers!")
    print(f"Man that's enough for a party!")
    print(f"Get a blanket.\n")

# print status string
print("We can just give the function numbers directly:")
# call function with numbers
cheese_and_crackers(20, 30)

#print status string
print("Or, we can use the variables from our script:")

# assign 2 variables to numbers
amount_of_cheese = 10
amount_of_crackers = 50
# call function with number assigned variables 
cheese_and_crackers(amount_of_cheese, amount_of_crackers)

print("We can do math inside too:")
# call function with number operands and arithmetic operations
cheese_and_crackers(10 + 20, 5 + 6)

# print string
print("And we can combine the two, variables and math:")
# Call function with vars combined with numbers
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)

def nut_bolt_count(nuts, bolts):
    print(f"We have {nuts} nuts.")
    print(f"We have {bolts} bolts.")
    if nuts == bolts:
        print(f"We have enought of each, we're good to go!")
    elif nuts >= bolts:
        print(f"We need more bolts")
    else:
        print(f"We need more nuts")
nut_bolt_count(50, 40)
nut_bolt_count(50, 50)

def user_ask():
    print("How many nuts do we have?")
    nuts = input()
    print("How many bolts we have?")
    bolts = input()
    nut_bolt_count(nuts, bolts)
user_ask()
