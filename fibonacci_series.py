n = int(input("Enter the number of terms: "))

a, b = 0, 1

print(f"Fibonacci series ({n} terms):", end=" ")

for i in range(n):
    print(a, end="")
    if i != n - 1:
        print(", ", end="")
    a, b = b, a + b
