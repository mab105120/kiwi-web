from sqlalchemy import Boolean, Column, Float, Integer, String

from app.db import Base


class User(Base):
    __tablename__ = 'User'
    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String, nullable=False)
    password = Column(String, nullable = False)
    is_active = Column(Boolean, default=True)
    balance = Column(Float, nullable=False)

    def __str__(self):
        return f'<id: {self.id}, name: {self.username}, balance: {self.balance}>'
