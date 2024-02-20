numar_participanti = int(input("Cati participanti avem la sondaj? "))
ages = []
for participant in range (1, numar_participanti+1):
    try:
        varsta = int(input(f"Introduceti varsta participantului {participant}: "))
    except ValueError:
        varsta = int(input(f"Nu ati introdus un format valid la participantul {participant}"))
    ages.append(varsta)
def average(list_of_numbers):
    total = 0
    for age in list_of_numbers:
        total +=age
    averange_age = total / len(list_of_numbers)
    return averange_age

print(average(ages))

