from . import Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy import CheckConstraint


class User(Base):
    __tablename__ = "user"
    uid = Column(Integer, primary_key=True)
    email = Column(String(120), nullable=False)
    first_name = Column(String(20), nullable=False)
    last_name = Column(String(20), nullable=False)
    password = Column(String(20), nullable=False)
    phone_number = Column(String(16), nullable=False)
    postal_code = Column(String(10), nullable=False)
    Dplstation = Column(Integer, ForeignKey('dplstations.station_id'), CheckConstraint('Dplstation > 0'))
    users_deliveries = relationship('Deliveries', backref='User', lazy=True)

class DPLstations(Base):
    __tablename__ = "dplstations"
    station_id = Column(Integer, primary_key=True, CheckConstraint('station_id > 999'))
    city = Column(String(20), nullable=False)
    def __repr__(self):
        return f"email={self.email}, user_del={self.users_deliveries}"


class Deliveries(Base):
    __tablename__ = "deliveries"
    delivery_id = Column(Integer, primary_key = True)
    user_id = Column(Integer, ForeignKey('user.uid'), nullable=False)
    def __repr__(self):
        return f"--did={self.delivery_id}, user_id={self.user_id}--"
