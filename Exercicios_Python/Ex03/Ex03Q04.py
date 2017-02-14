def ordemCrescente(a,b,c):
    if(a<b)and(a<c)and (b<c):
        primeiro =a
        segundo=b
        terceiro=c
    elif a>b and a<c:
        segundo = a
        terceiro = b
        primeiro=c

    elif a>b and a>c and b>c:
        terceiro=a
        primeiro=c
        segundo=b



