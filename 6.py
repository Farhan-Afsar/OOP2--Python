def sum_(a, b):
    return a + b


def sub(a, b):
    return a - b


def mul(a, b):
    return a * b


def div(a, b):
    return a / b


def mod(a, b):
    return a % b


a = int(input())
b = int(input())

print(f"Sum of {a} and {b} is {sum_(a,b)}")
print(f"Sub of {a} and {b} is {sub(a,b)}")
print(f"Multi of {a} and {b} is {mul(a,b)}")
print(f"Div of {a} and {b} is {div(a,b)}")
print(f"Mod of {a} and {b} is {mod(a,b)}")
