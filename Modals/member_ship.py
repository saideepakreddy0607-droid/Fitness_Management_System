from datetime import date
from dateutil.relativedelta import relativedelta
class Member_ship :
    # variables
    def __init__(self,member_ship_id,  member_id, member_ship_plan, start_date, end_date):
        self.member_ship_id = member_ship_id
        self.member_id = member_id
        self.member_ship_plan = member_ship_plan
        self.start_date = start_date
        self.end_date = end_date
    # methods
    # Renew member ship 
    def renew_member_ship (self) :
        if self.member_ship_plan == 'silver':
            self.end_date = self.end_date + relativedelta(months=3)
        elif self.member_ship_plan == 'gold':
            self.end_date = self.end_date + relativedelta(months=6)
        elif self.member_ship_plan == 'daimond':
            self.end_date = self.end_date + relativedelta(months=12)
    # check status
    def check_status (self) :
        today = date.today()
        if self.end_date < today:
            return "Expired"
        else :
            return "Active"
