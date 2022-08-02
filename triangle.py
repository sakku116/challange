def triangle(n):
    line = 1

    for i in range(n):
        whitespace_len = n - line
        whitespace = ' ' * whitespace_len

        drawer = '*' * (line*2)
        drawer = drawer[:-1]

        print(whitespace + drawer)

        line += 1


triangle(6)