a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = []
sum_list = 0
for i in a:
    sum_list = sum_list + i
print(f"Sum of list: {sum_list}")

for i in a:
    result.append(i**3)
print(result)