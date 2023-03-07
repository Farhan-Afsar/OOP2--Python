a = [1, 2, 33, 4, 5, 0, 7, 8, -1, 10]
max = a[0]
min = a[0];

for i in a:
    if i > max:
        max = i
    if i < min:
        min = i

print("Max element : ", max)
print("Min element : ", min)
