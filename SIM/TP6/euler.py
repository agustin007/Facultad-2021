def funcion(C,T):
	return C+0.2*T


def euler(T,C,h,D,step):
	t=0
	D0=0
	ti=0
	dD_dt=0

	for i in range(0,step):
		if i == 0:
			
			Dn=funcion(C,T)
			dD_dt= Dn*h
			
			print('\n-----------SOLUCION-----------')
			print('-------------------------------------------------')    
			print('t\tD0\tdD_dt\tDn\tti')
			print('-------------------------------------------------')
			print('%.4f\t%.4f\t%0.4f\t%.4f\t%.4f'% (t,D0,dD_dt,Dn,ti))
			print('-------------------------------------------------')
			D0=Dn
			t+=h
			ti+=t+h

		else:
			dD_dt=h*D0
			Dn = D0+h*D0
			print('%.4f\t%.4f\t%0.4f\t%.4f\t%.4f'% (t,D0,dD_dt,Dn,ti))
			print('-------------------------------------------------')
			D0=Dn
			t+=h
			ti+=h
		if D0>=D:
			print("En : ",round(t,3),", D :",D)
			break



print("Calculo por metodo de Euler")
cInicial= float(input("Ingrese la cantidad de autos que hay en la cola :"))
print('------------------------------')
cteT=float(input("Ingrese el valor de la constante T :"))
print('------------------------------')
auto=int(input("Auto grande(180) o el resto de los autos(130) :"))
print('------------------------------')
step=float(input("Ingrese el valor de h : "))
print('------------------------------')
pasos=int(input("Ingrese la cantidad de Iteraciones : "))
print('------------------------------')

euler(cteT,cInicial,step,auto,pasos)







		