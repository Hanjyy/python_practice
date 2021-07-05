#LOOP
'''
1. For loop (Counting Loop)
2. While loop (Conditional Loop)
'''

'''
For Loop
'''
'''

for i in range(1,13):
    print(f"12 x {i} = {12*i}")
print("*************")
print("*************")


for i in range(13,21):
    print(f"5 x {i} = {5*i}")
print("*************")
print("*************")


for i in range(1,6,2):
    print("Hi Anjy")
print("*************")
print("*************")


for i in range(20,0,-1):
    print(i)
print("*************")
print("*************")



a = int(input("What multiple table do you want?: "))
b = int(input("What limit number do you want the table to go?: "))
for i in range(1,b+1):
    print(f"{a} x {i} = {i*a}")
print("*************")
print("*************")


names = ['habeeb', 'kareem', 'jimoh', 'anjy']
for i in names:
    if i == 'jimoh':
        print('You are doing well', i)
    else:
        print('Welcome ', i)
print("*************")
print("*************")


names = ['tolu', 'tosin', 'tola', 'bola', 'anjy']
for i in names:
    print("Thank you for your patronage",i)
print("*************")
print("*************")


a = int(input("Put in a number: "))
f =1
for i in range(a,0,-1):
    f = i * f
print(f)


a = int(input("Put in any number: "))
f = 0
for i in range(a,0,-1):
    f = i + f
print(f)

'''

#WHILE LOOP

x = 5
while x > 1:
    print("Hello world!!!")
    x -= 1
    if x == 3:
        print("hello")
print("*************")
print("*************")


a = int(input("Put in any number: "))
for i in range(1,13):
    if i == 4:
        continue
    else:
        print(f"{a} x {i} = {i*a}")
    
    
              


