import json
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from edgar.sec_edgar_extraction.ingest_income_statement import get_income_statement
from edgar.sec_edgar_extraction.ingest_balance_sheet import get_balance_sheet

def main(event, context):
    body = json.loads(event.get("body", "{}"))
    ticker = body.get("ticker")
    form_type = body.get("form_type", "10-Q")
    fiscal_year = body.get("fiscal_year")
    fiscal_quarter = body.get("fiscal_quarter")

    # Basic validation
    if not ticker or not fiscal_year or not fiscal_quarter:
        return {
            "statusCode": 400,
            "body": json.dumps({"error": "Missing required parameters"}),
            "headers": {"Content-Type": "application/json"},
        }

    try:
        # Example: extract both balance sheet and income statement
        balance_sheet = get_balance_sheet(
            ticker=ticker,
            form_type=form_type,
            fiscal_year=fiscal_year,
            fiscal_quarter=fiscal_quarter,
        )
        income_statement = get_income_statement(
            ticker=ticker,
            form_type=form_type,
            fiscal_year=fiscal_year,
            fiscal_quarter=fiscal_quarter,
        )
        return {
            "statusCode": 200,
            "body": json.dumps({
                "balance_sheet": balance_sheet.dict() if hasattr(balance_sheet, "dict") else balance_sheet,
                "income_statement": income_statement.dict() if hasattr(income_statement, "dict") else income_statement,
            }),
            "headers": {"Content-Type": "application/json"},
        }
    except Exception as e:
        return {
            "statusCode": 500,
            "body": json.dumps({"error": str(e)}),
            "headers": {"Content-Type": "application/json"},
        }