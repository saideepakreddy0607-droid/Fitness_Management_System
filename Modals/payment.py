class Payment :
    # variables
    def __init__ (self,  payment_id, member_id, amount, payment_date):
        self.payment_id = payment_id
        self.member_id = member_id
        self.amount = amount
        self.payment_date = payment_date
    # methods 
    # update payment 
    def update_payment(self, amount, payment_date):
        self.amount = amount
        self.payment_date = payment_date