from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional
from datetime import date
import db_helper

class Expense(BaseModel):
    amount: float
    category: str
    notes: str

class ExpenseDateRange(BaseModel):
    expense_date: date
    amount: float
    category: str
    notes: str

class DateRange(BaseModel):
    start_date: date
    end_date: date


app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Welcome to the Expense Tracking System API"}


@app.get("/expenses_by_date/{expense_date}", response_model=List[Expense])
def get_expenses_for_date(expense_date: date):
    expenses = db_helper.fetch_expenses_for_date(expense_date)
    return expenses


@app.get("/expenses_by_date_range", response_model=List[ExpenseDateRange])
def get_expenses_by_date_range(date_range: DateRange):
    expenses = db_helper.fetch_expenses_for_date_range(date_range.start_date, date_range.end_date)
    return expenses



@app.post("/insert_expenses/{expense_date}")
def add_expenses(expense_date: date, expenses:List[Expense]):
    for expense in expenses:
        db_helper.insert_expenses(expense_date, expense.amount, expense.category, expense.notes)
    return {"message": "Expenses updated successfully!"}


@app.post("/analytics_by_category")
def get_analytics_by_category(date_range: DateRange):
    data = db_helper.fetch_expense_summary_by_category(date_range.start_date, date_range.end_date)
    if data is None:
        raise HTTPException(status_code=500, detail="Failed to retrieve expense summary from the database.")
    
    total = sum([row['total'] for row in data])

    breakdown = {}
    for row in data:
        percentage = (row['total']/total)*100 if total != 0 else 0
        breakdown[row['category']] = {
            "total": row['total'],
            "percentage": percentage
        }
    return breakdown


@app.post("/analytics_by_month")
def get_analytics_by_month(date_range: DateRange):
    data = db_helper.fetch_expense_summary_by_month(date_range.start_date, date_range.end_date)
    if data is None:
        raise HTTPException(status_code=500, detail="Failed to retrieve expense summary from the database.")
    
    total = sum([row['total'] for row in data])

    breakdown = {}
    for row in data:
        percentage = (row['total']/total)*100 if total != 0 else 0
        breakdown[row['month_name']] = {
            "total": row['total'],
            "percentage": percentage
        }
    return breakdown