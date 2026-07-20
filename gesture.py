def getCommand(points):

    if len(points) == 0:
        return "HOVER"

    tip = points[8]      # Index fingertip
    base = points[5]     # Index MCP

    x = tip[1]
    y = tip[2]

    if y < base[2] - 80:
        return "UP"

    if y > base[2] + 80:
        return "DOWN"

    if x < base[1] - 80:
        return "LEFT"

    if x > base[1] + 80:
        return "RIGHT"

    return "HOVER"