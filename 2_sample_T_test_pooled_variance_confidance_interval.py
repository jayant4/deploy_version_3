import scipy.stats
import  math
import streamlit as st

st.title("2 Sample T Test Pooled Variance Confidence Interval")

s1=st.number_input("Enter s1 value")#50
s2=st.number_input("Enter s2 value")#60
x1_bar=st.number_input("Enter x1_bar value")#25
x2_bar=st.number_input("Enter x2_bar value")#124
n1=st.number_input("Enter n1 value")#24
n2=st.number_input("Enter n2 value")#25
significance_level = st.number_input("Enter Significance level value")  # 0.01

def calculate():
# ----------- Pooled Variance Start------------------

    s_p=(((n1-1)*(s1*s1))+((n2-1)*(s2*s2)))/(n1+n2-2)
    st.write(s_p)
    dof=n1+n2-2
    st.write(dof)

    # ----------- Pooled Variance End------------------

    #------confidence interval start----------
    lhs=x1_bar-x2_bar
    rhs=(scipy.stats.t.ppf(1-significance_level/2,dof))*(math.sqrt((s_p)*(1/n1+1/n2)))

    confidence_level_minus,confidence_level_plus=lhs-rhs,lhs+rhs
    st.write(confidence_level_minus,confidence_level_plus)
    st.write(f"Lower bound : {confidence_level_minus}")
    st.write(f"Upper bound : {confidence_level_plus}")

#------confidence interval end----------

if (st.button("calculate")):
    calculate()
