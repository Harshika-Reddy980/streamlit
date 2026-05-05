import streamlit as st
from pymongo import MongoClient

# 🔗 MongoDB Connection
from pymongo import MongoClient

uri = "mongodb+srv://testuser:<testuser123>@cluster0.hugqvc9.mongodb.net/?appName=Cluster0"
client = MongoClient(uri)
db = client["student_db"]
collection = db["students"]

# Page config
st.set_page_config(page_title="Student Form", layout="wide")

# Custom CSS
st.markdown("""
    <style>
    .main {
        background-color: #f5f7fa;
    }
    .title {
        text-align: center;
        font-size: 40px;
        font-weight: bold;
        color: #2c3e50;
    }
    .section {
        background-color: white;
        padding: 20px;
        border-radius: 10px;
        margin-bottom: 20px;
        box-shadow: 0px 2px 5px rgba(0,0,0,0.1);
    }
    </style>
""", unsafe_allow_html=True)

# Title
st.markdown('<div class="title">🎓 Student Registration Form</div>', unsafe_allow_html=True)

with st.form("student_form"):

    # Personal Details
    st.markdown('<div class="section">', unsafe_allow_html=True)
    st.subheader("👤 Personal Details")

    col1, col2 = st.columns(2)
    with col1:
        full_name = st.text_input("Full Name")
        age = st.number_input("Age", min_value=1, max_value=100)
        gender = st.selectbox("Gender", ["Male", "Female", "Other"])
    with col2:
        email = st.text_input("Email")
        phone = st.text_input("Phone Number")

    st.markdown('</div>', unsafe_allow_html=True)

    # Academic Details
    st.markdown('<div class="section">', unsafe_allow_html=True)
    st.subheader("🎓 Academic Details")

    col3, col4 = st.columns(2)
    with col3:
        college = st.text_input("College Name")
        department = st.selectbox("Department", ["CSE", "ECE", "EEE", "MECH", "CIVIL", "OTHER"])
    with col4:
        year = st.selectbox("Year", ["1st", "2nd", "3rd", "4th"])
        cgpa = st.number_input("CGPA", min_value=0.0, max_value=10.0)

    st.markdown('</div>', unsafe_allow_html=True)

    # Skills
    st.markdown('<div class="section">', unsafe_allow_html=True)
    st.subheader("💡 Skills & Interests")

    skills = st.text_area("Skills")
    hobbies = st.text_area("Hobbies")

    st.markdown('</div>', unsafe_allow_html=True)

    # Address
    st.markdown('<div class="section">', unsafe_allow_html=True)
    st.subheader("🏠 Address")

    address = st.text_area("Address")
    col5, col6 = st.columns(2)
    with col5:
        city = st.text_input("City")
    with col6:
        state = st.text_input("State")

    pincode = st.text_input("Pincode")

    st.markdown('</div>', unsafe_allow_html=True)

    # Submit Button
    submit = st.form_submit_button("🚀 Submit")

# 🔥 STORE DATA IN MONGODB
if submit:
    data = {
        "full_name": full_name,
        "age": age,
        "gender": gender,
        "email": email,
        "phone": phone,
        "college": college,
        "department": department,
        "year": year,
        "cgpa": cgpa,
        "skills": skills,
        "hobbies": hobbies,
        "address": address,
        "city": city,
        "state": state,
        "pincode": pincode
    }

    collection.insert_one(data)

    st.success("✅ Data stored successfully in MongoDB!")
    