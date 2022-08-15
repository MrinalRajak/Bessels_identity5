
#Bessel's identity
#(5) jn(n,x) = (1/π)*∫_(t=0)^π▒(cos⁡(xsin(t)-nt) )dt

import numpy as np
from scipy.special import jn
from scipy.integrate import quad
from scipy.misc import derivative

n=int(input("Enter the n: "))
x=float(input("Enter the x: "))
def f(t):
    return (1/np.pi)*(np.cos(x*np.sin(t)-n*t))

LHS=jn(n,x)
RHS=quad(f,0,np.pi)[0]

print("LHS: ",LHS)
print("RHS: ",RHS)
   
