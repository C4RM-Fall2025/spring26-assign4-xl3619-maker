def getBondPrice_Z(face, couponRate, times, yc):
    coupon = face * couponRate
    bondPrice = 0.0

    for i, (y, t) in enumerate(zip(yc, times)):
        if i == len(times) - 1:
            cf = coupon + face          
        else:
            cf = coupon                

        pv = cf / ((1 + y) ** t)
        bondPrice += pv

    return bondPrice
