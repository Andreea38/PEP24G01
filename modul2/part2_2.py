#stringuri formatate

#method format
my_str = 'text {}'
print(my_str.format('''example'''))  # pentru un arg de pozitie

my_str = 'text {0} {0}'
print(my_str.format('example'))

my_str = 'text {1} {0}'
print(my_str.format('example1','example2')) #specificarea pozitiei

my_str = 'text {ex1} {ex2}'
print(my_str.format(ex1='example1',ex2='example2'))  #folosindu-ne de KW arguments

my_str = 'text {}'
print(my_str.format(2))  #pentru un obiect care poate fii transf intr=un string
print(80 * '#')
#formated string
ex1 = 'example1'
ex2 = 'example2'
print(f"Text1 {ex1}")
print(f"Text2 {ex2}")
print(f"Text2 {2}")
print(f"Text1 {ex2} si text2 {ex2}")

#len function
ex1 = 'example1'
print(len(ex1))

#index of string
hello = 'hello world'
print(hello[2])
print(hello[3:7]) #ultimul caracter nu se include in print
print(hello[0:10:2]) #ultimul arg este step-ul, din cate in cate carctere sa afiseze
print(hello[::2]) #incepe cu inceputul si termina cu sfarsitul
print(hello[::-1]) # se afiseara sirul invers.
print(hello[:len(hello):2])
print(hello[-5::])
print(hello[-5:0:1])