games = []
with open('day2-1', 'r') as myfile:
    for line in myfile:
        game = line.split(':')
        game[0] = game[0].replace('Game ','')
        wyniki = game[1].split(';')
        print("=============================================================")
        gameno = game[0]
        print(f"gameno: {gameno}")
        mydraw = {"game":[],"red":[],"green":[],"blue":[]}
        mydraw["game"].append(gameno)
        for wynik in wyniki:
            draw = wynik.split(",")
            print("+-----------------------------------------")
            print(f"draw: {draw}")
            for b in range(0, len(draw)):
                print(f"draw[{b}]: {draw[b]}")
                x = draw[b].replace('\n','').strip().split(" ")
                liczba  = x[0]
                kolor   = x[1]
                if kolor == 'red' and liczba is not None:
                    red = liczba
                else:
                    red = 0
                if kolor == 'green' and liczba is not None:
                    green = liczba
                else:
                    green = 0
                if kolor == 'blue' and liczba is not None:
                    blue = liczba
                else:
                    blue = 0
                print(f"liczba: {liczba}, kolor {kolor}")
                print(f"red: {red} blue: {blue} green: {green}")

#                print(f"mydraw: {mydraw}")
            games.append(mydraw)
        print(f"mydraw: {mydraw}")
        red     = False
        green   = False
        blue    = False
#print(games)

