print("Hello, I am learning Python!")
name ="Ali"
print(name)
age = 40
print(age)
city = "Karachi"
print(city)
city = "Lahore"
print(city)
price = 125.50
is_student = True

print(type(name))
print(type(age))
print(type(price))
print(type(is_student)) 

price = 750
quantity = 4

total = price * quantity

print("Total:", total)

price = 200
quantity = 5
discount = 100

total = price * quantity
final_price = total - discount

print(final_price)

name = input ("What is your name? ")
city = input ("Which city do you live in? ")

print("Your name is", name)
print("You live in", city)

product = input("What product are you buying? ")
price = float(input("What is the price? "))
quantity = int(input("How many do you want? "))

total = price * quantity

print("Product:", product)
print("Total:", total)

age = 40

print(age > 18)
print(age == 40)
print(age < 18)
print(age != 40)

age = 25
has_ticket = True
is_blocked = False

if age >= 18 and has_ticket and not is_blocked:
    print("Entry allowed")
else:
    print("Entry denied")

    print(True and False)
print(False or True)
print(not False)