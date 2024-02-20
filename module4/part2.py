#dictionare

my_dict = {'one': 1, 'two': 2, 'true': True} #cheile nu pot fii modificate pe urma, sunt hashable, valorile pot fii de orice tip, int, string, liste, etc
print(my_dict)
print(type(my_dict))

my_dict2 = dict()  #dictionar gol
print(my_dict2)

my_dict = dict(one=1, two=2)  #ia one ca si cheie si 1 ca si valoare
print(my_dict)

#dictionarele sunt iterabile
for element in my_dict:  #iteratie peste cheile dict sau my_dict.keys()
    print('Dict key:', element)

for element in my_dict.values():  # iteratie peste valorile dict
    print('Dict values:', element)

for element in my_dict.items():  # iteratie peste tot dict, atat chei cat si valori, devine un tuple iar tuple-ul spre deosebire de liste nu poate fi modificat
    print('Dict tuple:', element)

for key, value in my_dict.items():  # iteratie peste tot dict, atat chei cat si valori, care nu este tuple
    print('Dict tuple:', key, value)

#get key/value
value = my_dict['one']  #trebuie pusa cheia de la care vreau sa iau valoarea
print('returned value:', value)
my_dict['one'] = '''one'''
value = my_dict['one']
print('returned value:', value)

# test = {[1]: 'test'}  #eroare fiindca lista ca si cheie nu poate sa fie. nu este hashable
# print(test)

#Tuple, se poate scrie si cu paranteze rotunde si fara

a, b = (1, 2)  #same as 1, 2! tuple cu un singur element este (1,) sau 1,
print(a)
print(b)

a, b = b, a
print(a)
print(b)
