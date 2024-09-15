import numpy as np
from scipy import stats
import math



class pricer :
        def __init__(self,S,K,sig, T,r) :
            self.S = S
            self.K = K
            self.sig = sig
            self.T = T
            self.r = r
            self.d_1 = (math. log(self.S/self.K) + (self.r - self.sig**2/2)*self.T)/(self.sig*self.T**0.5)
            self.d_2 = (math. log(self.S/self.K) + (self.r - self.sig**2/2)*self.T)/(self.sig*self.T**0.5) - self.sig*self.T**0.5

        def call(self) :
            call = self.S*stats.norm.cdf(self.d_1) - self.K*math.exp(-self.r*self.T)*stats.norm.cdf(self.d_2)
            return call

        def put(self) :
            return self.S*math.exp(-self.r*self.T)*stats.norm.cdf(-self.d_2) - self.S*stats.norm.cdf(-self.d_1)

        def delta_call(self) :
            return stats.norm.cdf(self.d_1)

        def delta_put(self) :
            return stats.norm.cdf(self.d_1)-1

        def gamma(self) : 
            gamma = stats.norm.pdf(self.d_1)/(self.S*self.sig*(self.T)**0.5)
            return gamma

        def vega(self) : 
            return stats.norm.pdf(self.d_1)*self.S*(self.T)**0.5
        
            