suma_iloczynow = 0
with open('day2-1', 'r') as myfile:
    for line in myfile:
        game = line.split(':')
        game[0] = game[0].replace('Game ','')
        wyniki = game[1].split(';')
        print("=============================================================")
        gameno = int(game[0])
        print(f"gameno: {gameno}")
        game = {"gameno": [], "red": [], "green": [], "blue": []}
        game["gameno"].append(gameno)
        for wynik in wyniki:
            draws = wynik.split(",")
            print("+-----------------------------------------")
            print(f"draws: {draws}")
            for draw in range(0, len(draws)):
#                print(f"draws[{draw}]: {draws[draw]}")
                x = draws[draw].replace('\n','').strip().split(" ")
                liczba  = int(x[0])
                kolor   = x[1]
                if kolor == 'red':
                    game["red"].append(liczba)
                if kolor == 'green':
                    game["green"].append(liczba)
                if kolor == 'blue':
                    game["blue"].append(liczba)
#                print(f"liczba: {liczba}, kolor {kolor}")
        print(f"Gameno: {game['gameno']}, red: {game['red']}, green: {game['green']}, blue: {game['blue']}")
        print(f"Gameno: {game['gameno']}, red: {max(game['red'])}, green: {max(game['green'])}, blue: {max(game['blue'])}")
        mred = max(game['red'])
        mgreen = max(game['green'])
        mblue = max(game['blue'])
        msum = mred * mgreen * mblue
        suma_iloczynow += msum
print(f"Suma kwadratów gier: {suma_iloczynow}")
