##this fin2 module is the same as the fin module, but does not display intro text upon importing

from math import exp, log, sqrt, pi

## define the Stock class
class Stock(object):
    
    def Capm(self, b, rm, rf):
        return rf + b*(rm - rf)

    def Sale(self, R, e, d, p, S, T, i, x, c):
        sale =  e*(1-d*R+R)**(T-1)*R*p
        profit = sale - S
        cgt = profit*c*x
        if profit > 0:
            return (sale - cgt)*exp(- i*T)
        else:
            return sale * exp(-i*T)
    
    def Div(self, R, e, d, T, i, x):
        return R*d*(1-x)*e*((1-d*R+R)**(T-1)*exp(-i*T)-(1-d*R+R)**-1)/(log(1-d*R+R)-i)

    def Val(self, R, e, d, p, S, T, i, x, c):
        return self.Div(R, e, d, T, i, x) + self.Sale(R, e, d, p, S, T, i, x, c)

## define the Option class
class Option(object):

    def _PDFNorm(self, x):
        return(1.0/((2*pi)**0.5))*exp(-0.5*x**2)

    def _CDFNorm(self, x):
        k=1.0/(1.0+0.2316419*x)
        k_sum=k*(0.319381530 + k*(-0.356563782 + k*(1.781477937 + k*(-1.821255978 + k*(1.330274429)))))
        if x>=0.0:
            return(1.0 - self._PDFNorm(x)*k_sum)
        else:
            return 1.0 - self._CDFNorm(-x)

    def _d1(self, S, K, r, v, T):
        return(log(S/K)+(r+0.5*v**2)*T)/(v*(T**0.5))

    def _d2(self, S, K, r, v, T):
        return(log(S/K)+(r-0.5*v**2)*T)/(v*(T**0.5))

    def _Nprime(self, x):
        return(1/(2*pi)**0.5)*exp(-x**2/2)

## define the Call sub-class
class Call(Option):
    
    def Price(self, S, K, r, v, T):
        return S*self._CDFNorm(self._d1(S, K, r, v, T))-K*exp(-r*T)*self._CDFNorm(self._d2(S, K, r, v, T))

    def Delta(self, S, K, r, v, T):
        return self._CDFNorm(self._d1(S, K, r, v, T))
    
    def Gamma(self, S, K, r, v, T):
        return self._Nprime (self._d1(S, K, r, v, T))/(S*v*T**0.5)

    def Theta(self, S, K, r, v, T):
        return ((-S*self._Nprime(self._d1(S, K, r, v, T))*v)/(2*T**0.5) - r*K*exp(-r*T)*self._CDFNorm(self._d2(S, K, r, v, T)))/365.0

    def Vega(self, S, K, r, v, T):
        return S*exp(-0*T)*T**0.5*self._Nprime(self._d1(S, K, r, v, T))/100.0
  
    def Rho(self, S, K, r, v, T):
        return K*T*exp(-r*T)*self._CDFNorm(self._d2(S, K, r, v, T))/100.0
    
## define the Put sub-class
class Put(Option):
    
    def Price(self, S, K, r, v, T):
        return -S*self._CDFNorm(-self._d1(S, K, r, v, T))+K*exp(-r*T)*self._CDFNorm(-self._d2(S, K, r, v, T))

    def Delta(self, S, K, r, v, T):
        return self._CDFNorm(self._d1(S, K, r, v, T))-1
    
    def Gamma(self, S, K, r, v, T):
        return self._Nprime (self._d1(S, K, r, v, T))/(S*v*T**0.5)

    def Theta(self, S, K, r, v, T):
        return ((-S*self._Nprime(self._d1(S, K, r, v, T))*v)/(2*T**0.5) + r*K*exp(-r*T)*(1-self._CDFNorm(self._d2(S, K, r, v, T))))/365.0

    def Vega(self, S, K, r, v, T):
        return S*exp(-0*T)*T**0.5*self._Nprime(self._d1(S, K, r, v, T))/100.0
  
    def Rho(self, S, K, r, v, T):
        return -K*T*exp(-r*T)*(1-self._CDFNorm(self._d2(S, K, r, v, T)))/100.0
