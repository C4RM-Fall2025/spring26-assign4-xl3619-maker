def getBondPrice_Z(y, face, couponRate, m):
  pvcfsum = 0
  cf = couponRate * face
  for t in range(1, (m) +1):
    pV = (1 +y )**-t)
    pvcf = pv*cf
    #pvcfsum = pvcfsum +pvcf
    pvcfsum += pvcf
  bondprice = pvcfsum + pv*face
  return(bondprice)
