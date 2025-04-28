from typing import List

from app.db import get_session
from app.models.exceptions.QueryException import QueryException
from app.models.portfolio import Portfolio


def create_new(name: str, strategy: str, userId: int) -> None:
    try:
        if not isinstance(name, str) or not isinstance(strategy, str) or not isinstance(userId, int):
            raise Exception('Expected input data types: name|str, strategy|str, userId|int')
        portfolio = Portfolio(name=name, strategy=strategy, userId=userId)
        with get_session() as session:
            session.add(portfolio)
            session.commit()
    except Exception as e:
        raise QueryException('Failed to create a new portfolio', e)

def get_portfolios_by_user(userId: int) -> List[Portfolio]:
    return get_session().query(Portfolio).filter(Portfolio.userId == userId).all()

def get_portfolio_by_id(id: int) -> Portfolio:
    return get_session().query(Portfolio).filter(Portfolio.id == id).one()