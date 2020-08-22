import scipy.stats
import streamlit as st

import math


st.title("Confidence Interval 2 Proportion")

n1=st.number_input("Enter n1 Value") #230
n2=st.number_input("Enter n2 Value") #540
x1=st.number_input("Enter x1 Value") #100
x2=st.number_input("Enter x2 Value") #200
confidence_level = st.number_input("Enter Confidance level Value")  # 95


def calculate():
    # Sample proportion
    p1_hat = x1 / n1
    st.write("p1 hat : ", p1_hat)

    p2_hat = x2 / n2
    st.write("p2 hat : ", p2_hat)


    significance_level = 1 - (confidence_level) / 100

    z_critical_value = scipy.stats.norm.ppf(1 - significance_level / 2)

    lhs=p1_hat-p2_hat
    rhs=z_critical_value*math.sqrt((p1_hat*(1-p1_hat)/n1)+(p2_hat*(1-p2_hat)/n2))

    confidence_interval_lhs,confidence_interval_rhs=(lhs-rhs,lhs+rhs)
    st.write(confidence_interval_lhs," < p < ",confidence_interval_rhs)

if (st.button("calculate")):
        calculate()