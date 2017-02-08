def inversao(b):
    c=int(b/100)
    d=int((b%100)/10)
    u=(b%100)%10
    udc=int((u*100)+(d*10)+c)

    return udc


print(inversao(925))
