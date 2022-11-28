

# Kaprekar's constant

def get_number() -> str:
    '''
       Accept string as input to allow inputs with leading zeroes 0310
       Max of these digits is a valid number 3100
       Min is a valid number 13 
    '''

    while True:
        'while loop will check and only accept the correct input'

        number = input("Enter a four digit number with at least two different digits: ")
        digits = set(x for x in number)
        if len(number) == 4 and 4 >= len(digits) >= 2:
            break
    
    return number

def lower_number(user_number) -> int:
    'get the lowest possible number from our four digit string'

    lower_number = int(''.join(sorted(user_number)))
    return lower_number

def higher_number(user_number) -> int:
    'get the highest possible number from our four digit string'

    higher_number = int(''.join(sorted(user_number, reverse = True)))
    return higher_number

def subtract(num_low, num_high) -> str:
    'subtract two numbers we got from our initial four digit string'

    return str(num_high - num_low)

def main():
    'main function with the while loop will repeat until we reach number 6174 in form of a string' 

    number = get_number()
    count = 0
    while number != "6174":
        count += 1
        f_number = lower_number(number)
        s_number = higher_number(number)
        math = subtract(f_number, s_number)
        print(f"Routine {count} = {math}")
        number = math

    print(f"\nRoutine is completed. It took {count} attempts to reach Kaprekar's constant of {number}")

if __name__ == '__main__':
    main()
