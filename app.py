# Add this at the VERY TOP of app.py
try:
    __import__('pysqlite3')
    import sys
    sys.modules['sqlite3'] = sys.modules.pop('pysqlite3')
except ImportError:
    import sys
    sys.modules['sqlite3'] = __import__('sqlite3')
    pass  # Fallback to system sqlite3

# Then your regular imports
import streamlit as st
from src.main import crew

# Rest of your code...

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