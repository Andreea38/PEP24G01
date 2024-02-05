#for

my_str = 'Hello World'
my_int = 100

for letter in my_str:
    print(letter)

# for number in my_int:  #obiectul de tip int nu poate fii interabil, nu poate fii spart in bucati mai mici
#     print(number)

for number in range(my_int+1):
    print(number)

# user_input = input('give string: ')
# for letter in user_input:
#     print(letter)
#     if letter == 'x':
#         print('found x letter')
#         break
# else:
#     print('could not find "x"')
#
#
user_input = input('give string: ')  # do not print x
for letter in user_input:
    if letter == 'x':
        continue
    print(letter)
else:
    print('x was not printed')

