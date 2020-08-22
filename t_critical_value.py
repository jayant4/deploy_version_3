import scipy.stats
import streamlit as st

st.title('T Critical Value')
#find Z critical value
significance_level=st.text_input(" Enter significance value : ")
degrees_of_freedom=st.text_input(" Enter Degree of Freedom : ")

def t_critical_value(significance_level,degrees_of_freedom):
    Left_tailed_test=scipy.stats.t.ppf(significance_level,degrees_of_freedom)
    Right_tailed_test=scipy.stats.t.ppf(1-significance_level,degrees_of_freedom)
    Two_tailed_test=scipy.stats.t.ppf(1-significance_level/2,degrees_of_freedom)
    return(round(Left_tailed_test, 5)),(round(Right_tailed_test, 5)),(round(Two_tailed_test, 5))


if (st.button("calculate")):
    Left_tailed_test,Right_tailed_test,Two_tailed_test=((t_critical_value(float(significance_level),float(degrees_of_freedom))))

    st.write(f"""
   \n Left_tailed_test is : {Left_tailed_test} \n 
    Right_tailed_test is : {Right_tailed_test} \n
    Two_tailed_test is : {Two_tailed_test}
    """)

    f"""
    #### Whenever you perform a two-tailed test, there will be two critical values. In this case, the Z critical values are {Right_tailed_test} and {Left_tailed_test}. Thus, if the test statistic is less than {Left_tailed_test} or greater than {Right_tailed_test}, the results of the test are statistically significant.
    """
# print(t_critical_value(0.01,48))
# print(t_critical_value(0.01,46))