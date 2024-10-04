import mysql.connector
from contextlib import contextmanager
from logging_setup import setup_logger

logger = setup_logger('db_helper')

@contextmanager
def get_db_cursor(commit=False):
    connection = mysql.connector.connect(
        host= "b5bx8qbigdu2rroeb7fn-mysql.services.clever-cloud.com",
        user= "ueeenrp2cpz4wdl7",
        password= "Od7AQTpNJoI3TLtQsBx6",
        database= "b5bx8qbigdu2rroeb7fn"
    )
    cursor = connection.cursor(dictionary=True)
    yield cursor
    if commit:
        connection.commit()
    cursor.close()
    connection.close()

# This function fetches the expenses on a particular date.
def fetch_expenses_for_date(expense_date):
    logger.info(f"fetch_expenses called with {expense_date}")
    with get_db_cursor() as cursor:
        cursor.execute("SELECT * FROM expenses WHERE expense_date=%s", (expense_date,))
        expenses = cursor.fetchall()
        return expenses
    
# This function fetches the expenses on given data range.
def fetch_expenses_for_date_range(start_date, end_date):
    logger.info(f"fecth_expenses_for_date_range called with start_date: {start_date} and end_date: {end_date}")
    with get_db_cursor() as cursor:
        cursor.execute(
            '''
            SELECT * FROM
            expenses WHERE expense_date
            BETWEEN %s and %s;
            ''',
            (start_date, end_date)
        )
        expenses = cursor.fetchall()
        return expenses


# This function inserts the data into expenses table
def insert_expenses(expense_date, amount, category, notes):
    logger.info(f"insert_expenses called iwth date: {expense_date}, amount: {amount}, category: {category}, notes: {notes}")
    with get_db_cursor(commit=True) as cursor:
        cursor.execute(
            "INSERT INTO expenses (expense_date, amount, category, notes) VALUES (%s, %s, %s, %s)",
            (expense_date, amount, category, notes)
        )

# This function is to delete data from expenses table
def delete_expenses(expense_id):
    with get_db_cursor(commit=True) as cursor:
        cursor.execute("DELETE FROM expenses WHERE id = %s", (expense_id,))

        # check if any row has affected
        if cursor.rowcount == 0:
            logger.warning(f"Expense with id: {expense_id} not found.")
            return False
        else:
            logger.info(f"Expense with id: {expense_id} deleted successfully.")
            return True
        
# This function gives summary of expenses by category.
def fetch_expense_summary_by_category(start_date, end_date):
    logger.info(f"fetch_expense_summary_by_category called with start_date: {start_date} and end_date: {end_date}")
    with get_db_cursor() as cursor:
        cursor.execute(
            '''
            SELECT category, SUM(amount) as total
            FROM expenses WHERE expense_date
            BETWEEN %s and %s
            GROUP BY category;
            ''',
            (start_date, end_date)
        )
        data_summary = cursor.fetchall()
        if not data_summary:
            logger.info(f"No expenses found for the date range: {start_date} to {end_date}")
        return data_summary

# This function gives summary of expenses month wise.
def fetch_expense_summary_by_month(start_date, end_date):
    logger.info(f"fetch_expense_summary_by_month called with start_date: {start_date} and end_date: {end_date}")
    with get_db_cursor() as cursor:
        cursor.execute(
            '''
            SELECT
                DATE_FORMAT(expense_date, '%M') AS month_name,
                SUM(amount) AS total
            FROM expenses
            WHERE expense_date BETWEEN %s and %s
            GROUP BY MONTH(expense_date), month_name
            ORDER BY MONTH(expense_date)
            ''',
            (start_date, end_date)
        )
        data_summary = cursor.fetchall()
        if not data_summary:
            logger.info(f"No expenses found for the range: {start_date} to {end_date}")
        return data_summary




####################  CODE TESTING ##############################

insert_expenses("2024-10-01", 1000, "Entertainment", "watched devara movie")

# # delete_expenses(67)

# # expenses = fetch_expenses_for_date("2024-10-01")
# # print(expenses)

# expenses_summary = fetch_expense_summary_by_month("2024-08-01", "2024-10-31")
# print(expenses_summary)