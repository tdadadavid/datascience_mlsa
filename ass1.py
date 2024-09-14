#Problem 1
A_grades = [90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]
B_grades = [80, 81, 82, 83, 84, 85, 86, 87, 88, 89]
C_grades = [70, 71, 72, 73, 74, 75, 76, 77, 78, 79]
D_grades = [60, 61, 62, 63, 64, 65, 66, 67, 68, 69]

grade = int(input('Please enter your grade: '))

if grade in A_grades:
    print('Your grade is A')

elif grade in B_grades:
    print('Your grade is B')

elif grade in C_grades:
    print('Your grade is C')

elif grade in D_grades:
    print('Your grade is D')

elif grade <= 59:
    print('Your grade is F')

else:
    print('Value outside range')

#Problem 2

print('''Good day user!
Enter 'help' to view the menu''')

command = ''
shop_list = ['name', 'quantity', 'price', 'name', 'quantity', 'price']
while True:
    command = input('> ').lower()
    if command == 'add':
        a_name = input('Enter product name: ')
        a_quantity = input('Enter product quantity: ')
        a_price = input('Enter product price: ')
        shop_list[0] = a_name
        shop_list[1] = a_quantity
        shop_list[2] = a_price
    elif command == 'remove':
        r_name = input('Enter product name: ')
        r_quantity = input('Enter product quantity: ')
        r_price = input('Enter product price: ')
        shop_list.remove(r_name)
        shop_list.remove(r_quantity)
        shop_list.remove(r_price)
    elif command == 'update':
        u_name = input('Enter new product name: ')
        u_quantity = input('Enter new product quantity: ')
        u_price = input('Enter new product price: ')
        shop_list[0] = u_name
        shop_list[1] = u_quantity
        shop_list[2] = u_price
    elif command == 'display':
        print(shop_list)
    elif command == 'help':
        print('''
Enter add - To add product name, then price, then quantity
Enter remove - To remove product name, then price, then quantity
Enter update - To update product new name, then new quantity
Enter display - To display product full details
Enter quit - To exit the program''')
    elif command == 'quit':
        break

else:
    print('''I don't understand that''')

#Problem 3
print('Good day user ')

A_operation = input('What arithmetic operation would you like to perform: ')
A_operation.lower()

a = int(input('Input first value: '))
b = int(input('Input second value: '))

if A_operation == 'addition':
    sum = a + b
    print(f'Your sum is {sum}')

if A_operation == 'multiplication':
    product = a * b
    print(f'Your product is {product}')

if A_operation == 'division':
    Division = a / b
    print(f'Your division is {Division}')

if A_operation == 'subtraction':
    difference = a - b
    print(f'Your difference is {difference}')


#Problem 4
year = int(input('Please input your year:'))
year_determiner = year % 4
if year_determiner == 0:
    print(f'This input year {year} is a Leap year')
else:
    print('Its a common year.')