n = 5
fibonacci = 1
prev_fibonacci = 0

for i in range(1, n+1):
    fibonacci, prev_fibonacci = fibonacci + prev_fibonacci, fibonacci
    print(fibonacci)


name = input("Whats your name?")
print("Hello",name)