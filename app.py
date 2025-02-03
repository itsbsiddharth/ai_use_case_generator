# app.py
# SQLite Version Fix - MUST BE FIRST
__import__('pysqlite3')
import sys
sys.modules['sqlite3'] = sys.modules.pop('pysqlite3')

# Rest of your imports
# ... rest of your existing code ...
import streamlit as st
from src.main import crew

st.title("AI Use Case Generator")

# User input for company/industry
company_name = st.text_input("Enter the company name:")
industry = st.text_input("Enter the industry:")

if st.button("Generate Use Cases"):
    if company_name and industry:
        # Pass user input to the crew
        result = crew(company_name, industry)

        # Display the results in a structured format
        st.write("## Market Research")
        st.markdown(result["tasks_output"][0].raw)  # Display research output

        st.write("## Use Case Proposal")
        st.markdown(result["tasks_output"][1].raw)  # Display use case output

        st.write("## Feasibility Check (Resources)")
        st.markdown(result["tasks_output"][2].raw)  # Display resource output

    else:
        st.error("Please enter both the company name and industry.")