import streamlit as st
from datetime import datetime
import requests
import pandas as pd

API_URL = "http://localhost:8000"

def view_expenses_page():
    st.title("View Your Expenses")

    col1, col2 = st.columns(2)
    with col1:
        start_date = st.date_input("Start Date", datetime(2024, 10, 1))
    with col2:
        end_date = st.date_input("End_date", datetime(2024, 10, 5))

    if st.button("View Expenses"):
        payload = {
            "start_date": start_date.strftime("%Y-%m-%d"),
            "end_date": end_date.strftime("%Y-%m-%d")
        }

        response = requests.get(f"{API_URL}/expenses_by_date_range", json=payload)

        if response.status_code == 200:
            existing_expenses=  response.json()
        else:
            st.error("Failed to retrieve expenses.")
            existing_expenses = []

        # Check if any data is returned
        if existing_expenses:
            df = pd.DataFrame(existing_expenses)
            df['amount'] = df['amount'].apply(lambda x: int(x) if x.is_integer() else round(x, 1))
            st.table(df)
        else:
            st.warning(f"No data found for the selected date range: {start_date} to {end_date}.")


        
        