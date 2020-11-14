#monte carlo integration example code 
#monte carlo integration uses the mean value theorem.
#simply, an integral (in 1-d as example) can be approximated by the product of the AVERAGE function
#value over the integration domain [a,b] and the length of the integration interval (b-a) 
# int(f(x),x,a,b) = (b-a)*f_average 

import numpy as np
import seaborn as sb 

#test function 
def f(x):
    return x**2 

#monte carlo integration 1 dim
def m_carlo(func,a,b,n):
    #sample n random float i domain 0-1 (thats how numpy random works)
    rnd = np.random.random(size=n)
    #fit random numbers til integrationsinterval
    rnd = rnd*(b-a)+a 
    #evaluate function these values to get function values over the integration domain
    fvals = func(rnd)
    
    #calculate the integral using the mean value based approach
    I = (b-a)*fvals.mean() 
    
    return I 

#lets look at the errors at only n=100 
errors = []
for i in range(1000):
    errors.append(m_carlo(f,0,3,100))

sb.histplot(errors)