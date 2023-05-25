first_string = input()
second_string = input()
last_printed_string = first_string

for current_character in range(len(first_string)):
    left_part = second_string[:current_character + 1]
    right_part = first_string[current_character + 1:]
    new_string = left_part + right_part
    if last_printed_string == new_string:
        continue
    last_printed_string = new_string
    print(last_printed_string)