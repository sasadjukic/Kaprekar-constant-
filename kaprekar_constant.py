
#Kaprekar's constant
number = input("Enter a four digit number with at least two different digits: ")

def sort_list(user_number) -> list:
    first_array = list(user_number)
    first_array.sort()
    if first_array[0] == "0":
        first_array.pop(0)

    return first_array

def reverse_list(user_number) -> list:
    second_array = list(user_number)
    second_array.sort()
    second_array.reverse()
    if second_array[0] == "0":
        second_array.pop(0)

    return second_array

def get_lower_number(low_num) -> int:
    helping_string = ""
    for num in low_num:
        helping_string += num

    return int(helping_string)

def get_higher_number(high_num) -> int:
    helping_string = ""
    for num in high_num:
        helping_string += num

    return int(helping_string)

def subtract(num_low, num_high) -> str:
    return str(num_high - num_low)

count = 0
while number != "6174":
    count += 1
    first_list = sort_list(number)
    second_list = reverse_list(number)
    f_number = get_lower_number(first_list)
    s_number = get_higher_number(second_list)
    math = subtract(f_number, s_number)
    print(f"Routine {count} = {math}")
    number = math

print(f"\nRoutine is completed. It took {count} attempts to reach Kaprekar's constant of {number}")
