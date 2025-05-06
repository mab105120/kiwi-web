
from typing import List

from sqlalchemy.exc import MultipleResultsFound, NoResultFound

from app.extensions import db
from app.models.exceptions.QueryException import QueryException
from app.models.User import User


def create_user(username: str, password: str, balance: float) -> None:
    try:
        if not isinstance(balance, float):
            raise Exception(f'Balance must be a decimal, found {balance}')
        if username is None or password is None:
            raise Exception('Username and password are both required fields!')
        user = User(username=username, password=password, balance=balance)
        db.session.add(user)
        db.session.commit()
    except Exception as e:
        raise QueryException('Failed to create a new user', e)
    

def password_matches(username: str, password: str) -> User:
    try: 
        user = User.query.filter_by(username=username).one()
        if password == user.password:
            return user
        else:
            raise Exception('Username and password do not match')
    except NoResultFound:
        raise Exception(f'No user found with username: {username}')
    except MultipleResultsFound:
        raise Exception(f'Unexpected state - found multiple users with same username {username}')
    except Exception as e:
        raise QueryException('Failed while checking username & password', e)

def get_all() -> List[User]:
    try:
        return User.query.all()
    except Exception as e:
        raise QueryException('Failed to get all users', e)

def get_balance(userId: int) -> float:
    try:
        if not isinstance(userId, int):
            raise ValueError('userId must be an integer')
        user = User.query.filter_by(id=userId).one()
        return user.balance
    except NoResultFound as e:
        raise QueryException(f'No user exists with ID {userId}', e)
    except MultipleResultsFound as e:
        raise QueryException(f'More than one user exist with ID {userId}')
    except Exception as e:
        raise QueryException(f'Failed to get user balance for user with ID {userId}', e)

def delete_user(userId: int) -> None:
    try:
        user = User.query.filter_by(id=userId).one() # add except blocks to handle no or multiple records found.
        db.session.delete(user)
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        raise QueryException(f'Failed to delete user with ID {userId}', e)

# add code for handling exceptions and rolling back the database transaction in the event of a failure.
def update_balance(userId: int, updated_balance: float) -> None:
    user = User.query.filter_by(id=userId).one()
    user.balance = updated_balance
    db.session.commit()
