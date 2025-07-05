import streamlit as st
import pandas as pd
import os
import requests

# ✅ Streamlit page config - must be first
st.set_page_config(page_title="TalentScout Hiring Assistant", page_icon="🤖")

# ✅ Function to call Mistral via Ollama locally
def generate_questions(tech_stack):
    prompt = f"""
You are an AI Hiring Assistant.

Generate exactly 5 technical interview questions for a candidate skilled in: {tech_stack}.
Each question should be relevant to technical interviews.
Format the output as:
1. Question 1
2. Question 2
3. Question 3
4. Question 4
5. Question 5
Only return the list of questions.
"""
    try:
        response = requests.post(
            "http://localhost:11434/api/generate",
            json={"model": "mistral", "prompt": prompt, "stream": False},
            timeout=60
        )
        response.raise_for_status()
        data = response.json()
        return data["response"].strip()
    except Exception as e:
        return f"❌ Failed to generate questions: {e}"

# ✅ Streamlit App UI
st.title("🤖 TalentScout Hiring Assistant")

# ✅ Track session state
if "step" not in st.session_state:
    st.session_state.step = "start"
    st.session_state.data = {}

# ✅ Step 1: Greeting
if st.session_state.step == "start":
    st.markdown("👋 **Welcome to TalentScout!** Let’s begin the candidate screening process.")
    st.session_state.step = "form"

# ✅ Step 2: Candidate Form
if st.session_state.step == "form":
    st.subheader("📋 Candidate Information")
    with st.form("candidate_form"):
        name = st.text_input("Full Name")
        email = st.text_input("Email Address")
        phone = st.text_input("Phone Number")
        experience = st.text_input("Years of Experience")
        position = st.text_input("Desired Position(s)")
        location = st.text_input("Current Location")
        tech_stack = st.text_area("Tech Stack (e.g., Python, SQL, Django, Git)")

        submit = st.form_submit_button("Submit")
        if submit:
            st.session_state.data = {
                "Name": name,
                "Email": email,
                "Phone": phone,
                "Experience": experience,
                "Position": position,
                "Location": location,
                "Tech Stack": tech_stack
            }
            st.session_state.step = "questions"

# ✅ Step 3: Show Technical Questions
if st.session_state.step == "questions":
    st.subheader("🧠 Technical Questions Based on Your Tech Stack")
    tech_stack = st.session_state.data.get("Tech Stack", "").strip()

    if not tech_stack:
        st.error("❌ No tech stack provided. Please restart.")
    else:
        with st.spinner("Generating questions..."):
            questions = generate_questions(tech_stack)

        for line in questions.split('\n'):
            if line.strip():
                st.markdown(f"✅ {line.strip()}")

        # ✅ Save to CSV
        df = pd.DataFrame([st.session_state.data])
        if os.path.exists("candidate_data.csv"):
            df.to_csv("candidate_data.csv", mode='a', header=False, index=False)
        else:
            df.to_csv("candidate_data.csv", index=False)

        st.success("✅ Thank you! Your information has been recorded.")
        st.session_state.step = "end"

# ✅ Step 4: Restart Option
if st.session_state.step == "end":
    if st.button("🔁 Start Over"):
        st.session_state.step = "start"
        st.session_state.data = {}
