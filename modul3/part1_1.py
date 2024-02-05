#If + condition
# var1 = int(input("Add number:"))
#
# if var1 == 1:
#     print(var1)
# else:
#     print("Number is not 1!")
#
# #true-ish
# print(bool(''), 'Empty string')
# print(bool('0'), '0 string')  # 0 ca si string este True
# print(bool(0), '0 integer')  # 0 ca si numar este False
# print(bool(-1000), '-1000 integer')  # orice numar dif de 0 este True
# print(bool(None), 'None object')

# var1 = int(input("Add number:"))
#
# if 1 + var1:
#     print(var1)
# else:
#     print("Number is not x!")

#elif
# var1 = int(input("Add number:"))
#
# if 1 + var1:
#     print('first result: ', var1)
# elif 2 + var1:
#     print(f'second result: {2 + var1}')
# else:
#     print("Number is not x!")

#and
var1 = int(input("Add number:"))

if var1 > 10:
    print('positive result: ', var1)
elif var1 < -10:
    print(f'negative result: {var1}')
elif var1 <= 10 and var1 > 0:
    print('result is in interval (0-10]')
elif var1 >= -10 and var1 < 0:
    print('result is in interval [-10-0)')
else:
    print("Number is 0!")

