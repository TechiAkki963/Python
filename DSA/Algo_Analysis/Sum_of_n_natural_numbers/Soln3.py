n = int(input('Enter a number : '))


def sol3():
    sum = 0
    for i in range(1, n + 1):
        for j in range(1, i + 1):
           sum = sum + 1  # Calculate the sum within the loop
    return sum  # Return the final sum after the loop finishes

print(sol3())
