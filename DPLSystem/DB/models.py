from . import Base
from sqlalchemy import Column, Integer, String

class User(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True)
    email = Column(String(100))
    # first_name = Column(String)
    # last_name = Column(String)
    # password = Column(String)
    # phone_number = Column(String)
    # postal_code = Column(String)
