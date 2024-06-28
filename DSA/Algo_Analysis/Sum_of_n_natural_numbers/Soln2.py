n = int(input('Enter a number : '))


def sol2():
    sum = 0
    for i in range(1, n + 1):
        sum = sum + i  # Calculate the sum within the loop
    return sum  # Return the final sum after the loop finishes

print(sol2())
