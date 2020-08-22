import math
import scipy.stats
import numpy as np
import scipy.special as scsp
import streamlit as st

st.title("1 Sample T Test ")
#population mean
u_0=st.number_input("Enter u0 value") #u0=100
# sample size n
n=st.number_input("Enter n value") #n=100
# sample mean x_bar
x_bar=st.number_input("Enter x_bar value") #x_bar= 110
# Standard deviation sigma
sigma=st.number_input("Enter sigma value") #sigma=40
# significance_level
significance_level=st.number_input("Enter significance_level value")#significance_level=0.01

# degrees_of_freedom
degrees_of_freedom=n-1

#---------------------Hypothesis test start---------------
ho = st.selectbox(
            "Ho:(p)  P0 : ",
            ('==', '>=', '<='))  # "="input("Ho:(p)  P0 : "
ha = st.selectbox(
            "Ho:(p)  P0 : ",
            ('!=', '>', '<'))  # "!="#input("Ho:(p)  P0 : ")



# --------------------------Rejection Region Start---------------------------------
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

    st.write("Ho:(u) : " + ho + f" : {u_0}")
    st.write("Ha:(u) : " + ha + f" : {u_0}")
    # ---------------------Hypothesis test end---------------

    # ---------------Test Statistic start ----------------

    t = (x_bar - u_0) / ((sigma) / math.sqrt(n))
    st.write("Test Statistic t is: ", t)
    # ---------------Test Statistic end ------------------

    # ----------------P value from T Start-------------
    p_left = round(0.5 * (1 + scsp.erf(float(t) / np.sqrt(2))), 5)
    p_right = 1 - p_left
    p_two_tailed = 1
    if float(t) < 0:
        p_two_tailed = 2 * p_left
    else:
        p_two_tailed = 2 * p_right
    # #----------------P value from T End-------------





    # Rejection Region for 2 tail
    if (hypo_test(ho, ha) == "Two_tail"):
        Two_tailed_test=scipy.stats.t.ppf(1-significance_level/2,degrees_of_freedom)
        st.write(f"t critical value is  : {Two_tailed_test}")
        st.write(f"t < {Two_tailed_test}" if t<0 else f" t > {abs(Two_tailed_test)}")
        st.write("Decision is :")
        st.write(f"since test statistic t calculated < {round(Two_tailed_test, 2)} \n Therefore Null hypothesis is rejected" if t < Two_tailed_test else f"since test statistic z calculated > {round(Two_tailed_test, 2)} \n Therefore Null hypothesis is not rejected")

        st.write("p_value is : ", p_two_tailed)


    # Rejection Region for left tail
    if (hypo_test(ho, ha) == "Left_tail"):
        t_critical=scipy.stats.t.ppf(significance_level,degrees_of_freedom)

        st.write("t critical  is :", (t_critical))
        st.write("Decision is :")
        st.write(f"since test statistic t calculated < {round(t_critical, 2)} \n Therefore Null hypothesis is rejected" if t < t_critical else f"since test statistic t calculated > {round(t_critical, 2)} \n Therefore Null hypothesis is not rejected")

        st.write("p_value is : ", p_left)
        st.write(f"p_left < {significance_level}")

    # Rejection Region for right tail
    if (hypo_test(ho, ha) == "Right_tail"):
        t_critical=scipy.stats.t.ppf(1-significance_level,degrees_of_freedom)

        st.write("t critical is :", (t_critical))
        st.write("Decision is :")
        st.write(f"since test statistic t calculated < {round(t_critical, 2)} \n Therefore Null hypothesis is rejected" if t > t_critical else f"since test statistic t calculated > {round(t_critical, 2)} \n Therefore Null hypothesis is not rejected")
        st.write("p_value is : ", p_right)
        st.write(f"p_right > {significance_level}")

# --------------------------Rejection Region End---------------------------------


if (st.button("calculate")):
    rejection_region()