f, aux = 1, 1
numero=int(input("Ingrese un numero: "))
while f<=numero :
    factorial=0
    for i in range(f):

        factorial=factorial+aux

    aux=factorial
    f=f+1
print("El factorial de %d es %d " % (numero,factorial))