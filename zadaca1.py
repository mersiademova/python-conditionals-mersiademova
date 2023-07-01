"""1.Напишете програма која ќе прочита два броја од корисникот и ќе го испечати збирот, разликата, 
производот и количникот на двата броја.
Споредете кој резултат е поголем, збирот или производот"""
x =int(input ("Vnesete broj: "))
y = int(input  ("Vnesete uste eden broj: "))
zbir = x + y
razlika = x - y
proizvod = x * y
kolicnik = x / y
print(f"{x} + {y} = {zbir}")
print(f"{x} - {y} = {razlika}")
print(f"{x} * {y} = {proizvod}")
print(f"{x} / {y} = {kolicnik}")
if zbir > proizvod:
    print("Zbirot na vnesenite broevi e pogolem od nivniot proizvod.")
else:
    print("Zbirot na vnesenite broevi ne e pogolem od nivniot proizvod.")

