#exceptions

try:
    # raise NotImplemented("This is a test") #raise ne permite sa generam o eroare
    # print(result)
    # result = 1/0
    # print(result)
    pass  #nu facem nici o actiune
except ZeroDivisionError:  #doar eroarea de zero division o sa se printuie
    print('zero division error was visible')
except NameError:
    print("name error was visible")
# except BaseException:  #e ca si cum as pune doar except, ia in considerare toate exceptiile
#     print("all exceptions")
except Exception:
    print("some unexpected error was visible")
else:
    print("Everything executed successfully")
finally:
    print("This will always get printed")
