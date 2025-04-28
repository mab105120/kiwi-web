from datetime import date
from typing import List

from app.db import get_session
from app.models.exceptions.QueryException import QueryException
from app.models.investment import Investment
from app.services.db.portfolio_dao import get_portfolio_by_id
from app.services.db.user_dao import get_balance, update_balance


def get_investments_by_portfolio(portfolioId: int) -> List[Investment]:
    session = get_session()
    return session.query(Investment).filter(Investment.portfolio_id == portfolioId).all()

def get_investments(investmentId: int) -> Investment:
    with get_session() as session:
        return session.query(Investment).filter(Investment.id == investmentId).one()

def harvest_investment(investmentId: int) -> None:
    with get_session() as session:
        investment = session.query(Investment).filter(Investment.id == investmentId).one()
        session.delete(investment)
        session.commit()

def update_qty(investmentId: int, qty: int) -> None:
    with get_session() as session:
        investment = session.query(Investment).filter(Investment.id == investmentId).one()
        investment.quantity = qty
        session.commit()

def purchase(porftolio_id, ticker, price, quantity):
    try:
        userId: int = get_portfolio_by_id(porftolio_id).userId.value
        balance: float = get_balance(userId)
        investment_cost: float = price * quantity
        if balance < investment_cost:
            raise Exception('No sufficient funds')
        investment = Investment(portfolio_id=porftolio_id, ticker=ticker, price=price, quantity=quantity, date=date.today())
        with get_session() as session:
            session.add(investment)
            session.commit()
            update_balance(userId, balance - investment_cost)
    except Exception as e:
        raise QueryException('Failed to place purchase order', e)

def sell(investmentId, qty, sale_price):
    investment: Investment = get_investments(investmentId)
    available_qty: int = investment.quantity
    if qty > available_qty:
        raise Exception(f'Quantity provided on sale order ({qty}) exceeds user available quantity ({available_qty})')
    if qty == available_qty:
        harvest_investment(investmentId)
    else:
        updated_qty = available_qty - qty
        update_qty(investmentId, updated_qty)
    proceeds: float = qty * sale_price
    portfolio = get_portfolio_by_id(investment.portfolio_id)
    userId: int = portfolio.userId
    old_balance = get_balance(userId)
    update_balance(userId, old_balance + proceeds)