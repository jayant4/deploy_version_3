import math
import scipy.stats
import numpy as np
import scipy.special as scsp
import streamlit as st

st.title("1 Sample Z Test ")
#population mean
u_0=st.number_input("Enter u_0 value")

# sample size n
n=st.number_input("Enter n value")

# sample mean x_bar
x_bar=st.number_input("Enter x bar value")

# Standard deviation sigma
sigma=st.number_input("Enter standard deviation value ")

# significance_level
significance_level=st.number_input("Enter Significance level value")

#---------------------Hypothesis test start---------------
ho=st.selectbox(
            "Ho:(p)  P0 : ",
            ('==', '>=', '<='))#"="#input("u:(p)  u_0 : ")
ha= st.selectbox(
            "Ho:(p)  P0 : ",
            ('!=', '>', '<'))#"!="#input("u:(p)  u_0 : ")



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
    st.write("Ho:(u) : " + ha + f" : {u_0}")
    # ---------------------Hypothesis test end---------------

    # ---------------Test Statistic start ----------------

    z = (x_bar - u_0) / ((sigma) / math.sqrt(n))
    st.write("Test Statistic z is: ", z)
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

        # Rejection Region for 2 tail
        if (hypo_test(ho, ha) == "Two_tail"):
                z_critical = ((-(scipy.stats.norm.ppf(1 - significance_level / 2))))
                st.write(f"z critical <{z_critical}" if z < 0 else f"z critica >{abs(z_critical)}")

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

        if (hypo_test(ho, ha) == "Right_tail"):
            z_critical = scipy.stats.norm.ppf(1 - significance_level)
            # if z > (scipy.stats.norm.ppf(1 - significance_level / 2)):
            #     st.write("\nRight Null hypothesis is rejected ")
            st.write(f"z critical value is : {z_critical}")
            st.write("z test statistic  is : ", (z))
            st.write("Decision through z statistic :")
            st.write(f"since test statistic z calculated < {round(z_critical, 2)} \n Therefore Null hypothesis is rejected" if z > z_critical else f"since test statistic z calculated > {round(z_critical, 2)} \n Therefore Null hypothesis is not rejected")
            st.write("Decision through p value : ")
            st.write("p_value is : ", p_right)
            st.write(f"p_right > {significance_level}")
# --------------------------Rejection Region End---------------------------------

if (st.button("calculate")):
    rejection_region()