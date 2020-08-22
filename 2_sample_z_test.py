import math
import scipy.stats
import scipy.special as scsp
import numpy as np
import streamlit as st

st.title("2 Sample Z Test")

u1,u2=0,0
diff=st.number_input(" Enter u1- u2 value : ")#10
sigma1=st.number_input(" Enter sigma1 value : ")#50
sigma2=st.number_input(" Enter sigma2 value : ")#60
x1_bar=st.number_input(" Enter x1_bar value : ")#25
x2_bar=st.number_input(" Enter x2_bar value : ")#124
n1=st.number_input(" Enter n1 value : ")#24
n2=st.number_input(" Enter n2 value : ")#25
significance_level=st.number_input(" Enter significance_level value : ")#0.05




#---------------------Hypothesis test start---------------
# ho="="#input("u:(p)  u_0 : ")
# ha="!="#input("u:(p)  u_0 : ")

ho = st.selectbox(
            "Ho:(p)  P0 : ",
            ('==', '>=', '<='))  # "="input("Ho:(p)  P0 : ")
ha = st.selectbox(
            "Ho:(p)  P0 : ",
            ('!=', '>', '<'))



def rejection_region():
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

    st.write("Ho:(u) :  u1-u2  " + ho + f": {diff}")
    st.write("Ha:(u) :  u1-u2 " + ha + f" : {diff}")

    # ---------------------Hypothesis test end---------------

    # ---------------Test Statistic start ----------------
    z = (x1_bar - x2_bar - diff) / (math.sqrt((sigma1 * sigma1) / n1 + (sigma2 * sigma2) / n2))

    # ---------------Test Statistic end ------------------

    # ----------------P value from Z Start-------------
    p_left = round(0.5 * (1 + scsp.erf(float(z) / np.sqrt(2))), 5)
    p_right = 1 - p_left
    p_two_tailed = 1
    if float(z) < 0:
        p_two_tailed = 2 * p_left
    else:
        p_two_tailed = 2 * p_right
    # #----------------P value from Z End-------------


    st.write(" Rejection Region is : ")
    # Rejection Region for 2 tail
    if (hypo_test(ho, ha) == "Two_tail"):
        z_critical = ((-(scipy.stats.norm.ppf(1 - significance_level / 2))))
        st.write(f"z critical <{z_critical}" if z < 0 else f"z critica >{abs(z_critical)}")
        # st.write("\nTwo Null hypothesis is rejected ")
        st.write("z test statistic  is :", (z))
        st.write("Decision through z statistic : ")
        st.write(
            f"since test statistic z calculated < {round(z_critical, 2)} \n Therefore Null hypothesis is rejected" if z < z_critical else f"since test statistic z calculated > {round(z_critical, 2)} \n Therefore Null hypothesis is not rejected")
        st.write("Decision through p value : ")
        st.write("p_value is : ", p_two_tailed)
        st.write(f"since p value is < {significance_level}")

    # Rejection Region for left tail
    if (hypo_test(ho, ha) == "Left_tail"):
        z_critical = (-(scipy.stats.norm.ppf(1 - significance_level / 2)))
        st.write(f"z critical value is : {z_critical}")
        st.write("z test statistic  is  :", (z))
        st.write("Decision through z statistic :")
        st.write(
            f"since test statistic z calculated < {round(z_critical, 2)} \n Therefore Null hypothesis is rejected" if z < z_critical else f"since test statistic z calculated > {round(z_critical, 2)} \n Therefore Null hypothesis is not rejected")
        st.write("Decision through p value : ")
        st.write("p_value is : ", p_left)
        st.write(f"p_left < {significance_level}")

    # Rejection Region for right tail
    z_critical = scipy.stats.norm.ppf(1 - significance_level)
    if (hypo_test(ho, ha) == "Right_tail"):
        if z > (scipy.stats.norm.ppf(1 - significance_level / 2)):
            st.write("\nRight Null hypothesis is rejected ")
        st.write(f"z critical value is : {z_critical}")
        st.write("z test statistic  is : ", (z))
        st.write("Decision through z statistic :")
        st.write(
            f"since test statistic z calculated < {round(z_critical, 2)} \n Therefore Null hypothesis is rejected" if z > z_critical else f"since test statistic z calculated > {round(z_critical, 2)} \n Therefore Null hypothesis is not rejected")
        st.write("Decision through p value : ")
        st.write("p_value is : ", p_right)
        st.write(f"p_right > {significance_level}")

if (st.button("calculate")):

    rejection_region()

# --------------------------Rejection Region End---------------------------------