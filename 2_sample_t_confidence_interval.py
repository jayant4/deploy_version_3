import math
import scipy.stats
import streamlit as st

st.title("2 Sample T Confidence Interval")

sigma1=st.number_input("Enter Sigma_1 Value") #sigma1=50
sigma2=st.number_input("Enter Sigma_2 Value") #sigma2=60
x1_bar=st.number_input("Enter x1_bar Value") #x1bar=123.2
n1=st.number_input("Enter n1 Value") #n1=58
n2=st.number_input("Enter n2 Value") #n2=48
x2_bar=st.number_input("Enter x2_bar Value") #x2bar=173

significance_level=st.number_input("Enter Significance_level") #0.05

def degree_of_freedom(s1,s2,n1,n2):
    op_numerator=(((s1*s1)/n1)+((s2*s2)/n2))**2
    # print(op_numerator)
    op_denom=((1/(n1-1))*((s1*s1)/n1)**2)+((1/(n2-1))*((s2*s2)/n2)**2)
    return(op_numerator/op_denom)
def calculate():
    lhs=x1_bar-x2_bar
    dof=degree_of_freedom(sigma1,sigma2,n1,n2)
    rhs=(scipy.stats.t.ppf(1-significance_level/2,dof))*(math.sqrt((sigma1*sigma1)/n1+(sigma2*sigma2)/n2))
    confidence_level_minus,confidence_level_plus=lhs-rhs,lhs+rhs
    st.write(confidence_level_minus,confidence_level_plus)
    st.write(f"Lower bound : {confidence_level_minus}")
    st.write(f"Upper bound : {confidence_level_plus}")
if (st.button("calculate")):
        calculate()
