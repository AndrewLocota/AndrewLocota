n = 90
factorial = 1
for i in range(1, n + 1):
    factorial = factorial * i

print("The factorial of", n, "is:", factorial)

while n > 1:
    if n % 2 == 0:
        n = n/2
    else:
        n = 3 * n + 1
    print(n)