# Expense Management Tracker 💵

## Description
<p>Managing personal or business finances can be overwhelming without the right tools. The Expense Management System simplifies this by allowing users to track their expenses effortlessly. This application provides a seamless way to add, view, and analyze expenses based on date, category, and other filters, ensuring better financial management and decision-making.</p>

## Features
- **Add Expenses:** A straightforward interface to add expenses with details like date, amount, category, and notes.
- **View Expenses:** Filter and view expenses by date range, category, and other criteria.
- **Analyze Expenses:** Visualize and analyze expenses by category and date for better financial insights.
- **Streamlined Backend:** FastAPI backend to handle all database operations and API requests.
- **Interactive Frontend:** A user-friendly Streamlit frontend that allows users to interact with their expense data in real time.

## Technology Stack
* FastAPI: For building the backend REST API.
* Streamlit: To create the interactive frontend interface.
* MySQL: For storing expense data in a relational database.
* Python: Core language for the backend and frontend processing.
* Uvicorn: ASGI server for serving the FastAPI application.

## Backend (FastAPI)
The FastAPI backend handles the following tasks:
* Expense Management: APIs to add, view expenses.
* Date Range Queries: Fetch expenses based on date range filters.
* Category-based Analysis: Filter expenses by category for more detailed insights.

## Frontend (Streamlit)
The Streamlit frontend is designed for ease of use:
* Expense Input: Users can input their expenses in an easy-to-use form.
* Expense Table: View and filter all expenses in a table format.
* Visualization: Analyze expenses through graphical representations and charts.
