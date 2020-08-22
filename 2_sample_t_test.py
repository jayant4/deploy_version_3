import math
import math
import scipy.stats
import numpy as np
from scipy import stats
import scipy.special as scsp
import streamlit as st

st.title("2 sample T Test ")


u1,u2=0,0
diff=st.number_input("Enter P0 value")
s1=st.number_input("Enter s1 value")#50
s2=st.number_input("Enter s2 value")#60
x1_bar=st.number_input("Enter x1_bar value")#25
x2_bar=st.number_input("Enter x2_bar value")#124
n1=st.number_input("Enter n1 value")#24
n2=st.number_input("Enter n2 value")#25

# signinficane level sigma
significance_level = st.number_input("Enter Significance level value")  # 0.01
        #0.01


#---------------------Hypothesis test start---------------
ho = st.selectbox(
    "Ho:(p)  P0 : ",
    ('==', '>=', '<='))  # "="input("Ho:(p)  P0 : ")
ha = st.selectbox(
    "Ho:(p)  P0 : ",
    ('!=', '>', '<'))  # "!="#input("Ho:(p)  P0 : ")



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
    # t=((x1_bar-x2_bar) - (diff))/math.sqrt((s1*s1/n1)+(s2*s2/n2))
    t_test = ((x1_bar - x2_bar) - diff) / (math.sqrt(((s1 * s1) / n1) + ((s2 * s2) / n2)))
    st.write("t test", t_test)

    # ---------------Test Statistic end ------------------

    # ---------------- degree of freedom start ------------

    def degree_of_freedoms(s1, s2, n1, n2):

        op_numerator = (((s1 * s1) / n1) + ((s2 * s2) / n2)) ** 2
        op_denom = ((1 / (n1 - 1)) * ((s1 * s1) / n1) ** 2) + ((1 / (n2 - 1)) * ((s2 * s2) / n2) ** 2)
        return (op_numerator / op_denom)

    # ---------------- degree of freedom start ------------

    # --------------------------Rejection Region Start---------------------------------

    degree_of_freedom=degree_of_freedoms(s1,s2,n1,n2)
    pval = round((stats.t.sf(np.abs(t_test), degree_of_freedom)*2),3)
    st.write("p value is ",pval)


    # Rejection Region for 2 tail
    if (hypo_test(ho, ha) == "Two_tail"):
        t_critical=scipy.stats.t.ppf(1-significance_level/2,degree_of_freedom)
        st.write(f"t critical <{t_critical}" if t_test < 0 else f"z critica >{abs(t_critical)}")
        # st.write("\nTwo Null hypothesis is rejected ")
        st.write("t test statistic  is :", (t_test))
        st.write("Decision through t statistic : ")
        st.write(
            f"since test statistic t calculated < {round(t_critical, 2)} \n Therefore Null hypothesis is rejected" if t_test < t_critical else f"since test statistic t calculated > {round(t_critical, 2)} \n Therefore Null hypothesis is not rejected")
        st.write("Decision through p value : ")
        st.write("p_value is : ", round((1-pval)*2,7))
        st.write(f"since p value is < {significance_level}")


    # Rejection Region for left tail
    if (hypo_test(ho, ha) == "Left_tail"):
        p_left=pval

        t_critical = scipy.stats.t.ppf(significance_level,degree_of_freedom)
        st.write(f"t critical value is : {t_critical}")
        st.write("t test statistic  is  :", (t_test))
        st.write("Decision through t statistic :")
        st.write(
            f"since test statistic t calculated < {round(t_critical, 2)} \n Therefore Null hypothesis is rejected" if t_test < t_critical else f"since test statistic t calculated > {round(t_critical, 2)} \n Therefore Null hypothesis is not rejected")
        st.write("Decision through p value : ")
        st.write("p_value is : ", p_left)
        st.write(f"p_left < {significance_level}")

    # Rejection Region for right tail
    if (hypo_test(ho, ha) == "Right_tail"):
        p_right=round(1-pval,7)
        t_critical=scipy.stats.t.ppf(1-significance_level,degree_of_freedom)
        st.write(f"t critical value is : {t_critical}")
        st.write("t test statistic  is : ", (t_test))
        st.write("Decision through t statistic :")
        st.write(
            f"since test statistic t calculated < {round(t_critical, 2)} \n Therefore Null hypothesis is rejected" if t_test > t_critical else f"since test statistic t calculated > {round(t_critical, 2)} \n Therefore Null hypothesis is not rejected")
        st.write("Decision through p value : ")
        st.write("p_value is : ", p_right)
        st.write(f"p_right > {significance_level}")

# --------------------------Rejection Region End---------------------------------

if (st.button("calculate")):
    rejection_region()