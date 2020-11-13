#define test function
def f(x):
	return x**2

#single integral left sum 
def double_integral(func,a,b,n):
	dx = (b-a)/n
	A=0
	for i in range(n):
		xi = a+i*dx
		A=A+func(xi)*dx
	return A


#mid point sum. will converge faster
def mid_double_integral(func,a,b,n):
	dx = (b-a)/n
	A=0
	for i in range(n):
		xi = a+i*dx+0.5*dx
		A=A+func(xi)*dx
	return A



#check if works (verified against exact calculation)
#see how much faster midpoint sum converges 
print(double_integral(f,1,2,10))
print(mid_double_integral(f,1,2,10)) #only n=10 slices, midpoint much better 
