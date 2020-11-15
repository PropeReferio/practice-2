name = 'Bo'
age = 32
money = 4.32

print("%s is %d years old and he has $%1.2f to his name" %(name, age, money))
print("{2} is {1} years old and he has ${0} to his name".format(name, age, money))
print("{} is {} years old and he has ${} to his name".format(name, age, money))

print(f"{name} is {age} years old and he has ${money * age} to his name")
print(f"Too many digits: {age:.9f}")