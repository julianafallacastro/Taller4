contador=int(0)
dividendo=int(input("Ingrese el dividendo: "))
divisor=int(input("Ingrese el divisor: "))
dividendo=dividendo-divisor
while(dividendo>=0):
    contador=contador+1
    dividendo=dividendo-divisor
print("la división es igual a:"+str(contador))