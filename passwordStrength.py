import re
import streamlit as st 

# page styling
st.set_page_config(page_title="Password Strength Checker By Kishor Kumar", page_icon="👨‍💻", layout="centered")
# custom css 
st.markdown("""
<style>
    .main {text-align: center;}
    .stTextInput {width: 60% !important; margin: auto; }
    .stButton button {width: 50%; background-colorrgb(0, 91, 165); }
    .stButton button:hover { background-color:rgb(4, 118, 194);}         
</style>
""", unsafe_allow_html=True)

# page title and description
st.title("🗝️ Password Strength Checker")
st.write("Check the strength of your password by entering it below.")

# function to check password strength
def check_password_strength(password):
    score = 0
    feedback = []

    if len(password) >= 8:
        score += 1 
    else:
        feedback.append("❌Password must be at least 8 characters long.")  

    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1      
    else:
        feedback.append("❌Password must contain both uppercase and lowercase letters.")


    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("❌Password must contain at least one number.") 

    #special characters
    if re.search(r"[!@#$%^&*]", password):
        score += 1
    else:
        feedback.append("❌Password should include **at least one special character**")
        
    # display password strength results
    if score == 4:
        st.success("✅ Your password is **strong!** 👍🏻")
    elif score == 3:
        st.info("⚠️ Your password is **medium** strength.")
    else:
        st.error("❌ Your password is **weak**. Please try again.👎🏻")    
   

    # display feedback
    if feedback:
        with st.expander("Improve your password strength"):
            for item in feedback:
                st.write(item)
password = st.text_input("Enter your password", type="password", help="Ensure your password is strong.")


# Button Workflow
if st.button("Check Password Strength"):
    if password:
        check_password_strength(password)
    else:
        st.warning("⚠️ Please enter a password to check its strength.")
