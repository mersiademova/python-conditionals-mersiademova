"""БОНУС

Да се напише програма која ќе прочита година од корисникот и да одреди дали е годината престапна
(разгледајте и размислете како може да се креира вакво нешто)"""




def prestapna(godina):
    return (godina % 4 == 0 and godina % 100 != 0) or godina % 400 == 0
godina = int(input("Vnesete godina na ragjanje: "))
if prestapna(godina):
    print("Vie ste rodeni vo prestapna godina.")
else:
    print("Vie ste rodeni vo neprestapna godina.")