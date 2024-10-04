import streamlit as st
from datetime import datetime
import requests
import pandas as pd

API_URL = "http://localhost:8000"

def add_expenses_page():
    st.title("Expense Manager: Add Expenses")

    if 'num_expenses' not in st.session_state:
        st.session_state.num_expenses = 3  # start with one expense entry

    selected_date = st.date_input("Enter Date", datetime.now().date(), label_visibility="collapsed")

    
    categories = ["Food", "Groceries", "Food delivery", "Fuel", "Public Transportation", "Electricity", "Water", "Gas", "Internet","Shopping",
                  "Mobile phone bill", "haircut", "personal care", "Subscriptions(Netflix)", "Movie Tickets", "Rent", "Gym", "Medicines",
                  "Health Insurance", "Loan", "Gifts", "Others"]
    # Form for adding expenses
    with st.form(key="expense_form"):
        col1, col2, col3 = st.columns(3)
        with col1:
            st.text("Amount")
        with col2:
            st.text("Categories")
        with col3:
            st.text("Notes")
        # List to store entered expenses
        expenses = []

        for i in range(st.session_state.num_expenses):
            with col1:
                amount_input = st.number_input("Amount", min_value=0, step=1, value=0, label_visibility="collapsed", key=f"amount_{i}")
            with col2:
                category_input = st.selectbox(label="Category", options=categories, label_visibility="collapsed", key=f"category_{i}")
            with col3:
                notes_input = st.text_input(label="Notes", value="", label_visibility="collapsed", key=f"notes_{i}")

            expenses.append({
                'amount': amount_input,
                'category': category_input,
                'notes': notes_input
            })
        # Submit button for the form
        submit_button = st.form_submit_button("Submit Expenses")

        if submit_button:
            filtered_expenses = [expense for expense in expenses if expense['amount'] > 0]
            
            response = requests.post(f"{API_URL}/insert_expenses/{selected_date}", json=filtered_expenses)
            if response.status_code == 200:
                st.success("Expenses Updated Successfully.")
            else:
                st.error(f"Failed to update expenses. Error: {response.text}")

    # Add another expense button outside the form
    if st.button("+ Add another expense"):
        st.session_state.num_expenses += 1

    # View the added expenses on that date
    if st.button("View Expenses", key="view_single_date_expesnses"):
        response = requests.get(f"{API_URL}/expenses_by_date/{selected_date}")
        if response.status_code == 200:
            existing_responses = response.json()

            st.write(f"Expenses on {selected_date}: ")
            if existing_responses:
                df = pd.DataFrame(existing_responses)
                df['amount'] = df['amount'].apply(lambda x: int(x) if x.is_integer() else round(x, 1))  
                st.table(df)
            else:
                st.write("No data found for the selected date.")  
        
        else:
            st.error("Failed to retrieve expenses")
            existing_responses =[ ]