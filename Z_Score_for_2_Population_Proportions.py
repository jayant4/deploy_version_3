import math
import scipy.special as scsp
import scipy.stats
import numpy as np
import streamlit as st

st.title('Z Score For 2 Population Proportions')

n1=st.number_input("Enter n1 Value")#230
n2=st.number_input("Enter n2 Value")#540
x1=st.number_input("Enter x1 Value")#58
x2=st.number_input("Enter x2 Value")#58
significance_level=st.number_input("Enter Significance_level")#0.01


ho = st.selectbox(
            "Ho:  ud : ",
            ('==', '>=', '<='))  # "="input("Ho:(p)  P0 : "
ha = st.selectbox(
            "Ho:  ud : ",
            ('!=', '>', '<'))




def rejection_region():
    # Sample proportion
    p1_hat = x1 / n1
    # print("p1 hat : ",p1_hat)

    p2_hat = x2 / n2
    # print("p2 hat : ",p2_hat)

    # Pooled Population
    p_bar = (x1 + x2) / (n1 + n2)

    # print("p bar : ",p_bar)
    #
    # Hypothesis Test
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

    # print("Ho:(P1) : " + ho + f" : {p2_hat}")
    # print("Ha:(P1) : " + ha + f" : {p2_hat}")

    # print(hypo_test(ho,ha))

    # ---------------------Hypothesis test end---------------
    # Test Statistic
    z = (p1_hat - p2_hat) / (math.sqrt(p_bar * (1 - p_bar) * (1 / n1 + 1 / n2)))
    print("test statistic z : ", z)

    # ----------------P value from Z Start-------------
    p_left = round(0.5 * (1 + scsp.erf(float(z) / np.sqrt(2))), 5)
    p_right = 1 - p_left
    p_two_tailed = 1
    if float(z) < 0:
        p_two_tailed = 2 * p_left
    else:
        p_two_tailed = 2 * p_right
    # #----------------P value from Z End-------------

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

# --------------------------Rejection Region End---------------------------------

if (st.button("calculate")):
    rejection_region()