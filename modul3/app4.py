parola = 7788
# for incercare in range(99999):
#     parola_introdusa = int(input("Introduceti parola: "))
#     if parola == parola_introdusa:
#         print('Access granted')
#         break
#     else:
#         print('Access denied')

while True:
    parola_introdusa = int(input('Introduceti parola: '))
    if parola == parola_introdusa:
        print('Access granted')
        break
    else:
        print('Access denied')