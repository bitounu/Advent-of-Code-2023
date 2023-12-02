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

with open('day1-2', 'r') as myfile:
    for line in myfile:
        print("------------------------")
        print(line)
        for i in range(0, len(line)):
            raz     = line[i:i+1]
            trzy    = line[i:i+3]
            cztery  = line[i:i+4]
            piec    = line[i:i+5]
            try:
                a = int(raz)
                poczatek.append(int(raz))
                print(raz)
                break
            except:
                pass
            if trzy in list(cyfry.keys())[:3]:
                cyfra = int(cyfry[trzy])
                poczatek.append(cyfra)
                print(cyfra)
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
