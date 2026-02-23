def getBondPrice(y, face, couponRate, m, ppy=1):
    if ppy == 0:
        return face / (1 + y) ** m

    n = int(m * ppy)
    r = y / ppy
    coupon = face * couponRate / ppy

    bondPrice = 0

    for t in range(1, n + 1):
        bondPrice = bondPrice + coupon / ((1 + r) ** t)

    bondPrice = bondPrice + face / ((1 + r) ** n)

    
    return bondPrice
