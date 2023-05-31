def fibonnacci(n):
    if n <= 0:
        print(0)
    elif n == 1:
        print(1)
    else:
        ciag = [0,1]
        while len(ciag) < n:
            nastepna_liczba = ciag[-1] + ciag[-2]
            ciag.append(nastepna_liczba)
        return ciag

ilosc = input("podal ilosc elementu ciagu: ")
wynik = fibonnacci(int(ilosc))

print(wynik)