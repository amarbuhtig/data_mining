
# coding: utf-8

# In[20]:

from __future__ import division
from math import atan2, sin, cos


# In[42]:

class Ima():
    def __init__(self, re, im):
        self.re = re
        self.im = im
        
    def __repr__(self):
        if self.im>0:
            return "%r+%ri"%(self.re ,self.im)
        elif self.im<0:
            return "%r-%ri"%(self.re ,abs(self.im))
        else:
            return "%r" %(self.re)
    
    def __add__(self, other):
        if isinstance(other, Ima):
            return Ima(self.re+ other.re, self.im+ other.im)
        else:
            return self+Ima(other, 0)

    def __radd__(self, other):
        return self+other
          
    def __mul__(self, other):
        if isinstance(other, Ima):
            return Ima(self.re*other.re-self.im*other.im, self.re*other.im+self.im*other.re)
        else:
            return self*Ima(other, 0)
        
    def __rmul__(self, other):
        return self*other
    
    def __sub__(self, other):
        if isinstance(other, Ima):
            return Ima(self.re- other.re, self.im- other.im)
        else:
            return self-Ima(other, 0)

    def __rsub__(self, other):
        if isinstance(other, Ima):
            return other - self
        else:
            return Ima(other,0)-self
        
    def __neg__(self):
        return Ima(-self.re, -self.im)
        
    def __truediv__(self, other):               #__future__.division is active
        if other ==0:
            return "wrong"
        if isinstance(other, Ima):
            m = (self.im*other.re-self.re*other.im)/(other.re**2+other.im**2)
            return Ima((self.re*other.re+self.im*other.im)/(other.re**2+other.im**2) , m)
        else:
            return self/Ima(other, 0)
        
    def __rtruediv__(self, other):                 #__future__.division is active
        if isinstance(other, Ima):
            return other/self
        else:
            return Ima(other,0)/self
    
    def __abs__(self):
        return (self.re**2+ self.im**2)**(1/2)
        
    def rad(self):
        return atan2(self.im, self.re)
    
    def __pow__(self, other):
        abs_ = abs(self)
        ra = self.rad()
        return Ima(abs_**other*cos(ra*other), abs_**other*sin(ra*other) )       

