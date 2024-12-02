from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from datetime import datetime
from config import Base


class Users_Table(Base):
    __tablename__ = 'users'

    u_id = Column(Integer, primary_key=True, autoincrement=True)
    u_name = Column(String, nullable=False)
    u_email = Column(String, unique=True, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)


class Orders_Table(Base):
    __tablename__ = 'orders'

    o_id = Column(Integer, primary_key=True, autoincrement=True)
    u_id = Column(Integer, ForeignKey('Users.u_id'))  # User Id as a foreign key
    product_name = Column(String, nullable=False)
    quantity = Column(Integer)
    order_date = Column(DateTime, default=datetime.utcnow(), nullable=False)
