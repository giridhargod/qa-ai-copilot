import streamlit as st
from main import run  # we’ll tweak this

st.set_page_config(page_title="QA AI Copilot", layout="wide")

st.title("🧠 QA AI Copilot")
st.markdown("Analyze UI, detect PII, and generate test cases using AI")

user_input = st.text_area("Enter URL or screen description")

if st.button("Run Analysis"):
    if user_input:
        with st.spinner("Running AI agents..."):
            result = run(user_input)

        st.success("Analysis Complete!")

        st.subheader("📊 Output")
        st.text(result)

    else:
        st.warning("Please enter input first.")