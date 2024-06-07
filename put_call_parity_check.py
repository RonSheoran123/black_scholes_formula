def put_call_parity_check(C,P,s0,r,T,k):
    return round(C-P,4)==round(s0-(k*np.exp(-1*r*T)),4)
