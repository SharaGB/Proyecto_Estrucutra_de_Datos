from database.db import get_connection
from .entities.Estudiantes import Estudiantes


class EstudiantesModel():

    @classmethod
    def get_estudiantes(self):
        try:
            connection = get_connection()
            estudiantes = []

            with connection.cursor() as cursor:
                cursor.execute("SELECT * FROM estudiantes_ingenieria ORDER BY apellido ASC")
                resultset = cursor.fetchall()

                for row in resultset:
                    estudiante = Estudiantes(
                        cedula=row[0],
                        nombre=row[1],
                        apellido=row[2],
                        telefono=row[3],
                        n_semestre_actual=row[4],
                        promedio_acumulado=row[5],
                        serial=row[6]
                    )
                    estudiantes.append(estudiante.to_JSON())

            connection.close()
            return estudiantes
        except Exception as e:
            print(f"Error: {e}")


    @classmethod
    def get_estudiante(self, cedula):
        try:
            connection = get_connection()

            with connection.cursor() as cursor:
                cursor.execute("SELECT * FROM estudiantes_ingenieria WHERE cedula = %s", (cedula,))
                row = cursor.fetchone()

                if row:
                    estudiante = Estudiantes(
                        row[0],
                        row[1],
                        row[2],
                        row[3],
                        row[4],
                        row[5],
                        row[6]
                    )
                    estudiante = estudiante.to_JSON()

            connection.close()
            return estudiante

        except Exception as e:
            print(f"Error: {e}")


    @classmethod
    def add_estudiante(self, estudiante):
        try:
            connection = get_connection()

            with connection.cursor() as cursor:
                cursor.execute("""INSERT INTO estudiantes_ingenieria (
                    cedula,
                    nombre,
                    apellido,
                    telefono,
                    n_semestre_actual,
                    promedio_acumulado,
                    serial)
                    VALUES (%s, %s, %s, %s, %s, %s, %s)""",
                    (estudiante.cedula, estudiante.nombre, estudiante.apellido, estudiante.telefono, estudiante.n_semestre_actual, estudiante.promedio_acumulado, estudiante.serial))
                affected_rows = cursor.rowcount
                connection.commit()

            connection.close()
            return affected_rows

        except Exception as e:
            print(f"Error: {e}")


    @classmethod
    def update_estudiante(self, estudiante):
        try:
            connection = get_connection()

            with connection.cursor() as cursor:
                cursor.execute("""UPDATE estudiantes_ingenieria SET
                               nombre = %s,
                               apellido = %s,
                               telefono = %s,
                               n_semestre_actual = %s,
                               promedio_acumulado = %s,
                               serial = %s
                               WHERE cedula = %s""",
                    (estudiante.nombre, estudiante.apellido, estudiante.telefono, estudiante.n_semestre_actual, estudiante.promedio_acumulado, estudiante.serial, estudiante.cedula))
                affected_rows = cursor.rowcount
                connection.commit()

            connection.close()
            return affected_rows

        except Exception as e:
            print(f"Error: {e}")


    @classmethod
    def delete_estudiante(self, estudiante):
        try:
            connection = get_connection()

            with connection.cursor() as cursor:
                cursor.execute("DELETE FROM estudiantes_ingenieria WHERE cedula = %s", (estudiante.cedula,))
                affected_rows = cursor.rowcount
                connection.commit()

            connection.close()
            return affected_rows

        except Exception as e:
            print(f"Error: {e}")
