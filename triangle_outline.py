def triangle(n):
    line = 1

    for column in range(n):
        whitespace_len = n - line
        whitespace = ' ' * whitespace_len

        drawer = '*' * (line*2)
        drawer = drawer[:-1]
        drawer = list(drawer)
        
        drawer_idx = 0
        for j in drawer:
            if column != n-1:
                if drawer_idx == 0 or drawer_idx == len(drawer)-1:
                    drawer_idx += 1
                    continue
                else:
                    drawer[drawer_idx] = ' '
                drawer_idx += 1

        drawer = ''.join(drawer)

        print(whitespace + drawer)

        line += 1


triangle(10)