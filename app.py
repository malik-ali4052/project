import re
import streamlit as st

def check_password_strength(password):
    score = 0
    feedback = []

    # Check length
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("❌ Password should be at least 8 characters long.")

    # Check for uppercase and lowercase letters
    if re.search(r'[A-Z]', password) and re.search(r'[a-z]', password):
        score += 1
    else:
        feedback.append("❌ Include both uppercase and lowercase letters.")

    # Check for digits
    if re.search(r'\d', password):
        score += 1
    else:
        feedback.append("❌ Include at least one digit (0-9).")

    # Check for special characters
    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        score += 1
    else:
        feedback.append("❌ Include at least one special character (e.g., !@#$%^&*).")

    return score, feedback

# Streamlit UI
st.set_page_config(page_title="Password Strength Checker", layout="centered")
st.title("🔐 Password Strength Checker")
st.header("Evaluate the strength of your password by checking its complexity by the app made by M.Ali.")
st.write("Enter your password below to check its security level.")

password = st.text_input("Enter your password:", type="password")

if st.button("Check Password"):
    if password:
        score, feedback = check_password_strength(password)

        if score == 4:
            st.success("✅ Strong Password - Your password is secure.")
        elif score == 3:
            st.info("⚠️ Moderate Password - Consider improving security by following suggestions:")
            for f in feedback:
                st.write(f)
        else:
            st.error("❌ Weak Password - Please address the following issues:")
            for f in feedback:
                st.write(f)
    else:
        st.warning("⚠️ Please enter a password first!")

