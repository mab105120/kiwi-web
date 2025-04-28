
from typing import List

from sqlalchemy.exc import MultipleResultsFound, NoResultFound

from app.db import get_session
from app.models.exceptions.QueryException import QueryException
from app.models.User import User


def create_user(username: str, password: str, balance: float) -> None:
    try:
        if not isinstance(balance, float):
            raise Exception(f'Balance must be a decimal, found {balance}')
        if username is None or password is None:
            raise Exception('Username and password are both required fields!')
        user = User(username=username, password=password, balance=balance)
        with get_session() as session:
            session.add(user)
            session.commit()
    except Exception as e:
        raise QueryException('Failed to create a new user', e)
    

def password_matches(username: str, password: str) -> bool:
    try: 
        session = get_session()
        user = session.query(User).filter(User.username == username).one()
        return password == user.password
    except NoResultFound:
        raise Exception(f'No user found with username: {username}')
    except MultipleResultsFound:
        raise Exception(f'Unexpected state - found multiple users with same username {username}')
    except Exception as e:
        raise QueryException('Failed while checking username & password', e)

def get_all() -> List[User]:
    try:
        session = get_session()
        return session.query(User).all()
    except Exception as e:
        raise QueryException('Failed to get all users', e)

def get_balance(userId: int) -> float:
    return get_session().query(User).filter(User.id == userId).one()

def delete_user(userId: int) -> None:
    try:
        with get_session() as session:
            user = session.query(User).filter(User.id == userId).one()
            session.delete(user)
            session.commit()
    except Exception as e:
        raise QueryException(f'Failed to delete user with ID {userId}', e)

def update_balance(userId: int, updated_balance: float) -> None:
    with get_session() as session:
        user = session.query(User).filter(User.id == userId).one()
        user.balance = updated_balance
        session.commit()
