import streamlit as st
from datetime import datetime
import pandas as pd
import requests
import matplotlib.pyplot as plt

# API_URL = "http://localhost:8000"
API_URL = "https://expense-tracker-fastapi-backend.onrender.com/"


def analytics_by_month_page():
    st.title("Analyze Your Expenses By Month")
    col1, col2 = st.columns(2)
    with col1:
        start_date = st.date_input("Start Date", datetime(2024, 8, 1))
    with col2:
        end_date = st.date_input("End Date", datetime(2024, 8, 5))

    if st.button("Get Analytics"):
        payload = {
            "start_date": start_date.strftime("%Y-%m-%d"),
            "end_date": end_date.strftime("%Y-%m-%d")
        }

        response = requests.post(f"{API_URL}/analytics_by_month/", json=payload)

        # Check if the response status code is OK
        if response.status_code == 200:
            response = response.json()

            # Check if the response is empty
            if not response:  # If response is an empty dictionary
                st.warning("There is no data present for the selected date range.")
            else:
                data = {
                    "Category": list(response.keys()),
                    "Total": [response[category]["total"] for category in response],
                    "Percentage": [response[category]["percentage"] for category in response]
                }

                df = pd.DataFrame(data)
                df_sorted = df.sort_values(by="Percentage", ascending=False)

                

                # Create a single row for side-by-side charts
                col3, col4 = st.columns(2)

                # Bar Chart
                with col3:
                    plt.figure(figsize=(6, 5))  # Set figure size
                    colors = plt.cm.Set2.colors  # Using the Set2 color palette
                    plt.bar(df_sorted['Category'], df_sorted['Percentage'], color=colors)
                    plt.xlabel('Category')
                    plt.ylabel('Percentage')
                    plt.title('Expense Breakdown by Percentage')
                    plt.xticks(rotation=45, ha='right')  # Rotate x-axis labels for better visibility
                    plt.tight_layout()  # Adjust layout to prevent clipping
                    st.pyplot(plt)  # Display the bar chart

                # Pie Chart
                with col4:
                    plt.figure(figsize=(6, 5))  # Adjust size as needed
                    plt.pie(df_sorted['Total'], labels=df_sorted['Category'], autopct='%1.1f%%', startangle=140, colors=colors)
                    plt.axis('equal')  # Equal aspect ratio ensures that pie chart is circular
                    st.pyplot(plt)  # Display the pie chart

                df_sorted["Total"] = df_sorted["Total"].map("{:.2f}".format)
                df_sorted["Percentage"] = df_sorted["Percentage"].map("{:.2f}".format)

                st.table(df_sorted)
        else:
            st.error("Failed to retrieve analytics. Please try again later.")
