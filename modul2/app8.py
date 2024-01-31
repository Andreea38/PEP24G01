# sir = input('Introduceti un sir:')
# lungime = len(sir)
# string = 'Lungimea sirului este: {}'
# print(string.format(lungime))
# print(f'Lungimea sirului este: {lungime}')
# print('Lungimea sirului este: ' + str(lungime))
# print('Lungimea sirului este: ', lungime, sep='')

#alta varianta
sir = input("Introduceti un sir: ")
print("Lungimea sirului este: {} ".format(len(sir)))
print(f'Lungimea sirului este: {len(sir)}')
print(f'Lungimea sirului este: ' + str(len(sir)))
print('Lungimea sirului este: ', len(sir), sep='')