#motne carlo integration in 2D over a domain which is NOT a rectangle (a-b domain in x, c-d domain in y) 
#frequent problem, not straightforwards. can be done with moete carlo integration 

import numpy as np
import seaborn as sb 
import plotext.plot as plt

def f(x,y): #test function 
    return x**2+y**2

def f2(x,y):
    return 5 #test function two - will create a plane z=5, so it is easy to calculate true volume by hand

def g(x,y): #funktion der beskriver domæne i  xy-plan (returnerer 1 hvis punkt (x,y) i domæne, -1 hvis ikke)
    #domæne eksempel her: x^2 + y^2 = 4 (cirkel i xy centrum med radius 2)
    if x**2+y**2 <= 4:
        return True  #dette er hvis givet (x,y) punkt er i domænet 
    else: 
        return False

def mc(func,g,x0,x1,y0,y1,n):
    #first use monte carlo to find approximate area of box (throw darts method using g points embedded in rectangle specified)
    
    #draw random points within box x0,x1,y0,y1 (make sure g is contained in box!)
    xvals = np.random.random(size=n)*(x1-x0)+x0
    yvals = np.random.random(size=n)*(y1-y0)+y0
    #zip into points 
    points = list(zip(xvals,yvals)) 
    
    #now check how many points are inside the domain to estimate the area size in the rectangle
    inside_g = [g(*point) for point in points]
    
    #gives 1 and 0, so the mean is the proportion inside the domain
    inside_g = sum(inside_g)/len(inside_g)

    #now use that proportion to calculate area of domain as prorpotion of rectangle area:
    Ag = inside_g*(x1-x0)*(y1-y0)
    
    #now extract points inside g domain to calculate function values for those points
    g_points = [point for point in points if g(*point)]
    
    #take mean of function values evaluated over points in g
    f_vals = [func(*point) for point in g_points]
    mean_f_vals = sum(f_vals)/len(f_vals)
    
    #calculate vol
    V = mean_f_vals*Ag
    
    return V 
    
u = mc(f2,g,-3,3,-3,3,10000) #make sure the box can contain the entire domain g! 
print(u)
#sb.scatterplot(x=u[0],y=u[1])
    
    