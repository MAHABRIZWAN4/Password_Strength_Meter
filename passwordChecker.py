

import streamlit as st
import re

# Set page config must be the first Streamlit command
st.set_page_config(page_title="Password Strength Checker", page_icon="🔐")

# Custom CSS styling


# Custom CSS styling
st.markdown("""
<style>
    .main {
        background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
        padding: 20px;
        border-radius: 10px;
    }
    .title-text {
        background: linear-gradient(120deg, #155799, #159957);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-size: 42px;
        font-weight: bold;
        text-align: center;
        padding: 20px;
        animation: fadeIn 1.5s ease-in;
    }
    .subtitle-text {
        color: #2c3e50;
        font-size: 18px;
        text-align: center;
        margin-bottom: 30px;
        animation: slideIn 1.5s ease-out;
    }
    .password-input {
        margin: 20px 0;
        padding: 10px;
        border-radius: 5px;
        border: 2px solid #3498db;
        transition: all 0.3s ease;
    }
    .password-input:focus {
        border-color: #2ecc71;
        box-shadow: 0 0 10px rgba(46, 204, 113, 0.3);
    }
    .feedback-box {
        padding: 15px;
        border-radius: 8px;
        margin: 10px 0;
        animation: bounceIn 0.8s ease;
    }
    @keyframes fadeIn {
        from { opacity: 0; }
        to { opacity: 1; }
    }
    @keyframes slideIn {
        from { transform: translateY(-20px); opacity: 0; }
        to { transform: translateY(0); opacity: 1; }
    }
    @keyframes bounceIn {
        0% { transform: scale(0.3); opacity: 0; }
        50% { transform: scale(1.05); }
        70% { transform: scale(0.9); }
        100% { transform: scale(1); opacity: 1; }
    }
</style>
""", unsafe_allow_html=True)


# Title with animation
st.markdown(' <h1 class="title-text"> 🔐 Password Strength Checker</h1>', unsafe_allow_html=True)

# Subtitle with animation
st.markdown("""
<div class="subtitle-text">
    <p>Welcome to the ultimate password strength checker!🔥</p>
    <p>Use this simple tool to check the strength of your password and get suggestions on how to make it stronger.🔒</p>
    <p>We will give you helpful tips to create a <strong>Strong Password</strong> 🔏</p>
</div>
""", unsafe_allow_html=True)

# Password input with custom styling
password = st.text_input("Enter your password here:", type="password")

feedback = []
score = 0

if password:
    # Length check
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("❌ Password should be 8 characters long.")
    
    # Uppercase & lowercase check
    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("❌ Password should contain both upper and lowercase letters.")
    
    # Digit check
    if re.search(r"[0-9]", password):
        score += 1
    else:
        feedback.append("❌ Password should contain at least one digit.")
    
    # Special character check
    if re.search(r"[!$%_\-?]", password):
        score += 1
    else:
        feedback.append("❌ Password should contain at least one special character (!$%-_?).")
    
    # Feedback styling based on score
    if score == 4:
        st.markdown("""
            <div class="feedback-box" style="background-color: #d4edda; color: #155724; border: 1px solid #c3e6cb;">
                ✨ Excellent! Your password meets all security requirements! ✔
            </div>
        """, unsafe_allow_html=True)
    elif score == 3:
        st.markdown("""
            <div class="feedback-box" style="background-color: #fff3cd; color: #856404; border: 1px solid #ffeeba;">
                🎀 Your password is medium strength. It could be stronger! 🟡
            </div>
        """, unsafe_allow_html=True)
    else:
        st.markdown("""
            <div class="feedback-box" style="background-color: #f8d7da; color: #721c24; border: 1px solid #f5c6cb;">
                🔴 Your password is too weak. Please make it stronger!
            </div>
        """, unsafe_allow_html=True)
    
    if feedback:
        st.markdown("## 🔍 Improvement Suggestions")
        for tip in feedback:
            st.markdown(f"""
                <div class="feedback-box" style="background-color: #e8f4f8; color: #0c5460; border: 1px solid #bee5eb;">
                    {tip}
                </div>
            """, unsafe_allow_html=True)
else:
    st.markdown("""
        <div class="feedback-box" style="background-color: #cce5ff; color: #004085; border: 1px solid #b8daff;">
            ℹ️ Please enter your password to get started...
        </div>
    """, unsafe_allow_html=True)

# Progress bar for password strength
if password:
    st.markdown("### Password Strength")
    progress = score * 25  # Convert score to percentage
    st.progress(progress)
    st.markdown(f"<p style='text-align: center; color: {'#28a745' if score == 4 else '#ffc107' if score == 3 else '#dc3545'}'>Strength: {progress}%</p>", unsafe_allow_html=True)