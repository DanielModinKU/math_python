#triple integral

#test function af 3 variable
def f(x,y,z):
	return x*y*z 

#triple integral 
def trip(func,a,b,c,d,e,f,n):
	dx=(b-a)/n
	dy=(d-c)/n
	dz=(f-e)/n
	I = 0
	for j in range(n):
		for p in range(n):
			for i in range(n):
				xi = a+0.5*dx+i*dx
				yp = c+0.5*dy+p*dy
				zj = e+0.5*dz+j*dz
				I = I+func(xi,yp,zj)*dx*dy*dz 
	return I

#testing - problem is thought with higher order integrals 
#the number of iterations in the loops blow up so it gets very
#conmputationally heavy 
print(trip(f,1,2,1,2,1,2,100))
				