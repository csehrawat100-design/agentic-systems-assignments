name = input('Entre your name: ')
age_input = input('Entre your age: ')

try:
    age = int(age_input)
    print('Hello', name)
    if age < 0:
        print('Age cannot be negative\nYou are not eligible to vote')
    elif age < 13:
        print('You are a Child\nYou are not eligible to vote')
    elif age < 18:
        print('You are a Teenager\nYou are not eligible to vote')
    elif age < 60:
        print('You are an Adult\nYou are eligible to vote')
    elif age >= 60:
        print('You are a Senior Citizen\nYou are eligible to vote')
except:
    print('Invalid age input')
