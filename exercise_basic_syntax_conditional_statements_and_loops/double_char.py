string = input()
while string != 'End':
    if string != 'SoftUni':
        new_string = ''
        for ch in string:
            new_string += ch * 2
        print(new_string)
    string = input()
