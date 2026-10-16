from databases.connection import get_connection

class TrainerRepository:

    def add_trainer(self, trainer):
        connection = get_connection()
        cursor = connection.cursor()

        query = """
            INSERT INTO Trainer
            (Trainer_Id, Trainer_Name, Trainer_Phno)
            VALUES (%s, %s, %s)
        """

        values = (
            trainer.trainer_id,
            trainer.trainer_name,
            trainer.trainer_phno
        )

        cursor.execute(query, values)
        connection.commit()

        cursor.close()
        connection.close()

    def get_trainer(self, trainer_id):
        connection = get_connection()
        cursor = connection.cursor()

        query = """
            SELECT * FROM Trainer
            WHERE Trainer_Id = %s
        """

        cursor.execute(query, (trainer_id,))
        result = cursor.fetchone()

        cursor.close()
        connection.close()

        return result

    def update_trainer(self, trainer_id, trainer_name, trainer_phno):
        connection = get_connection()
        cursor = connection.cursor()

        query = """
            UPDATE Trainer
            SET Trainer_Name = %s,
                Trainer_Phno = %s
            WHERE Trainer_Id = %s
        """

        values = (trainer_name, trainer_phno, trainer_id)

        cursor.execute(query, values)
        connection.commit()

        cursor.close()
        connection.close()

    def delete_trainer(self, trainer_id):
        connection = get_connection()
        cursor = connection.cursor()

        query = """
            DELETE FROM Trainer
            WHERE Trainer_Id = %s
        """

        cursor.execute(query, (trainer_id,))
        connection.commit()

        cursor.close()
        connection.close()