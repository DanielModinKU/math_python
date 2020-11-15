#now lets try to numerically solve a 1st order diff equation
import numpy as np
import seaborn as sb 

def df(N):
    r=0.1
    df=r*N
    return df

def dsolve(df,f0,t0,tlen,dt):
    xvals = [t0]
    yvals = [f0]
    while xvals[-1] < t0+tlen:
        y = yvals[-1] + df(yvals[-1])*dt
        x = xvals[-1]+dt
        yvals.append(y)
        xvals.append(x) 
    return (xvals,yvals)

plt = dsolve(df,1,0,20,0.0001)

sb.scatterplot(x=plt[0],y=plt[1])
  