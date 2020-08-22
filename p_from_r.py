import math
from scipy import stats
import streamlit as st

st.title('P value from R')

r=st.text_input(" Enter R value : ")
N=st.text_input(" Enter N value : ")



def calculate(r,N):
    if   r<1 or N>6:
        if not N==2:
            t =r/math.sqrt((1-r*r)/(N-2))
            p=1 - stats.t.cdf(t,N-2)
            return(p,p*2)
        else:
            return "N value 2 not valid",""
    else:
        return "N should be greater than 6 or r less than 1",""

if (st.button("calculate")):
  p_one_tail,p_two_tail= (calculate(float(r),float(N)))

  if type(p_two_tail and p_one_tail)!=str:
    st.write("P value is  ",p_one_tail)


    st.write("two tail is ",p_two_tail)

  else:
      st.write(p_one_tail)

# print(calculate(0.1,4))