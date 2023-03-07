even_sum = 0
odd_sum = 0
prime_sum = 0
for i in range(1, 1001):
    if i % 2 == 0:
        even_sum = even_sum + i
    else:
        odd_sum = odd_sum + i

print(f"Even sum: {even_sum}")
print(f"Odd sum: {odd_sum}")


def is_prime(n):
    for i in range(2, n):
        if (n % i) == 0:
            return False
    return True


for i in range(2, 101):
    if is_prime(i):
        prime_sum = prime_sum + i

print(f"Prime Sum : {prime_sum}")