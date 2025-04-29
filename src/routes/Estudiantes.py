from flask import Blueprint, jsonify, request
# Models
from models.EstudiantesModel import EstudiantesModel
# Entities
from models.entities.Estudiantes import Estudiantes

main = Blueprint('estudiantes', __name__)

@main.route('/')
def get_estudiantes():
    try:
        estudiantes = EstudiantesModel.get_estudiantes()
        return jsonify(estudiantes), 200
    except Exception as e:
        return jsonify({"message": str(e)}), 500


@main.route('/<cedula>')
def get_estudiante(cedula):
    try:
        estudiante = EstudiantesModel.get_estudiante(cedula)
        if estudiante:
            return jsonify(estudiante), 200
        else:
            return jsonify({"message": "Estudiante no encontrado"}), 404
    except Exception as e:
        return jsonify({"message": str(e)}), 500


@main.route('/add', methods=['POST'])
def add_estudiante():
    try:
        cedula = request.json['cedula']
        nombre = request.json['nombre']
        apellido = request.json['apellido']
        telefono = request.json['telefono']
        n_semestre_actual = int(request.json['n_semestre_actual'])
        promedio_acumulado = float(request.json['promedio_acumulado'])
        serial = request.json['serial']

        estudiante = Estudiantes(cedula, nombre, apellido, telefono, n_semestre_actual, promedio_acumulado, serial)

        affected_rows = EstudiantesModel.add_estudiante(estudiante)
        if affected_rows == 1:
            return jsonify({"message": f"Estudiante {estudiante.cedula} agregado exitosamente"}), 201
        else:
            return jsonify({"message": f"Error al agregar el estudiante {estudiante.cedula}"}), 500

    except Exception as e:
        return jsonify({"message": str(e)}), 500


@main.route('/update/<cedula>', methods=['PUT'])
def update_estudiante(cedula):
    try:
        nombre = request.json['nombre']
        apellido = request.json['apellido']
        telefono = request.json['telefono']
        n_semestre_actual = int(request.json['n_semestre_actual'])
        promedio_acumulado = float(request.json['promedio_acumulado'])
        serial = request.json['serial']

        estudiante = Estudiantes(cedula, nombre, apellido, telefono, n_semestre_actual, promedio_acumulado, serial)

        affected_rows = EstudiantesModel.update_estudiante(estudiante)
        if affected_rows == 1:
            return jsonify({"message": f"Estudiante {estudiante.cedula} actualizado exitosamente"}), 200
        else:
            return jsonify({"message": f"Error al actualizar el estudiante {estudiante.cedula}"}), 404

    except Exception as e:
        return jsonify({"message": str(e)}), 500


@main.route('/delete/<cedula>', methods=['DELETE'])
def delete_estudiante(cedula):
    try:
        estudiante = Estudiantes(cedula, None, None, None, None, None, None)

        affected_rows = EstudiantesModel.delete_estudiante(estudiante)
        if affected_rows == 1:
            return jsonify({"message": f"Estudiante {estudiante.cedula} eliminado exitosamente"}), 200
        else:
            return jsonify({"message": f"Error al eliminar el estudiante {estudiante.cedula}"}), 404

    except Exception as e:
        return jsonify({"message": str(e)}), 500
