def stairs(n):

    line = 1

    for i in range(n):
        whitespace_len = n - line
        whitespace = ' ' * whitespace_len

        drawer = '*' * line # (line  * 2) to draw triangle
        
        # triangle
        #drawer = drawer[:-1]

        print(whitespace + drawer)

        line += 1

stairs(6)