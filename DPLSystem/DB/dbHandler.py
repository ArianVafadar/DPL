from .models import User, Deliveries, DPLstations
from . import Session

class dbHandler():
    def check_passcode(_passcode):
        '''
            checks the given _passcode to see if it belongs to any of the deliveries
            if it exists then it will return the delivery_id of the delivery
            otherwise it will return -1
        '''
        # query = Session.query(Deliveries).filter_by(passcode = _passcode).first()
        # if not query:
        #     return -1
        # return query.delivery_id
    def check_cam_readings(self,_code):
        '''
            checks the given _code to see if it belongs to any of the deliveries
            if it exists then it will return the delivery_id of the delivery
            otherwise it will return -1
        '''
        pass

    def update_delivery_status(self, _deliveryId):
        pass

    def testFunc(self, x):
        query = Session.query(Deliveries).filter_by(delivery_id=x).first()
        print(query)
        if not query:
            return -1
        return query.delivery_id
