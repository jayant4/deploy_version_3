import scipy.stats
import streamlit as st

st.title('Chi Critical Value')
#find Z critical value
significance_level=st.text_input(" Enter significance value : ")
degrees_of_freedom=st.text_input(" Enter Degree of Freedom : ")

def chi_critical_value(significance_level,degrees_of_freedom):
    critical_value=scipy.stats.chi2.ppf(significance_level,degrees_of_freedom)

    return(round(critical_value, 5))


if (st.button("calculate")):
    critical_value=((chi_critical_value(1-float(significance_level),float(degrees_of_freedom))))

    st.write(f"Critical value of Chi Test is is : {critical_value} ")

    f"""
    #### Thus, if we’re conducting some type of Chi-Square test then we can compare the Chi-Square test statistic to {critical_value}. If the test statistic is greater than {critical_value}, then the results of the test are statistically significant.
    """
