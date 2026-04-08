from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
from typing import List

router = APIRouter()
templates = Jinja2Templates(directory="src/templates")


class AmortizationRequest(BaseModel):
    purchase_price: float
    down_payment_pct: float   # percentage, e.g. 20.0
    annual_interest_rate: float  # percentage, e.g. 6.5
    term_years: int


class PaymentRow(BaseModel):
    month: int
    payment: float
    principal: float
    interest: float
    balance: float


class AmortizationResponse(BaseModel):
    monthly_payment: float
    loan_amount: float
    total_paid: float
    total_interest: float
    schedule: List[PaymentRow]


def calculate_amortization(
    purchase_price: float,
    down_payment_pct: float,
    annual_interest_rate: float,
    term_years: int,
) -> AmortizationResponse:
    loan_amount = purchase_price * (1 - down_payment_pct / 100)
    monthly_rate = (annual_interest_rate / 100) / 12
    n = term_years * 12

    if monthly_rate == 0:
        monthly_payment = loan_amount / n
    else:
        monthly_payment = loan_amount * (monthly_rate * (1 + monthly_rate) ** n) / ((1 + monthly_rate) ** n - 1)

    schedule: List[PaymentRow] = []
    balance = loan_amount
    for month in range(1, n + 1):
        interest = balance * monthly_rate
        principal = monthly_payment - interest
        balance = max(balance - principal, 0)
        schedule.append(
            PaymentRow(
                month=month,
                payment=round(monthly_payment, 2),
                principal=round(principal, 2),
                interest=round(interest, 2),
                balance=round(balance, 2),
            )
        )

    total_paid = monthly_payment * n
    total_interest = total_paid - loan_amount

    return AmortizationResponse(
        monthly_payment=round(monthly_payment, 2),
        loan_amount=round(loan_amount, 2),
        total_paid=round(total_paid, 2),
        total_interest=round(total_interest, 2),
        schedule=schedule,
    )


@router.get("/calculator", response_class=HTMLResponse)
def calculator_page(request: Request):
    return templates.TemplateResponse("calculator.html", {"request": request})


@router.post("/api/calculate", response_model=AmortizationResponse)
def api_calculate(data: AmortizationRequest):
    return calculate_amortization(
        data.purchase_price,
        data.down_payment_pct,
        data.annual_interest_rate,
        data.term_years,
    )
