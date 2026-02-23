def getBondDuration(y, face, couponRate, m, ppy=1):
    n = int(m * ppy)
    r = y / ppy
    coupon = face * couponRate / ppy

    bondPrice = 0
    numerator = 0

    for t in range(1, n + 1):
        cf = coupon
        if t == n:
            cf = cf + face

        pvcf = cf / ((1 + r) ** t)

        bondPrice = bondPrice + pvcf
        numerator = numerator + t * pvcf

    bondDuration = (numerator / bondPrice) / ppy
    return bondDuration
