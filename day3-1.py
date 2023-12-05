# tablica ma 140 x 140
# n = obecna pozycja w postaci rzad,kolumna [r,k]; np. n = [8,6]
# trzeba sprawdzić czy polach jest (coś co nie jest kropką i cyfrą):
# [7,5] [7,6] [7,7]
# [8,5]       [8,7]
# [9,5] [9,6] [9,7]
# czyli:
# [r-1,k-1] [r-1,k] [r-1,k+1]
# [r,  k-1]         [r ,k+1]
# [r+1,k-1] [r+1,k] [r+1,k+1]
# edge case'y są w rogach oraz lewej i prawej krawędzi
# można zrobić tablicę "ruchów":
# rogi to:
# [1,1] [1,140] [140,1] [140,140]
# krawędzie to: [1-140,1] [140,1-140]

symbols = [ '#', '%', '&', '*', '+', '-', '/', '=', '@', '$']
with open('day3-1', 'r') as myfile:
    for line in myfile:
        game = line.split(':')
        game[0] = game[0].replace('Game ','')
        wyniki = game[1].split(';')
