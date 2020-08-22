import streamlit as st

import numpy as np
import scipy.special as scsp

st.title('P value from Z')


z_value_input=st.text_input(" Enter z value : ")


def main(z):
    """From z-score return p-value."""
    left=0.5 * (1 + scsp.erf(float(z) / np.sqrt(2)))
    right =1-left

    if float(z)<0:
        two_tailed=2*left
    else:
        two_tailed=2*right

    return (left,right,two_tailed)


if (st.button("calculate")):
  left,rigt,two_tail= main(z_value_input)
  st.write("left is ",left)
  st.write("right is ",rigt)
  st.write("two tail is ",two_tail)



print(main(-3.395))