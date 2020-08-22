import math
import scipy.stats
import streamlit as st

st.title("Confidence Interval 1 Proportional")

n=st.number_input("Enter n Value")#70
x=st.number_input("Enter x Value")#30
significance_level=st.number_input("Enter Significance level")#0.05


def calculate():
    p_cap = x / n

    z = scipy.stats.norm.ppf(1 - significance_level / 2)

    confidance_interval_left,confidance_interval_right=p_cap-z*math.sqrt(p_cap*(1-p_cap)/n),p_cap+z*math.sqrt(p_cap*(1-p_cap)/n)

    st.write("Z value is : ", z )

    st.write("left  : ",confidance_interval_left)
    st.write("right : ",confidance_interval_right)

if (st.button("calculate")):
        calculate()