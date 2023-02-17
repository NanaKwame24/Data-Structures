#https://github.com/NanaKwame24
import numpy as np
L=12 #m
w=10 #kN/m
#Question a
#bending moment(M) and shear forces(V) at the first end, x=0
x=0
M=(w*(-6*x**2+6*L*x-L**2))/12
V=w*(L/2-x)
u=' bending moment at x=0 is'
n=' shear force at x=0 is'
print()
print('(a.1)'+u+str(M)+'and'+ n+str(V))
#bending moment(M) and shear force(V) at the first end, x=L=10
x=L
M=(w*(-6*x**2+6*L*x-L**2))/12
V=w*(L/2-x)
a=' bending moment at x=L is'
b=' shear force at x=L is'
print()
print('(a.2)'+u+str(M)+'and',n+str(V))
#Question b
"""
the expression x**2-Lx+L**2/6=0 is obtained when the bending moment is zero
"""
#from the expression
a=1
b=-L
c=L**2/6
#using the almighty formula the two roots are;
discriminant=b**2-4*a*c
root_1b=(-b+np.sqrt(discriminant))/2*a
root_2b=(-b-np.sqrt(discriminant))/2*a
print()
print('(b) the points of contraflexure are {0} and {1}'.format(root_1b,root_2b))
#Question c 
"""
When shear force is zero, x=L/2
"""
x=L/2
print()
print('(c) the point at which V=0 is {}'.format(x))
#Question d
k=0
t=0.01
q=L+t
x=np.arange(k,q,t)
M=(w*(-6*x**2+6*L*x-L**2))/12
print()
print('(d) using the initialized variable,  bending moment at each step in the array is {0}'.format(M))
#Question e
V=w*(L/2-x)
print()
print('(e)  shear force for each step along the span is {}'.format(V))
#Question f
"""
let the absolute value of the bending moment array be AM
Also let the minimum AM be m_AM
"""
AM=abs(M)
m_AM=min(AM)
"""
When  bending moment is m_AM, the expression x**2-Lx+(L**2/6)+(2*m_AM)/w=0 is obtained
"""
#from the above expression
a=1
b=-L
c=(L**2/6)+(2*m_AM)/w
#using the almighty formula the two roots are;
discriminant=b**2-4*a*c
root_1f=(-b+np.sqrt(discriminant))/2*a
root_2f=(-b-np.sqrt(discriminant))/2*a
print()
print('(f) the points along L at which the absolute values of the bending moment array is minimum are {0} and {1}'.format(root_1f,root_2f))
#Question g
"""
let the relative errors be r_t
"""
r_t1=((root_1b-root_1f)/root_1b*100)                                                                                                                         
r_t2=((root_2f-root_2b)/root_2f*100)
print()
print('(g) the relative errors between estimated points of contraflexure are {0}% and {1}%'.format(r_t1,r_t2))
#question h 
"""
let  maximum bending moment be max_M and  minimum bending moment be min_M
"""
#for the maximum
max_M=max(M)
"""
when bending moment is max_M, the expression x**2-Lx+(L**2/6)+(2*max_M)/w=0 is obtained
"""
a=1
b=-L
c=(L**2/6)+(2*max_M)/w
#using the almighty formula the two roots are;
discriminant=b**2-4*a*c
root_1=(-b+np.sqrt(discriminant))/2*a
root_2=(-b-np.sqrt(discriminant))/2*a
print()
print('(h.1)the points at which the maximum bending moment occur are {0} and {1}'.format(root_1,root_2))
#for the minimum
min_M=min(M)
"""
when  bending moment is min_M, we get an expression x**2-Lx+(L**2//6)+(2*min_M)/w=0
"""
a=1
b=-L
c=(L**2//6)+(2*min_M)/w
#using the almighty formula the two roots are;
discriminant=b**2-4*a*c
root_1=(-b+np.sqrt(discriminant))/2*a
root_2=(-b-np.sqrt(discriminant))/2*a
print()
print('(h.2)the points at which the minimum bending moment occur are {0} and {1}'.format(root_1,root_2))
#https://github.com/NanaKwame24