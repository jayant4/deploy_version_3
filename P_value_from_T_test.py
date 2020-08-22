import numpy as  np
from scipy import stats

import streamlit as st
#
st.title('P value from T test')
#
# Calculate the t-statistics
t_test =st.number_input(" Enter T value : ")
# #0.408
# #Degrees of freedom
df =st.number_input(" Enter Degrees of Freedom : ")

pval=(stats.t.sf((t_test), df))
# print((1-pval)*2)
if (st.button("calculate")):
    st.write("Left Tail Test: ",pval)
    st.write("Right Tail Test: ", round(1-pval,7))
    st.write("Two Tail Test: ", round((1-pval)*2,7))