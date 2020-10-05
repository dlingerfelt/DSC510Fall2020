def get_total_distance(pings):
    """
    Determines the total distance covered by the pings.
    """
    # TODO: implement
    length = len(pings)
    total = 0
    # adding the positions to the distance formula and adding all of those distances returning
    # distance formula = sqrt((x2-x1)^2 + (y2-y1)^2)
    for x in pings:
        for y in range(1, length):
            total += ((pings[y].position.get_x() - pings[x].position.x.get_x()) ** 2 + (pings[y].position.y.get_y() - pings[x].position.y.get_y()) ** 2)**(1/2)
    return total
