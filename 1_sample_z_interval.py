import math
import scipy.stats
import numpy as np
import scipy.special as scsp
import streamlit as st

st.title("1 Sample Z interval ")
n = st.number_input("Enter n value") #n=80
# sample mean x_bar

x_bar = st.number_input("Enter x bar value")  # 30

# Standard deviation sigma

sigma = st.number_input("Enter sigma value") #sigma=40

significance_level = st.number_input("Enter Significance level value")  # significance_level=0.5
def calculate():

    z_critical = ((-(scipy.stats.norm.ppf(1 - significance_level / 2))))
    # Confidence interval
    c_i_minus,c_i_plus=x_bar-z_critical*((sigma)/(math.sqrt(n))),x_bar+z_critical*((sigma)/(math.sqrt(n)))
    st.write(c_i_plus,c_i_minus)
    st.write(f"lower bound {c_i_plus}")
    st.write(f"upper bound {c_i_minus}")

if (st.button("calculate")):
    calculate()