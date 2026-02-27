num_1 = input()
num_2 = input()

try:
    sum = int(num_1) + int(num_2)
    div = int(num_1)/int(num_2)

    print(sum)
    print(div)
except ZeroDivisionError:
    print('Cannot divide by zero')
except ValueError:
    print('Invalid input')

x = type(div)
print(x)