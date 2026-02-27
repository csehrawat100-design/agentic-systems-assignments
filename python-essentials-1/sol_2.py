
first_name = input('Enter your first name: ')
surname_name = input('Enter your surname: ')
age = input('Enter your age: ')

try:
    if int(age) > 0:
        full_name = first_name + surname_name
        print(f'Full Name: {full_name}\nYou will be {int(age) + 1} next year')
    else:
        print('Age cannot be negative')

except ValueError:
    print('Invalid age input')

 