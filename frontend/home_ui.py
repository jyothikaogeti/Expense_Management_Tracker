import streamlit as st

def home_page():
    
    st.markdown(
    """
    <style>
    .full-width-image {
        width: 100%; /* Full width */
        height: 200px; /* Controlled height */
        object-fit: cover; /* Maintain aspect ratio and cover */
    }
    </style>
    <img class="full-width-image" src="https://c7.alamy.com/comp/2FKHRFY/tracking-expenses-is-written-in-a-document-on-the-office-desk-with-office-accessories-keyboard-and-diagram-2FKHRFY.jpg"/>
    """,
    unsafe_allow_html=True
    )

    st.markdown("<h1 style='text-align: center;'>Expense Management Tracker 💵</h1>", unsafe_allow_html=True)

    # Brief description
    st.markdown(
        """
        <h4 style='text-align: center;'><em>Your one-stop solution for managing and analyzing your expenses!</em></h4>
        <p style='text-align: center;'>
        Track, analyze, and get detailed insights into your spending habits.
        This application is designed to help you make smarter financial decisions 
        by giving you a clear breakdown of your daily, weekly, and monthly expenses.
        </p>
        """,
        unsafe_allow_html=True
    )

    # Additional content to enhance the page
    st.markdown(
        """
        <div style="text-align: center; font-size: 1.2em;">
            <p><strong>Key Features:</strong></p>
            <ul style="list-style-type: none;">
                <li>✔️ Add and track expenses with ease.</li>
                <li>✔️ View your expense history in a clear and organized manner.</li>
                <li>✔️ Gain insights with interactive graphs and analytics.</li>
                <li>✔️ Stay on top of your budget and savings goals.</li>
            </ul>
        </div>
        """,
        unsafe_allow_html=True
    )