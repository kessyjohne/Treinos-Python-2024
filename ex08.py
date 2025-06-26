#altura=float(input("Digite sua altura:"))
#centimetros=int(altura*100)
#milimetros=int(altura*1000)
#print("Sua altura é {}".format(altura))
#print("Sua altura em centimetros é {} cm".format(centimetros))
#print("Sua altura em milimetros é {} mm".format(milimetros))

medida=int(input('Digite uma medida em METROS:'))
km=medida/1000
hm=medida/100
dam=medida/10
dm=medida*10
cm=medida*100
mm=medida*1000
print('Sua medida em Kilometros é {}, em hectometro {}, em decametros {}, em decimetro {}, em centimetro {}, e em milimetro {}'.format(km,hm,dam,dm,cm,mm))