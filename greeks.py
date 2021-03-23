import math
import scipy.stats as sp

class EuropeanCall:

    ''' Inputs
    S: Stock Price
    v: Volatility
    X: Strike Price
    T: Time to maturity
    r: Risk free interest rate
    '''

    def __init__(self, S, v, X, T, r):
        self.S = S
        self.v = v
        self.X = X
        self.T = T
        self.r = r
        self.price = self.call_price(S, v, X, T, r)
        self.delta = self.call_delta(S, v, X, T, r)
        self.theta = self.call_theta(S, v, X, T, r)
        self.vega = self.call_vega(S, v, X, T, r)
        self.rho = self.call_rho(S, v, X, T, r)

    def call_price(self, S, v, X, T, r):
        b = math.exp(-r * T)
        d1 = (math.log(S / X) + (r + 0.5 * v**2) * T) / (v * math.sqrt(T))
        d2 = (math.log(S / X) + (r - 0.5 * v**2) * T) / (v * math.sqrt(T))
        N_d1 = sp.norm.cdf(d1)
        N_d2 = sp.norm.cdf(d2)
        x1 = S * N_d1
        x2 = X * b * N_d2
        return x1 - x2

    def call_delta(self, S, v, X, T, r):
        b = math.exp(-r * T)
        d1 = (math.log(S / X) + (r + 0.5 * v**2) * T) / (v * math.sqrt(T))
        N_d1 = sp.norm.cdf(d1)
        return N_d1

    def call_theta(self, S, v, X, T, r):
        b = math.exp(-r * T)
        d1 = (math.log(S / X) + (r + 0.5 * v**2) * T) / (v * math.sqrt(T))
        d2 = (math.log(S / X) + (r - 0.5 * v**2) * T) / (v * math.sqrt(T))
        N_d1 = sp.norm.cdf(d1)
        N_d2 = sp.norm.cdf(d2)
        dN_d1 = math.exp((-d1**2) / 2) / math.sqrt(2 * math.pi)
        x1 = (S * dN_d1 * v) / (2 * math.sqrt(T))
        x2 = r * X * math.exp(-r * T) * N_d2
        return -(-x1 - x2)

    def call_vega(self, S, v, X, T, r):
        b = math.exp(-r * T)
        d1 = (math.log(S / X) + (r + 0.5 * v**2) * T) / (v * math.sqrt(T))
        N_d1 = sp.norm.cdf(d1)
        dN_d1 = math.exp((-d1**2) / 2) / math.sqrt(2 * math.pi)
        x1 = S * dN_d1 * math.sqrt(T)
        return x1

    def call_rho(self, S, v, X, T, r):
        b = exp(-r * T)
        d1 = (math.log(S / X) + (r + 0.5 * v**2) * T) / (v * math.sqrt(T))
        d2 = (math.log(S / X) + (r - 0.5 * v**2) * T) / (v * math.sqrt(T))
        N_d1 = sp.norm.cdf(d1)
        N_d2 = sp.norm.cdf(d2)
        x1 = X * T * math.exp(-r * T) * N_d2
        return x1

price = EuropeanCall(S=100, v=0.5, X=150, T=20, r=.01).price
delta = EuropeanCall(S=100, v=0.5, X=150, T=20, r=.01).delta
theta = EuropeanCall(S=100, v=0.5, X=150, T=20, r=.01).theta
vega = EuropeanCall(S=100, v=0.5, X=150, T=20, r=.01).vega
rho = EuropeanCall(S=100, v=0.5, X=150, T=20, r=.01).rho

print(f"EUROPEAN CALL: \n - Price = {price} \n - Delta = {delta} \n - Theta = {theta} \n - Vega = {vega} \n - Rho = {rho}")
