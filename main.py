

def fibonacci_generator(n):
    x = 0
    y = 1
    z = 1
    fibonacci_sequence = [x, y]
    if n == 1:
        return [x]
    elif n == 2:
        return fibonacci_sequence
    else:
        while (n - 1) > z:
            z += 1
            new_number = x + y
            x = y
            y = new_number
            fibonacci_sequence.append(new_number)
        return fibonacci_sequence



output = fibonacci_generator(4)
print(output)