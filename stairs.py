def stairs(n):

    line = 1

    for i in range(n):
        drawer = '*' * line
        print(drawer)

        line += 1

stairs(6)