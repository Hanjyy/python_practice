'''
purchase_price = int(input("What is the purchase price: "))
discount_price_10 = (10 /100 )* (purchase_price)
final_price_10 = purchase_price - discount_price_10

discount_price_20 = (20/100) * (purchase_price)
final_price_20 = purchase_price - discount_price_20

if purchase_price < 10:
    print("10%", final_price_10, discount_price_10)
else:
    print("20%",final_price_20, discount_price_20)


user_gender = input("Enter your gender: ")
if user_gender == "M":
    print("You are not eligible")
else:
    print("You are eligible")

    
user_age = int(input("How old are you: "))
if user_age >= 10 and user_age <= 12:
    print("You are eligible to play on the team")
else:
    print("You are not eligible to play on the team")

gas_tank =int(input("What is your tank size in litres: "))
tank_percentage = int(input("What is the percentage of your tank: "))
km_litre = int(input("How many km/litre does your car get: "))

current_litre = (tank_percentage/100) * (gas_tank)
distance_litre_can_go = (current_litre * km_litre) + 5

if distance_litre_can_go < 200:
    print(f"You can go another {distance_litre_can_go} km")
    print("The next gas station is 200 km away")
    print("Get gas now")
else:
    print(f"You can go another {distance_litre_can_go} km")
    print("The next gas sation is 200 km away")
    print("You can wait for the next station")
    '''

password = "Anjola"
pin = input("Enter a secret password: ")

if pin == password:
    print("You're in")
else:
    print("Ask the owner")
    print("Learn enough python to look at the code and figure out")

'''Q = input("Enter any word: ")
if Q.isupper() or Q.islower():
    print("It is a fact")'''

