import streamlit as st
from home_ui import home_page
from add_expenses_ui import add_expenses_page
from view_expenses_ui import view_expenses_page
from analytics_by_category_ui import analytics_by_category_page
from analytics_by_month_ui import analytics_by_month_page

st.sidebar.header("Navigation")
page = st.sidebar.selectbox("Choose an option: ",
                            ["Home", "Add Expenses", "View Expenses", "Analytics By Category", "Analytics By Month"])

# Display the selected page
if page == "Home":
    home_page()
elif page == "Add Expenses":
    add_expenses_page()
elif page == "View Expenses":
    view_expenses_page()
elif page == "Analytics By Category":
    analytics_by_category_page()
elif page == "Analytics By Month":
    analytics_by_month_page()

