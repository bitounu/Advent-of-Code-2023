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
# >>> x = map(rev,list(cyfry.keys())[6:9])
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
            raz2     = rline[i:i+1]
            trzy2    = rline[i:i+3]
            cztery2  = rline[i:i+4]
            piec2    = rline[i:i+5]
            try:
                a = int(raz)
                poczatek.append(int(raz))
                print(raz)
                a = int(raz2)
                koniec.append(int(raz2))
                print(raz2)
                break
            except:
                pass
            if trzy in list(cyfry.keys())[:3]:
                cyfra = int(cyfry[trzy])
                poczatek.append(cyfra)
                print(cyfra)
                break
            print(f"tu: {list(map(rev, list(cyfry.keys())[:3]))}")
            if trzy2 in list(map(rev, list(cyfry.keys())[:3])):
                cyfra = int(map(rev, cyfry[trzy2]))
                koniec.append(cyfra)
                print(f"r: {cyfra}")
                break
            if cztery in list(cyfry.keys())[3:6]:
                cyfra = int(cyfry[cztery])
                poczatek.append(cyfra)
                print(cyfra)
                break
            if piec in list(cyfry.keys())[6:9]:
                cyfra = int(cyfry[piec])
                poczatek.append(cyfra)
                print(cyfra)
                break
print(poczatek)
