#brute force algorithm for root finding

import numpy as np

def f(x): #implement equation we wish to solve here (if for example x² = 9, then x²-9=0, and then solve f(x) = x² -9 where f(x)=0)
    return x**2-9

def brf(func,a,b,n):
    #create the points 
    xvals = np.linspace(a,b,num=n)
    
    #create the yvals
    yvals = func(xvals)
        
    #go through the brute force find roots
    for i in range(len(xvals)-1):
        if yvals[i+1]*yvals[i]<0:
            root = xvals[i]-((xvals[i+1]-xvals[i])/(yvals[i+1]-yvals[i]))*yvals[i]
            return root 
        
  
             
x=brf(f,0,1000,100000)    
print(x)