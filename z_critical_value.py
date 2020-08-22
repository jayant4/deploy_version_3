import scipy.stats
import streamlit as st

st.title('Z Critical Value')
#find Z critical value
significance_level=st.text_input(" Enter significance value : ")


def z_critical_value(significance_level):
    Left_tailed_test=scipy.stats.norm.ppf(significance_level)
    Right_tailed_test=scipy.stats.norm.ppf(1-significance_level)
    Two_tailed_test=scipy.stats.norm.ppf(1-significance_level/2)
    return(round(Left_tailed_test, 5)),(round(Right_tailed_test, 5)),(round(Two_tailed_test, 5))


if (st.button("calculate")):
    Left_tailed_test,Right_tailed_test,Two_tailed_test=((z_critical_value(float(significance_level))))

    st.write(f"""
   \n Left_tailed_test is : {Left_tailed_test} \n 
    Right_tailed_test is : {Right_tailed_test} \n
    Two_tailed_test is : {Two_tailed_test}
    """)

    f"""
    #### Whenever you perform a two-tailed test, there will be two critical values. In this case, the Z critical values are {Right_tailed_test} and {Left_tailed_test}. Thus, if the test statistic is less than {Left_tailed_test} or greater than {Right_tailed_test}, the results of the test are statistically significant.
    """

# print(z_critical_value(0.01))