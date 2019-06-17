def CoverWithTiles(len):
    if len % 2 == 1 or len <= 0:
        return - 1
    if len == 2 :
        return 3
    elif len == 4 :
        return 11
    else:
        return 4 * CoverWithTiles(len - 2) - CoverWithTiles(len - 4)