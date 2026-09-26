import streamlit as st
from datetime import date

st.title("STUDENT APP")

with st.sidebar:
    st.header("Student Details")
    name=st.text_input("Name: ")
    st.write("Name: ", name)
    age=st.number_input("AGE: ",
             min_value=1,
             max_value=100)
    st.write("Age: ",age)
    address=st.text_area("ADDRESS: ")
    st.write("Address: ",address)

col1, col2 = st.columns(2)
with col1:
    department=st.selectbox("SELECT YOUR DEPARTMENT",
        ["AI & ML",
        "DATA SCIENCE",
        "COMPUTER SCIENCE",
        "BCA",
        "INFORMATION TECHNOLOGY"])
    
    gender=st.radio("SELECT YOUR GENDER",
        ["FEMALE", "MALE", "TRANSGENDER"])

with col2:
    dob=st.date_input("SELECT YOUR DATE OF BIRTH",
        min_value=date(1950, 1, 1),
        max_value=date.today())

    course=st.multiselect("SELECT THE COURSE",
    ["PYTHON",
    "SQL",
    "POWER BI",
    "MACHINE LEARNING",
    "DEEP LEARNING"])

with st.container(border=True):
    agree=st.checkbox("I agree to the terms")
    if st.button("SUBMIT"):
        if agree:
            st.write("Registration completed")
            st.write("SUBMITTED!")

            with st.expander("View Student Details"):
                    st.write("Name:", name)
                    st.write("Age:", age)
                    st.write("DOB: ", dob)
                    st.write("Gender: ",gender)
                    st.write("Address:", address)
                    st.write("Course:, ",course)
                    st.write("Department: ",department)
        else:
            st.write("Please agree to the terms.")
