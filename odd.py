def odd(n):
    return [i for i in range(n + 1) if i % 2 != 0]

n = int(input("Enter a number: "))
print("Odd numbers from 0 to", n, "are:", odd(n))