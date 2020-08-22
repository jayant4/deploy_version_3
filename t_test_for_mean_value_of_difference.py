import math
import scipy.stats
import numpy as np
import pandas as pd

import numpy as np
import streamlit as st


st.title("T Test for Mean Value of Difference")


x=(st.text_input(" Enter Sample values of x  separated by ' , ' example : '1,2,3' : "))
y=(st.text_input(" Enter Sample values of y separated by ' , ' example : '1,2,3' : "))
n=(st.text_input(" Enter number of rows : "))
ud=(st.text_input(" Enter u0 "))
difference = []
ho = st.selectbox(
            "Ho:  ud : ",
            ('==', '>=', '<='))  # "="input("Ho:(p)  P0 : "
ha = st.selectbox(
            "Ho:  ud : ",
            ('!=', '>', '<'))
significance_level=st.number_input("Enter significance_level value")#significance_level=0.01
#0.1




def rejecion_region(x_col,y_col):

            zip_object = zip(x_col, y_col)

            for list1_i, list2_i in zip_object:
                difference.append(list1_i-list2_i)

            sumation_d=sum(difference)
            st.write("summation of difference is : ",sumation_d)

            d_bar=np.mean(difference)
            st.write("mean of difference is: ",d_bar)


            dict_op={"X":x_col,"Y":y_col,"d_bar : X-Y":difference}

            op_df=pd.DataFrame(dict_op)
            st.write(op_df)

            std_dev=np.std(difference)
            st.write("standard deviation is : ",std_dev)


            # ---------------------Hypothesis test start---------------


            def hypo_test(ho, ha):
                if ((ho == ">=" and ha == "!=") or (ho == ">=" and ha == ">") or (ho == "<=" and ha == "!=") or (
                        ho == "<=" and ha == "<")):
                    return False
                elif (ha == "<"):
                    return "Left_tail"
                elif (ha == ">"):
                    return "Right_tail"
                else:
                    return "Two_tail"


            # st.write(hypo_test(ho,ha))

            # st.write("Ho:(p) : " + ho + f" : {P0}")
            # st.write("Ho:(p) : " + ha + f" : {P0}")

            # ---------------------Hypothesis test end---------------

            # --------------------Test Statistic Start--------------------
            t=(d_bar-float(ud))/(std_dev/math.sqrt(float(n)))
            # st.write(t)

            # --------------------Test Statistic End--------------------

            # ---------------- P value start-----------
            df=int(n)-1
            p_two_tailed= (1 - (scipy.stats.t.cdf((t),df)))*2
            p_right=1 - scipy.stats.t.cdf((t),df)
            p_left=scipy.stats.t.cdf(t,df)
            st.write(p_two_tailed)
            # ---------------- P value end-----------
# Rejection Region for 2 tail
            if (hypo_test(ho, ha) == "Two_tail"):
                st.write(f"p value is {p_two_tailed}")
                st.write(f"since  p-value > {significance_level} therefore fail to reject " if p_two_tailed > significance_level else f"since  p-value > {significance_level} therefore reject ")

# Rejection Region for left tail
            if (hypo_test(ho, ha) == "Left_tail"):
                st.write(f"p value is {p_left}")
                st.write(f"since  p-value > {significance_level} therefore fail to reject " if p_two_tailed > significance_level else f"since  p-value > {significance_level} therefore reject ")

# Rejection Region for right tail
            if (hypo_test(ho, ha) == "Right_tail"):

                st.write(f"p value is {p_right}")
                st.write(f"since  p-value > {significance_level} therefore fail to reject " if p_two_tailed > significance_level else f"since  p-value > {significance_level} therefore reject ")


if (st.button("calculate")):
    x_col = list(map(int, x.split(",")))
    y_col = list(map(int, y.split(",")))
    rejecion_region(x_col,y_col)


# st.write(f"since  p-value > {significance_level} therefore fail to reject " if p_two_tailed>significance_level else f"since  p-value > {significance_level} therefore reject ")
