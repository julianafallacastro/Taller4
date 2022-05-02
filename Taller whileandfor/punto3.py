s=0
m=int(input("Ingrese el numero inicial"))
n=int(input("Ingrese el numero final"))
for i in range(m,n+1):
  if i%2==0:
     s+=i
print((s))
