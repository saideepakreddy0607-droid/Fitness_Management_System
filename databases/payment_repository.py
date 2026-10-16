from databases.connection import get_connection

class PaymentRepository:

    def add_payment(self, payment):
        connection = get_connection()
        cursor = connection.cursor()

        query = """
            INSERT INTO Payment
            (Payment_Id, Member_Id, Amount, Payment_Date)
            VALUES (%s, %s, %s, %s)
        """

        values = (
            payment.payment_id,
            payment.member_id,
            payment.amount,
            payment.payment_date
        )

        cursor.execute(query, values)
        connection.commit()

        cursor.close()
        connection.close()

    def get_payment(self, payment_id):
        connection = get_connection()
        cursor = connection.cursor()

        query = """
            SELECT * FROM Payment
            WHERE Payment_Id = %s
        """

        cursor.execute(query, (payment_id,))
        result = cursor.fetchone()

        cursor.close()
        connection.close()

        return result

    def update_payment(self, payment_id, amount, payment_date):
        connection = get_connection()
        cursor = connection.cursor()

        query = """
            UPDATE Payment
            SET Amount = %s,
                Payment_Date = %s
            WHERE Payment_Id = %s
        """

        values = (amount, payment_date, payment_id)

        cursor.execute(query, values)
        connection.commit()

        cursor.close()
        connection.close()

    def delete_payment(self, payment_id):
        connection = get_connection()
        cursor = connection.cursor()

        query = """
            DELETE FROM Payment
            WHERE Payment_Id = %s
        """

        cursor.execute(query, (payment_id,))
        connection.commit()

        cursor.close()
        connection.close()