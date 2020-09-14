# Ian Brinkerhoff
# CS 3620
# Coding Challenge 3

# Part 1:
# func1 - student discount, func2 - additional discount
# Reduces price by 10 percent
def func1(price):
    price -= price * 0.10
    return price


# Reduces price by 5 percent
def func2(func, price):
    price -= price * 0.05
    return func(price)


# Price is set as 100
print("Part1:")
print("Price: $", func2(func1, 100))
print()

# Part 2:
# lambda expression
print("Part2:")
value = (lambda x: x * (x+5)**2)(5)
print(value)
print()


# Part 3:
# functions for list
def ten_pct(p):
    return p - (p * 0.10)


# Takes list prices, takes 10 percent off every price and moves to result
print("Part3:")
prices = [10.00, 25.00, 17.30, 35.00, 14.65, 5.20]
result = list(map(ten_pct, prices))
print("Original prices: ", prices)
print("New prices: ", result)
print()


# Part 4:
# OOP - Inheritance
print("Part4:")


class Computer:
    def __init__(self, ram, storage):
        self.ram = ram
        self.storage = storage

    def getspecs(self, ram, storage):
        self.ram = ram
        self.storage = storage

    def displayspecs(self):
        print("RAM(GB):", self.ram)
        print("Storage(GB):", self.storage)


class Desktop(Computer):
    def get_desktop(self, model):
        self.model = model

    def display_desktop(self):
        print("Model:", self.model)


class Laptop(Computer):
    def get_laptop(self, weight):
        self.weight = weight

    def display_laptop(self):
        print("Weight(lbs):", self.weight)


# Create instance of laptop, gather weight, ram, and storage
laptop1 = Laptop("", "")
l_weight = input("Enter laptop weight(lbs): ")
l_ram = input("Enter laptop ram(GB): ")
l_storage = input("Enter laptop storage(GB): ")
laptop1.get_laptop(l_weight)
laptop1.getspecs(l_ram, l_storage)
print()

# Create instance of desktop, gather model, ram, and storage
desktop1 = Desktop("", "")
d_model = input("Enter desktop model: ")
d_ram = input("Enter desktop ram(GB): ")
d_storage = input("Enter desktop storage(GB): ")
desktop1.get_desktop(d_model)
desktop1.getspecs(d_ram, d_storage)
print()

print("Laptop Specs:")
# Display Laptop Specs
laptop1.displayspecs()
laptop1.display_laptop()
print()
print("Desktop Specs:")
# Display Desktop Specs
desktop1.displayspecs()
desktop1.display_desktop()
print()


# Part 5:
# Operator Overloading
print("Part5: ")


class Overload:
    def __init__(self, x):
        self.x = x

    def __mul__(self, other):
        x = self.x + other.x
        return x


# Create instance of Overload
x = Overload(5)
y = Overload(6)
# Print x * y, should display x + y
print(x * y)
