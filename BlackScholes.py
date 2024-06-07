import numpy as np
import scipy.stats as st

def BlackScholes(s0,r,T,k,sigma):
    log_term=np.log(s0/k)
    rate_sigma_term=(r+(0.5)*(sigma**2))*T
    d1=(log_term+rate_sigma_term)/(sigma*np.sqrt(T))
    d2=d1-(sigma*np.sqrt(T))
    C=(s0*st.norm.cdf(d1))-(k*np.exp(-1*r*T)*st.norm.cdf(d2))
    P=(k*np.exp(-1*r*T)*st.norm.cdf(-d2))-(s0*st.norm.cdf(-d1))
    return f"Call option = {C}, Put option = {P}"
