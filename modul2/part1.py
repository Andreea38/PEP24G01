str1 = 'hello world'  #exemplu de string
int1 = 100            #exemplu de integer
none = None           #obiect aparte None, este un cuvant cheie in py

#metode string
result = str1.capitalize()  #metoda care returneaza

print(type(result))  #type este o functie ca si print, ce ne returneaza tipul variabilei
print('Return type: ', type(result))  #type este o functie ca si print, ce ne returneaza tipul variabilei
print(type(str1))  #str
print(type(int1))  #int
print(type(none))  #NoneType

str1 = 'hello world {} {}'  # in primul {} o sa puna primul argument de la format, iar in al
                            # doilea {} o sa puna al doilea argument de la format si tot asa
result = str1.format('test','test2')  #metoda format primeste argumente de tip string
print('Formatted string: ', result)

str1 = 'hello world'
result = str1.center(30, '#')  #are ca argumente lungimea si caracterul de umplutura,
                                               # pune textul intre cele 30 de caractere si umple cu # ce trebuie umplute
result2 = str1.center(16, '#')
print('Centered string: ', result)
print('Centered string 2: ', result2)
