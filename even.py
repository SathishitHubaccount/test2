def even_numbers(n):
    return [i for i in range(n + 1) if i % 2 == 0]


n=int(input("Enter a number: "))
print("Even numbers from 0 to", n, "are:", even_numbers(n))