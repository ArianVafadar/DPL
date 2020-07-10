from . import Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship


class User(Base):
    __tablename__ = "user"
    uid = Column(Integer, primary_key=True)
    email = Column(String(120))
    first_name = Column(String(20))
    last_name = Column(String(20))
    password = Column(String(20))
    phone_number = Column(String(16))
    postal_code = Column(String(10))
    Dplstation = Column(Integer, ForeignKey('dplstations.station_id'))
    users_deliveries = relationship('Deliveries', backref='User', lazy=True)

class DPLstations(Base):
    __tablename__ = "dplstations"
    station_id = Column(Integer, primary_key=True)
    city = Column(String(20))
    def __repr__(self):
        return f"email={self.email}, user_del={self.users_deliveries}"


class Deliveries(Base):
    __tablename__ = "deliveries"
    delivery_id = Column(Integer, primary_key = True)
    user_id = Column(Integer, ForeignKey('user.uid'), nullable=False)
    def __repr__(self):
        return f"--did={self.delivery_id}, user_id={self.user_id}--"
