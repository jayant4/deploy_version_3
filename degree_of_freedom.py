import streamlit as st

st.title("Degree of freedom ")

s1=st.number_input("Enter s1 Value")#50
s2=st.number_input("Enter s2 Value")#60
n1=st.number_input("Enter n1 Value ")#24
n2=st.number_input("Enter n2 Value") #25

def calculate():
    def degree_of_freedom(s1,s2,n1,n2):
        op_numerator=(((s1*s1)/n1)+((s2*s2)/n2))**2
         # print(op_numerator)

        op_denom=((1/(n1-1))*((s1*s1)/n1)**2)+((1/(n2-1))*((s2*s2)/n2)**2)
        return(op_numerator/op_denom)

    st.write("Degree of Freedom is: ",degree_of_freedom(s1,s2,n1,n2))

if (st.button("calculate")):
        calculate()