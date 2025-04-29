class Estudiantes():

    def __init__(self, cedula, nombre, apellido, telefono, n_semestre_actual, promedio_acumulado, serial):
        self.cedula = cedula
        self.nombre = nombre
        self.apellido = apellido
        self.telefono = telefono
        self.n_semestre_actual = n_semestre_actual
        self.promedio_acumulado = promedio_acumulado
        self.serial = serial

    def to_JSON(self):
        return {
            'cedula': self.cedula,
            'nombre': self.nombre,
            'apellido': self.apellido,
            'telefono': self.telefono,
            'n_semestre_actual': self.n_semestre_actual,
            'promedio_acumulado': self.promedio_acumulado,
            'serial': self.serial
        }
