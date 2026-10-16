class Member :
    # variables
    def __init__(self, member_id, name, dob, email, phone_no, address, join_date):
        self.member_id = member_id
        self.name = name
        self.dob = dob
        self.email = email
        self.phone_no = phone_no
        self.address = address
        self.join_date = join_date
    # methods 
    # display member
    def displayMember (self):
        print (f"Member ID: {self.member_id}")
        print (f"Name: {self.name}")
        print (f"Date Of Birth: {self.dob}")
        print (f"Email: {self.email}")
        print (f"Phone Number: {self.phone_no}")
        print (f"Address: {self.address}")
        print (f"Join Date: {self.join_date}")
    # updating member
    # Name
    def updateName (self, name) :
        self.name = name
    # DOB 
    def updateDob (self, dob) :
        self.dob = dob
    # Email
    def updateEmail (self, email) :
        self.email = email
    # Phone Number
    def update_phone_no (self, phone_no) :
            self.phone_no = phone_no
    # Address
    def updateAddress (self, address) :
        self.address = address