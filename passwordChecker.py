import streamlit as st
# Regix hum is liye import kerwatein hien ke hamein kisi specific pattern find kerna hoto::
# jese ke check kerna he ke password me koi capital letter he ya koi small letter he ya koi number he ya koi special character he to regex ka use karein ge ..
# re ==> regular expression
import re


st.set_page_config(page_title="Password Strength Checker", page_icon="🔐")
st.title("🔐 Password Strength Checker")
st.markdown("""
## Welcome to the ultimate password strength checker!🔥
Use this simple tool to check the strength of your password and get suggestions on how to to make it stronger.🔒
We will give you helpful tips to create a ***Strong Password*** 🔏""")




password = st.text_input("Enter your password here:", type="password")


feedback = []
score = 0


if password:
    # Length check
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("❌Password should be 8 characters long.")
    
    # Uppercase & lowercase check
    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("❌Password should contain both upper and lowercase letters.")
    
    # Digit check
    if re.search(r"[0-9]", password):
        score += 1
    else:
        feedback.append("❌Password should contain at least one digit.")
    
    # SPECIAL CHARACTER CHECK (FIXED REGEX)
    if re.search(r"[!$%_\-?]", password):  # Corrected line
        score += 1
    else:
        feedback.append("❌Password should contain at least one special character (!$%-_?).")
    
    if score == 4:
        feedback = ["✔ Your Password is correct.✨"]
    elif score == 3:
        feedback.append("🟡 Your Password is medium strength. It could be stronger.🎀")
    else:
        feedback.append("🔴 Your Password is too weak. Please make it stronger.")
        
    if feedback:
        st.markdown("## Improvement Suggestions")
        for tip in feedback:
            st.write(tip)
else:
    st.info("Please enter your password to get started..")