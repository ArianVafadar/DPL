from .models import User
from . import Session


class dbHandler():
    def add(self):
        user = User(id = 1,email="Sina@sina.com")
        Session.add(user)
        Session.commit()
    ##add Db funcitona
