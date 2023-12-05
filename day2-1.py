suma_gier = 0
# 12 red cubes, 13 green cubes, and 14 blue cubes
R = 12
G = 13
B = 14
with open('day2-1', 'r') as myfile:
    for line in myfile:
        game = line.split(':')
        game[0] = game[0].replace('Game ','')
        wyniki = game[1].split(';')
        print("=============================================================")
        gameno = int(game[0])
        print(f"gameno: {gameno}")
        game = True
        for wynik in wyniki:
            draws = wynik.split(",")
            print("+-----------------------------------------")
            print(f"draws: {draws}")
            for draw in range(0, len(draws)):
                print(f"draws[{draw}]: {draws[draw]}")
                x = draws[draw].replace('\n','').strip().split(" ")
                liczba  = int(x[0])
                kolor   = x[1]
                print(f"liczba: {liczba}, kolor {kolor}")
                if kolor == 'red':
                    if liczba > R:
                        game = False
                        break
                if kolor == 'green':
                    if liczba > G:
                        game = False
                        break
                if kolor == 'blue':
                    if liczba > B:
                        game = False
                        break
            print(f"Gra: {game}")
        if game:
            suma_gier += gameno
print(f"Suma gier: {suma_gier}")
