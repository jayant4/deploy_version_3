import math
import streamlit as st
import scipy.stats
import numpy as np
import scipy.special as scsp

P0=st.number_input("Enter P0",min_value=0.01)#0.625
n=st.number_input("Enter  N :",min_value=0.01)#70
x=st.number_input("Enter  X :",min_value=0.01)#30
p_cap=x/n

significance_level=st.number_input("Enter  Significance value :")#0.01
#---------------------Hypothesis test start---------------

ho="="#input("Ho:(p)  P0 : ")
ha="!="#input("Ho:(p)  P0 : ")

def hypo_test(ho,ha):

    if((ho==">=" and ha=="!=") or (ho==">=" and ha==">") or (ho=="<=" and ha=="!=")or (ho=="<=" and ha=="<")):
        return False
    elif (ha=="<"):
        return "Left_tail"
    elif (ha==">"):
        return "Right_tail"
    else:
        return "Two_tail"
st.write("Ho:(p) : " + ho + f" : {P0}")
st.write("Ho:(p) : " + ha + f" : {P0}")

# print(hypo_test(ho,ha))



#---------------------Hypothesis test end---------------
#


# --------------------------Rejection Region Start---------------------------------
def rejection_region():
    # --------------------Test Statistic Start--------------------
    z = ((p_cap - P0) / math.sqrt(P0 * (1 - P0) / n))

    # --------------------Test Statistic End--------------------

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
        if z < (-(scipy.stats.norm.ppf(1 - significance_level / 2))) or z > (
        scipy.stats.norm.ppf(1 - significance_level / 2)):
            z_critical=((-(scipy.stats.norm.ppf(1 - significance_level / 2))))
            st.write(f"z<{z_critical}" if z<0 else f"z>{abs(z_critical)}")
            st.write("\nTwo Null hypothesis is rejected ")
        st.write("z is :", (z))
        st.write("Decision is :")
        st.write("p_value is : ", p_two_tailed)


    # Rejection Region for left tail
    if (hypo_test(ho, ha) == "Left_tail"):
        if z < (-(scipy.stats.norm.ppf(1 - significance_level / 2))):
            print("\n Left Null hypothesis is rejected ")
        st.write("z is :", (z))
        st.write("Decision is :")
        st.write("p_value is : ", p_left)
        st.write(f"p_left < {significance_level}")

    # Rejection Region for right tail
    if (hypo_test(ho, ha) == "Right_tail"):
        if z > (scipy.stats.norm.ppf(1 - significance_level / 2)):
            print("\nRight Null hypothesis is rejected ")
        st.write("z is :", abs(z))
        st.write("Decision is :")
        st.write("p_value is : ", p_right)
        st.write(f"p_right > {significance_level}")
# rejection_region()
# --------------------------Rejection Region End---------------------------------



if (st.button("calculate")):
    rejection_region()

