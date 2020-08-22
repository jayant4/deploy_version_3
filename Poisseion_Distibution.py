from  scipy import stats
import scipy
import streamlit as st

st.title('Calculate Poisson Distribution')

p = float((st.number_input("   Enter Average rate of success p  : ")) ) # 0.5
x = float(st.number_input("   Enter Poisson random variable (x)	: "))  # 10

if (st.button("calculate")):
    st.write(f"""
    Poisson Probability: P(X = x)	 : {scipy.stats.distributions.poisson.pmf(x, p)}\n
    Cumulative Probability: P(X < x) : {scipy.stats.distributions.poisson.cdf(x, p)-scipy.stats.distributions.poisson.pmf(x, p)}\n
    Cumulative Probability: P(X <= x): {scipy.stats.distributions.poisson.cdf(x, p)}\n
    Poisson Probability: P(X > x)	 : {scipy.stats.distributions.poisson.sf(x, p)}\n
    Poisson Probability: P(X >= x)	 : {scipy.stats.distributions.poisson.sf(x, p)+scipy.stats.distributions.poisson.pmf(x, p)}\n
     """)