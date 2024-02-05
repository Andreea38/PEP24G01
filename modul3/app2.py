number = int(input('Give number: '))
print(range(0, number, 2))
print(type(range(number)))

#for syntax
for count in range(0, number + 1, 2):  #functia range(start,stop,step)
    print(count)

print(f'Last value: {count}')  #can be undefined
