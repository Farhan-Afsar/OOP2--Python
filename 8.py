name = input()

alpha = 0
digit = 0

for i in name:
    if i.isdigit():
        digit += 1
    if i.isalpha():
        alpha += 1

print(f"Alphabet: {alpha}")
print(f"Digit : {digit}")