def main():
    expression = input("Expression: ")
    x, y, z = expression.split()

    x = int(x)
    z = int(z)

    result = None

    if y == '+':
        result = x + z
    elif y == '-':
        result = x - z
    elif y == '*':
        result = x * z
    elif y == '/':
        result = x / z

    result = float(result)


main()
