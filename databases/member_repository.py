from databases.connection import get_connection
class MemberRepository:
    def add_member(self, member):
        connection = get_connection()
        cursor = connection.cursor()

        query = """
            INSERT INTO Member
            (Member_Id, Name, DOB, Email, Phone_no, Address, Join_Date)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
        """
        values = (
            member.member_id,
            member.name,
            member.dob,
            member.email,
            member.phone_no,
            member.address,
            member.join_date
        )
        cursor.execute(query, values)
        connection.commit()

        cursor.close()
        connection.close()
    def get_member(self, member_id):
        connection = get_connection()
        cursor = connection.cursor()

        query = "SELECT * FROM Member WHERE Member_Id = %s"
        values = (member_id,)

        cursor.execute(query, values)

        row = cursor.fetchone()

        cursor.close()
        connection.close()

        return row
    def update_name(self, member_name, member_id):
        connection = get_connection()
        cursor = connection.cursor()

        query = """
            UPDATE Member
            SET Name = %s
            WHERE Member_Id = %s
        """

        values = (member_name, member_id)

        cursor.execute(query, values)
        connection.commit()

        cursor.close()
        connection.close()

    def update_dob(self, dob, member_id):
        connection = get_connection()
        cursor = connection.cursor()

        query = """
            UPDATE Member
            SET DOB = %s
            WHERE Member_Id = %s
        """

        values = (dob, member_id)

        cursor.execute(query, values)
        connection.commit()

        cursor.close()
        connection.close()

    def update_email(self, email, member_id):
        connection = get_connection()
        cursor = connection.cursor()

        query = """
            UPDATE Member
            SET email = %s
            WHERE Member_Id = %s
        """

        values = (email, member_id)

        cursor.execute(query, values)
        connection.commit()

        cursor.close()
        connection.close()

    def update_phone_no (self, phone_no, member_id):
        connection = get_connection()
        cursor = connection.cursor()

        query = """
            UPDATE Member
            SET Phone_No = %s
            WHERE Member_Id = %s
        """

        values = (phone_no, member_id)

        cursor.execute(query, values)
        connection.commit()

        cursor.close()
        connection.close()

    def update_address (self, address, member_id):
        connection = get_connection()
        cursor = connection.cursor()

        query = """
            UPDATE Member
            SET Address = %s
            WHERE Member_Id = %s
        """

        values = (address ,member_id)

        cursor.execute(query, values)
        connection.commit()

        cursor.close()
        connection.close()
    def delete_member(self, member_id) :
        connection = get_connection()
        cursor = connection.cursor()

        query = """
                delete from member where member_id = %s
                """
        value = (member_id,)

        cursor.execute(query, value)
        connection.commit()

        cursor.close()
        connection.close()