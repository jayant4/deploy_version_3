import math
import streamlit as st
import scipy.stats

# sample size n
st.title("1 Sample T interval ")
n = st.number_input("Enter n value") #n=80
# sample mean x_bar
x_bar=st.number_input("Enter x_bar value : ") #50
x = st.number_input("Enter x value")  # 30

# Standard deviation sigma

sigma = st.number_input("Enter sigma value") #sigma=60

significance_level = st.number_input("Enter Significance level value")  # significance_level=0.05
# degree_of_freedom
degree_of_freedom=n-1

def calculate():
    t_critcal=scipy.stats.t.ppf(1-significance_level/2,degree_of_freedom)

    confidence_interval_minus,confidence_interval_plus=x_bar-t_critcal*sigma/math.sqrt(n),x_bar+t_critcal*sigma/math.sqrt(n)
    st.write((confidence_interval_minus,confidence_interval_plus))

    st.write(f"lower bound : {confidence_interval_minus}")
    st.write(f"upper bound : {confidence_interval_plus}")

if (st.button("calculate")):

    calculate()