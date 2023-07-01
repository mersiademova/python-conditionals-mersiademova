"""2.Напишете програма која ќе прочита број од корисникот и ќе го провери дали тој е деллив со 3, 5, 3 и 5,
а потоа ќе испечати соодветната порака."""


x = int(input("Vnesete broj: "))
if x % 3 == 0 and x % 5 == 0:
    print(f"Brojot {x} e delliv so broevite 5 i 3.")
if x % 5 == 0 and x % 3 != 0:
    print(f"Brojot {x} e delliv so 5, no ne e delliv so 3.")
elif x % 3 == 0 and x % 5 != 0:
    print(f"Brojot {x} e delliv so 3, no ne e delliv so 5.")
else:
    print(f"Brojot {x} ne e delliv so 3 i 5.")
    