#function to calcualte height of ball
import seaborn as sb 

def diffx(f,x,dx,**kwargs):   
    df = f(x+dx,**kwargs)-f(x,**kwargs) 
    #print(df)
    dfdx = df/dx
    return dfdx 

def fheight(t,v0,s0,neg=False):
    h = v0*t-0.5*9.82*t**2
    if neg==True:
        return -h
    else:
        return h 

def max_height(init,alpha,epoch): #numerical optimization here 
    for i in range(epoch):
        dydx = diffx(fheight,init,0.00001,v0=10,s0=0,neg=True)
        if dydx<0:
            init = init + alpha
        if dydx>0: 
            init = init - alpha 
        y = -fheight(init,v0=10,s0=0,neg=True)
        x = init 
    return x,y
    

print(max_height(-100,0.1,1000000))
    