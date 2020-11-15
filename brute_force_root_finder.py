#brute force algorithm for root finding

import numpy as np

def f(x): 
    return np.sin(x)

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
        
  
            
    
#brute force root finder 
brf(f,0,5,1000)    