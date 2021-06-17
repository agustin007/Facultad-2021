def funcion(C,T):
	return C+0.2*T


def euler(T0,C0,h,Iteraciones):

	t=0  #Tiempo inicial
	D0=0 #Condicion Inicial
	print('\n-----------SOLUCION-----------')
	print('------------------------------')    
	print('t\tD0\tPendiente\tDn')
	print('------------------------------')
	for i in range(Iteraciones):
		pendiente = funcion(C0,T0)
		Dn = D0+pendiente*h
		print('%.4f\t%.4f\t%0.4f\t%.4f'% (t,D0,pendiente,Dn))
		print('------------------------------')
		D0=Dn
		t+=h

print("Calculo por metodo de Euler")
cInicial= float(input("Ingrese la cantidad de autos que hay en la cola :"))
print('------------------------------')
cteT=float(input("Ingrese el valor de la constante T :"))
print('------------------------------')
step=float(input("Ingrese el valor de h : "))
pasos=int(input("Ingrese la cantidad de Iteraciones : "))
print('------------------------------')

euler(cteT,cInicial,step,pasos)







		