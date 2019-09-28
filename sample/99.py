x = range(1, 10)
y = range(1, 10)

for i in x:
    line = ''
    for j in y:
        # line += '%s x %s = %2s  ' % (i, j, i*j) # old fashioned
        line += '{} x {} = {:2d} '.format(i, j, i*j)
    print(line)
