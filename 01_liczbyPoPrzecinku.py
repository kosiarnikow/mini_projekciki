import math

wartosc_pi = math.pi

i = input("podaj liczbe, miejsc po przecinku: ")

if i < 20:
    x2 = round(wartosc_pi,int(i))
    print(x2)
else:
    print("podane i jest za duze")