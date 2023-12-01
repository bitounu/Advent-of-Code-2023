lsum = '';
gsum = 0;
with open('day1-1', 'r') as myfile:
    for line in myfile:
        for i in range(0, len(line)):
            try:
                a = int(line[i])
                lsum += line[i]
            except:
                pass
        lsum = lsum[:1]+lsum[-1:]
        lsum = int(lsum)
        gsum += lsum
        lsum = ''
print(gsum)
