num = int(input())

if 80 <= num <= 100:
    print("A+")
elif 75 <= num <= 79:
    print("A")
elif 70 <= num <= 74:
    print("A-")
elif 65 <= num <= 69:
    print("B+")
elif 60 <= num <= 64:
    print("B")
elif 55 <= num <= 59:
    print("B-")
elif 50 <= num <= 54:
    print("C+")
elif 45 <= num <= 49:
    print("C")
elif 40 <= num <= 44:
    print("D")
else:
    print("F")