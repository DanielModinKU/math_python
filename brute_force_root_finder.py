#brute force algorithm for root finding

import numpy as np
import seaborn as sb 

def f(x): 
    return np.sin(x)

def brf(func,a,b,n):
    #create the points 
    xvals = np.linspace(a,b,num=n)
    
    #create the yvals
    yvals = func(xvals)
    
    sb.scatterplot(x=xvals,y=yvals)
    
    #go through the brute force find roots
    for i in range(len(xvals)-1):
        if yvals[i+1]*yvals[i]<0:
            root = xvals[i]-((xvals[i+1]-xvals[i])/(yvals[i+1]-yvals[i]))*yvals[i]
            return root 
        
  
            
    
#brute force root finder 
    