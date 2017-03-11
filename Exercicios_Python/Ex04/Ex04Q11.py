def tempo():

    popCidadeA=5000000
    iA = 0.03
    popCidadeB=7000000
    iB = 0.02
    contadorTempo =1

    mA = popCidadeA*(1+(iA*contadorTempo))
    mB = popCidadeB*(1+(iB*contadorTempo))

    while(mA<mB):
        contadorTempo =1+contadorTempo
        mA = popCidadeA*(1+(iA*contadorTempo))
        mB = popCidadeB*(1+(iB*contadorTempo))

    print(str(contadorTempo+1) +' anos')

tempo()



