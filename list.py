names = ["Anjy", "Tolu", "Tola", "Bola", "Bode"]
for i in names:
    if i == names[2]:
        print("Hi", i)
    else:
        print("Hello", i)

names = []
print(names)

names.append("Habeeb")
print(names)

names.append("Anjy")
print(names)

weight = [6.6, 4.7, 2.9, 7.9, 3.7]
names.extend(weight)
print(names)

names.insert(0, "kareem")
print(names)

names.insert(3, "Bukky")
print(names)

names.pop()
print(names)


names.pop(-4)
print(names)

other =[]
print(other)

other = names.copy()
print(other)

names = []
for i in range(1,6):
    a = input("Enter five names: ")
    names.append(a)
    
print(names)
names.pop(0)
names.pop()
print(names)



names = ["Bola", "Tito", "Tope", "Dami", "Anjy"]
print(names)
print(names[0:3])


names = ["Bola", "Tito", "Tope", "Dami", "Anjy", "Zainab"]
names.sort(reverse=True)
print(names)

names.remove("Bola")
print(names)

b = names.index("Anjy")
print(b)

