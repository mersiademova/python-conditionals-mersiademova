"""6.Напишете програма која ќе прочита страни на правоаголник и квадрат,
да се пресмета плоштината и да се провери дали збирот на плоштините е деллив со 2,3 или 5"""



a = int(input("Vnesete ja dolzinata na pravoagolnikot: "))
b = int(input("Vnesete ja sirinata na pravoagolnikot: "))
PP = a*b
print(f"Plostinata na pravoagolnikot e {PP}cm^2 ")
c = int(input("Vnesete ja dolzinata na stranata na kvadratot: "))
PK = c*c
print(f"Plostinata na kvadratot e {PK}cm^2 ")
ZP = PP + PK
print(f"Zbirot na plostinite e {ZP}")
if ZP % 5 == 0:
    print("Zbirot na plostinite e delliv so 5.")
if ZP % 3 == 0:
    print("Zbirot na plostinite e delliv so 3.")
if ZP % 2 == 0:
    print("Zbirot na plostinite e delliv so 2.")    
else:
    print("Zbirot na plostinitene ne e delliv sobroevite 5, 3 i 2.")
