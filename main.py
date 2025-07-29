def main():
    print("Welcome to the Arithmetic program!")
    first_number = float(input('Insert the first number: '))
    second_number = float(input('Insert the second number: '))
    execute(first_number, second_number)


def execute(first, second):
    operation = input('Select the operation:\n1 - Addition\n2 - Subtraction\n3 - Multiplication\n4 - Division\nOption: ')
    
    result = ''

    match operation:
        case '1':
            result = addition(first,second)
            print("\nAddition")
        case '2':
            result = subtraction(first,second)
            print("\nSubtraction")
        case '3':
            result = multiplication(first,second)
            print("\nMultiplication")
        case '4':
            result = division(first,second)
            print("\nDivision")
        case _:
            print('Invalid option!')
            execute(first,second)
            return
    
    print("Result: " + str(result))


def addition(first, second):
    return first + second

def subtraction(first, second):
    return first - second

def multiplication(first, second):
    return first * second

def division(first, second):
    return first / second

if __name__ == "__main__":
    main()

