from databases.connection import get_connection


class MembershipRepository:

    def add_membership(self, membership):
        connection = get_connection()
        cursor = connection.cursor()

        query = """
            INSERT INTO Membership
            (Member_Ship_Id, Member_Id, Member_Ship_Plan, Start_Date, End_Date)
            VALUES (%s, %s, %s, %s, %s)
        """

        values = (
            membership.member_ship_id,
            membership.member_id,
            membership.member_ship_plan,
            membership.start_date,
            membership.end_date
        )

        cursor.execute(query, values)
        connection.commit()

        cursor.close()
        connection.close()

    def get_membership(self, member_ship_id):
        connection = get_connection()
        cursor = connection.cursor()

        query = """
            SELECT * FROM Membership
            WHERE Member_Ship_Id = %s
        """

        cursor.execute(query, (member_ship_id,))
        result = cursor.fetchone()

        cursor.close()
        connection.close()

        return result

    def update_membership(self, member_ship_id, plan, start_date, end_date):
        connection = get_connection()
        cursor = connection.cursor()

        query = """
            UPDATE Membership
            SET Member_Ship_Plan = %s,
                Start_Date = %s,
                End_Date = %s
            WHERE Member_Ship_Id = %s
        """

        values = (plan, start_date, end_date, member_ship_id)

        cursor.execute(query, values)
        connection.commit()

        cursor.close()
        connection.close()

    def delete_membership(self, member_ship_id):
        connection = get_connection()
        cursor = connection.cursor()

        query = """
            DELETE FROM Membership
            WHERE Member_Ship_Id = %s
        """

        cursor.execute(query, (member_ship_id,))
        connection.commit()

        cursor.close()
        connection.close()