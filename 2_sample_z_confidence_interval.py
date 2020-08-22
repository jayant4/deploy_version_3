import math

import scipy.stats
import streamlit as st


st.title("2 Sample Z confidence Interval")

sigma1=st.number_input("Enter Sigma_1 Value")#50
sigma2=st.number_input("Enter Sigma_2 Value")#60
x1_bar=st.number_input("Enter x1_bar Value")#123.2
n1=st.number_input("Enter n1 Value")#58
n2=st.number_input("Enter n2 Value")#48
x2_bar=st.number_input("Enter x2_bar Value")#173

significance_level=st.number_input("Enter Significance_level")#0.05

def calculate():

    lhs=x1_bar-x2_bar
    rhs=(scipy.stats.norm.ppf(1-significance_level/2))*(math.sqrt((sigma1*sigma1)/n1+(sigma2*sigma2)/n2))

    confidence_level_minus,confidence_level_plus=lhs-rhs,lhs+rhs
    st.write(confidence_level_minus,confidence_level_plus)
    st.write(f"Lower bound : {confidence_level_minus}")
    st.write(f"Upper bound : {confidence_level_plus}")

if (st.button("calculate")):
        calculate()