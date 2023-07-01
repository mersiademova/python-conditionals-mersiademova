"""5.Напишете програма која ќе прочита два броја од корисникот и ќе го испечати производот на броевите,
да се провери дали резултатот е парен или не парен."""



x =int(input ("Vnesete broj: "))
y = int(input  ("Vnesete uste eden broj: "))
proizvod = x * y
print(f"{x} * {y} = {proizvod}")
if (x * y) % 2 == 0:
    print(f"Proizvodot na {x} i {y} e paren broj.")
else:
    print(f"Proizvodot na {x} i {y} e neparen broj.")
