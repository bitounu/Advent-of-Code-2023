gsum = 0;
poczatek = []
koniec = []
cyfry = {
        "one":      1,
        "two":      2,
        "six":      6,
        "four":     4,
        "five":     5,
        "nine":     9,
        "three":    3,
        "seven":    7,
        "eight":    8
        }
def rev(l):
    return l[::-1]
with open('day1-2', 'r') as myfile:
    for line in myfile:
        print("------------------------")
        print(f"normal:   {line.rstrip()}")
        rline = line[::-1].strip()
        print(f"reversed: {rline}")
        for i in range(0, len(line)):
            raz     = line[i:i+1]
            trzy    = line[i:i+3]
            cztery  = line[i:i+4]
            piec    = line[i:i+5]
            try:
                a = int(raz)
                poczatek.append(raz)
#                print(raz)
                break
            except:
                pass
            if trzy in list(cyfry.keys())[:3]:
                poczatek.append(cyfry[trzy])
                break
            if cztery in list(cyfry.keys())[3:6]:
                poczatek.append(cyfry[cztery])
                break
            if piec in list(cyfry.keys())[6:9]:
                poczatek.append(cyfry[piec])
                break

        for i in range(0, len(rline)):
            raz2     = rline[i:i+1]
            trzy2    = rline[i:i+3]
            cztery2  = rline[i:i+4]
            piec2    = rline[i:i+5]
#            print(f"trojki: {list(cyfry.keys())[:3]}")
#            print(f"revtrojki: {list(map(rev, list(cyfry.keys())[:3]))}")
#            print(f"czworki: {list(cyfry.keys())[3:6]}")
#            print(f"revczworki: {list(map(rev, list(cyfry.keys())[3:6]))}")
#            print(f"piatki: {list(cyfry.keys())[6:9]}")
#            print(f"revpiatki: {list(map(rev, list(cyfry.keys())[6:9]))}")
            try:
                a = int(raz2)
                koniec.append(raz2)
                break
            except:
                pass
            if trzy2 in list(map(rev, list(cyfry.keys())[:3])):
                koniec.append( cyfry[trzy2[::-1]] )
                break
            if cztery2 in list(map(rev, list(cyfry.keys())[3:6])):
                koniec.append( cyfry[cztery2[::-1]] )
                break
            if piec2 in list(map(rev, list(cyfry.keys())[6:9])):
                koniec.append( cyfry[piec2[::-1]] )
                break
print(f"poczatek: {poczatek}")
print(f"koniec: {koniec}")
suma = 0
for i in range(0, len(poczatek)):
    liczba = str(poczatek[i])+str(koniec[i])
    print(f"liczba: {liczba}")
    suma += int(liczba)
print(f"{suma}")
