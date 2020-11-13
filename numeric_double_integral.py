#program to calculate double integrals numerically 

#define test function
def f(x,y):
	return x**2+y**2

#create double integral function using left sum 
#( not as numerically efficient as mid sum etc, but will do for now) 
def double_integral(func,a,b,c,d,n):
	dx = (b-a)/n
	dy = (d-c)/n
	V=0
	for p in range(n):
		yp = c+p*dy
		A=0
		for i in range(n):
			xi = a+i*dx
			A=A+func(xi,yp)*dx
		V=V+A*dy
	return V

#mid point sum. will converge faster
def mid_double_integral(func,a,b,c,d,n):
	dx = (b-a)/n
	dy = (d-c)/n
	V=0
	for p in range(n):
		yp = c+p*dy+0.5*dy
		A=0
		for i in range(n):
			xi = a+i*dx+0.5*dx
			A=A+func(xi,yp)*dx
		V=V+A*dy
	return V



#check if works (verified against exact calculation)
#see how much faster midpoint sum converges 
print(double_integral(f,1,2,1,2,10))
print(mid_double_integral(f,1,2,1,2,10)) #only n=10 slices, midpoint much better 


	
	