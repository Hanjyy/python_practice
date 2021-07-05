#OPERATORS

'''a = input("Enter your name: ")
print(a.upper())
print(a.lower())
print(a.title())
print(int(a) + 2)
'''



'''
distance = 200
speed = 80
print(distance / speed)


initial_total_payment = 35.27
tip = (15/100) * 35.27
final_payment = initial_total_payment + tip
individual_fee = final_payment / 3
print(individual_fee)



height = 1.25
breath = 16.7
Area = height * breath
perimeter = 2*(height + breath)
print(Area)
print(perimeter)

F = int(input("Enter the temperature value: "))
formula = 5/9 *(F-32)
print("The value of the temperature you inputed in celsius is: ",formula)
'''




'''
Write a program that ask a user for a number,
then your program should tell the user if the number inputted is even or odd.
'''



#LOGICAL OPERATORS
'''
and
or

T and T = T
T and F = F
F and F = F
F and T = F

T or T = T
T or F = T
F or T = T
F or F = F
'''


#COMPARISON OPERATORS
'''
== means equal equal
!= means Not equal
<= means less than or equals to
>= means greater than or equals to
> means greater than
< means less than
is
is not
'''

'''
x = 5
y = 9

print(x>y and x<y)
print(x<y)
print(x==y)
print(x!=y)
print(x>=y)
print(x<=y)
print(x is y)
print(x is not y)
'''

#Task
'''
write a program that converts the user length input from cm to mm
'''
'''
x = int(input("Enter any number in cm: "))
formular = x * 10
print("The value of the number you inputed in mm is: ",formular)
'''


#Condition Statement

'''
number = int(input("Enter guess number:   "))
secret_number = 5
if number == secret_number:
    print("Hello World")
else:

    print("The number you inputted was not the secret number"
          , "the secret number is", secret_number)

if number == secret_number:
    print("WOW..., you are a genius, you guessed right")
elif number < secret_number:
    print("U are almost there, sorry your guess was less than the secret number")
elif number > secret_number:
    print("U are almost there, sorry your guess was greater than the secret number")
    '''


#Task
'''
Write a program that ask a user for his score in a subject, then your program
should display the grade of the score

'''
score = int(input("Input your score: "))
if score >=40 and score <= 49:
    print("D")
elif score >=50 and score <= 59:
    print("C")
elif score >=60 and score <= 69:
    print("B")
elif score >=70 and score <= 100:
    print("A")
elif score < 40:
    print("F")
