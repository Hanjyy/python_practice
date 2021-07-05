a = int(input("Input any number: "))
if a%2 == 0:
        print("This is an even number")
else:
        print("This is an odd number")


a = int(input("Input the number of classes held: "))
b = int(input("Input the number of classes attended: "))
print(a,b)

missed = a-b

percentage = (b/a) * 100
print("The student's perecentage is", percentage)

if percentage < 75:
    print("This student is not allowed to sit for the exam")
else:
    print("The student is allowed to sit for the exam")
    


'''
a = int(input("Input any number: "))
b = int(input("Input any number: "))
c = int(input("Input any number: "))
d = int(input("Input any number: "))
e = int(input("Input any number: "))

l = int(input("Input any length for the table: "))

for i in range(1, l+1):
        print(f"{a} x {i} = {a*i}")
for i in range(1, l+1):
        print(f"{b} x {i} ={b*i}")
for i in range(1, l+1):
        print(f"{c} x {i} = {c*i}")
for i in range(1, l+1):
        print(f"{d} x {i} = {d*i}")
for i in range(1, l+1):
        print(f"{e} x {i} = {e*i}")

a = int(input("Put in any number: "))
b = int(input("Put in any number: "))
if a > b:
        print(f"{a} is greater than {b}")
else:
        print(f"{a} is not grater than {b}")

        

a = input("Input any name of the month: ")
if a == "September" or a == "April" or a == "June" or a == "November":
        print(f"{a} has 30 days")
elif a == "January" or  a =="March" or a == "May" or a == "July" or a == "August" or a =="October" or a =="December":
        print(f"{a} has 31 days")
else:
        print(f"{a} has 28/29 days")
'''
          
              


