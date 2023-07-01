"""4.Напишете програма која ќе прочита два броја од корисникот 
и ќе го испечати збирот на броевите помеѓу нив што се делливи со 4."""



x =int(input ("Vnesete broj: "))
y = int(input  ("Vnesete uste eden broj: "))
zbir = x + y
print(f"{x} + {y} = {zbir}")
if zbir % 4 == 0:
    print(f"Zbirot na broevite {x} i {y} e delliv so '4'. ")
else:
    print(f"Zbirot na broevite {x} i {y} ne e delliv so '4'. ")


